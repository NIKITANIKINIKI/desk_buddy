from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import START, StateGraph

from desk_buddy.graph.nodes import assistant, call_tools, should_continue
from desk_buddy.graph.state import State


def build_graph():
    return (
        StateGraph(State)
        .add_node("assistant", assistant)
        .add_node("tools", call_tools)
        .add_edge(START, "assistant")
        .add_conditional_edges("assistant", should_continue)
        .add_edge("tools", "assistant")
        .compile(checkpointer=InMemorySaver())
    )
