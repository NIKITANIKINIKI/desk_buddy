from langchain.messages import SystemMessage, ToolMessage
from langgraph.graph import END

from desk_buddy.config import get_llm
from desk_buddy.graph.state import State
from desk_buddy.prompts import SYSTEM
from desk_buddy.tools import TOOLS, TOOLS_BY_NAME

llm_with_tools = get_llm().bind_tools(TOOLS)


def assistant(state: State) -> dict:
    return {
        "messages": [
            llm_with_tools.invoke(
                [SystemMessage(content=SYSTEM), *state["messages"]]
            )
        ]
    }


def call_tools(state: State) -> dict:
    last = state["messages"][-1]
    results = []
    for call in last.tool_calls:
        result = TOOLS_BY_NAME[call["name"]].invoke(call["args"])
        results.append(ToolMessage(content=str(result), tool_call_id=call["id"]))
    return {"messages": results}


def should_continue(state: State) -> str:
    last = state["messages"][-1]
    return "tools" if getattr(last, "tool_calls", None) else END
