from langchain.tools import tool

from desk_buddy.data.notes import NOTES


@tool
def lookup_notes(topic: str) -> str:
    """Ищет заметку: langchain, langgraph или reducer."""
    key = topic.strip().lower()
    return NOTES.get(key, f"Нет заметки про '{topic}'. Есть: {', '.join(NOTES)}")
