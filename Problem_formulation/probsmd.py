import json
import random
from pathlib import Path
import uuid

import pandas as pd

URL = "https://raw.githubusercontent.com/google-deepmind/superhuman/refs/heads/main/imobench/answerbench_v2.csv"
imo_answer_df = pd.read_csv(URL, dtype=str)


unique_id = str(uuid.uuid4())

# Change these in one place; the file and your system prompt stay in sync.
# {n} is replaced with the problem number.
START_DELIM = "=== PROBLEM {n} START ==="
END_DELIM = "=== PROBLEM {n} END ==="


def _filter_categories(df: pd.DataFrame, categories) -> pd.DataFrame:
    """Keep only the requested categories (str or list of str, case-insensitive)."""
    if categories is None:
        return df
    if isinstance(categories, str):
        categories = [categories]

    valid = {c.lower(): c for c in df["Category"].dropna().unique()}
    wanted = []
    for c in categories:
        key = c.strip().lower()
        if key not in valid:
            raise ValueError(f"Unknown category '{c}'. Valid options: {sorted(valid.values())}")
        wanted.append(valid[key])

    return df[df["Category"].isin(wanted)]


def generate_questions(
    df: pd.DataFrame,
    category: bool = False,          # show "Category : X" lines in questions file
    categories=None,                 # restrict to e.g. "Algebra" or ["Algebra", "Number Theory"]
    n: int | None = None,
    per_category: int | None = None,
    seed: int | None = 0,
    out_dir: str = ".",
    questions_file: str = f"{unique_id}_questions.md",
    solutions_file: str = f"{unique_id}_questions_category_id_solution_map.json",
):
    rng = random.Random(seed)

    # ---- filter ----
    df = _filter_categories(df, categories)
    if df.empty:
        raise ValueError("No problems left after filtering.")

    # ---- sampling ----
    if per_category is not None:
        parts = [
            g.sample(n=min(per_category, len(g)), random_state=rng.randint(0, 2**31 - 1))
            for _, g in df.groupby("Category")
        ]
        sampled = pd.concat(parts)
    elif n is not None:
        sampled = df.sample(n=min(n, len(df)), random_state=rng.randint(0, 2**31 - 1))
    else:
        sampled = df.copy()

    # ---- ordering ----
    if category:
        sampled = sampled.sort_values("Category", kind="stable")
    else:
        sampled = sampled.sample(frac=1, random_state=rng.randint(0, 2**31 - 1))
    sampled = sampled.reset_index(drop=True)

    # ---- build plain-text file + solution map ----
    lines = []
    solution_map = {}
    current_cat = None

    for i, row in enumerate(sampled.to_dict("records"), start=1):
        problem_id = row["Problem ID"]
        problem = str(row["Problem"]).strip()
        answer = str(row["Short Answer"]).strip()
        cat = row["Category"]

        if category and cat != current_cat:
            if current_cat is not None:
                lines.append("")
            lines.append(f"Category : {cat}")
            lines.append("")
            current_cat = cat

        lines.append(START_DELIM.format(n=i))
        lines.append(problem)
        lines.append(END_DELIM.format(n=i))
        lines.append("")

        solution_map[problem_id] = {
            "number": i,
            "category": cat,
            "problem": problem,
            "solution": answer,
        }

    text = "\n".join(lines).rstrip() + "\n"

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / questions_file).write_text(text, encoding="utf-8")
    (out / solutions_file).write_text(
        json.dumps(solution_map, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    return str(out / questions_file), solution_map



generate_questions(imo_answer_df, categories=None, n=20, seed=42, out_dir="run_nt")
