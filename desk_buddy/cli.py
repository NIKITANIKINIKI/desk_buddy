from langchain.messages import HumanMessage

from desk_buddy.config import get_thread_id
from desk_buddy.graph.builder import build_graph


def message_text(message) -> str:
    content = message.content
    if isinstance(content, str):
        return content
    if isinstance(content, list) and content:
        first = content[0]
        if isinstance(first, dict):
            return str(first.get("text", first))
        return str(getattr(first, "text", first))
    return str(content)


def run_cli() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": get_thread_id()}}

    print("Desk Buddy. Пустая строка — выход.")
    while True:
        text = input("you> ").strip()
        if not text:
            break
        out = graph.invoke({"messages": [HumanMessage(content=text)]}, config)
        print("bot>", message_text(out["messages"][-1]))
