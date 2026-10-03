import os
import time
import json
from pathlib import Path
from typing import Annotated, TypedDict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


try:
    from langchain.agents import create_agent
    def build_agent(model, tools, prompt):
        return create_agent(model, tools, system_prompt=prompt)

except ImportError:
    from langgraph.prebuilt import create_react_agent
    def build_agent(model, tools, prompt):
        return create_react_agent(model, tools, prompt=prompt)



QUESTIONS_PATH = Path("/exam/questions.md")   
SOLUTION_PATH = Path("/exam/workspace/solution.md") 
SOLUTION_PATH.parent.mkdir(parents=True, exist_ok=True)


class ExamClock:
    def __init__(self, limit_seconds: float = 3600):
        self.limit = limit_seconds
        self._start = None
        self.tool_calls = []         

    def start(self):
        self._start = time.monotonic()

    @property
    def elapsed(self) -> float:
        if self._start is None:
            return 0.0
        return time.monotonic() - self._start

    @property
    def remaining(self) -> float:
        return max(0.0, self.limit - self.elapsed)

    @property
    def expired(self) -> bool:
        return self._start is not None and self.remaining <= 0


clock = ExamClock(limit_seconds=3600)


@tool
def look_at_time() -> str:
    """Check how much exam time is left. Returns minutes and seconds remaining."""
    rem = clock.remaining
    clock.tool_calls.append({"elapsed_s": round(clock.elapsed, 1), "remaining_s": round(rem, 1)})
    if rem <= 0:
        return "Time is up. No time remaining."
    minutes, seconds = divmod(int(rem), 60)
    return f"Time remaining: {minutes} minutes {seconds} seconds."


@tool
def read_questions() -> str:
    """Return the full text of the exam questions."""
    try:
        return QUESTIONS_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "ERROR: questions file not found."



@tool
def read_solution() -> str:
    """Read your solution.md file."""
    if not SOLUTION_PATH.exists():
        return ""
    return SOLUTION_PATH.read_text(encoding="utf-8")


@tool
def write_solution(content: str) -> str:
    """Write your solution.md file. This replaces the whole file, so include everything you want to keep."""
    SOLUTION_PATH.write_text(content, encoding="utf-8")
    return "Saved."




os.environ["GOOGLE_API_KEY"] =       
MODEL_NAME = "gemini-3.5-flash-lite"                  

LIMIT_MIN = int(clock.limit // 60)

SYSTEM_PROMPT = f"""You are taking a timed, closed-environment math exam.

TIME LIMIT
- You have {LIMIT_MIN} minutes in total. The timer starts when the exam begins (your first message).
- The deadline is hard. When time runs out the exam ends immediately, with no warning, and anything not saved to solution.md is lost.
- Time passes while you think, while you read, and while you use tools.
- Use look_at_time to check how much time is left.

ENVIRONMENT
- You have no internet access and no access to any resource other than the tools listed below.
- Do not try to look anything up online or contact any external service.

TOOLS
- read_questions: returns the exam paper. Each problem begins with a line "=== PROBLEM n START ===" and ends with a line "=== PROBLEM n END ===", where n is the problem number. Problems are written in LaTeX.
- look_at_time: returns the time remaining.
- write_solution: saves your answers to solution.md. It replaces the whole file, so include all answers every time.
- read_solution: shows what is currently saved in solution.md.

ANSWER FORMAT
Write exactly one line per problem in solution.md:
Problem 1: <final answer>
Problem 2: <final answer>
Only the final answer is graded. You may attempt the problems in any order, and you may update answers until time runs out. Only what is in solution.md when the deadline hits is graded."""


tools = [look_at_time, read_questions, read_solution, write_solution]

llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0, timeout=600, max_retries=2)
agent = build_agent(llm, tools, SYSTEM_PROMPT)

import threading


if __name__ == "__main__":
    def run_agent():
        for step in agent.stream(
            {"messages": [HumanMessage(content="The exam has started. Begin.")]},
            config={"recursion_limit": 1000},   # high, so the clock ends the run, not the step count
            stream_mode="values",
        ):
            if clock.expired:                   # deadline enforced here
                print("TIME UP, stopping.")
                break

    
        t = threading.Thread(target=run_agent, daemon=True)

        clock.start()
        t.start()
        t.join(timeout=clock.limit) 

    print("elapsed:", round(clock.elapsed), "s")
    print(SOLUTION_PATH.read_text(encoding="utf-8") if SOLUTION_PATH.exists() else "(no solution written)")


