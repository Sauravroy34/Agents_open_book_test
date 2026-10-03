from langchain_core.tools import tool


@tool
def read_questions():
    "Use this tool to read the questions"
    path = "file_path"

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

        return content.strip()
