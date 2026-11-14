from desk_buddy.tools.calculator import add
from desk_buddy.tools.notes import lookup_notes

TOOLS = [lookup_notes, add]
TOOLS_BY_NAME = {tool.name: tool for tool in TOOLS}

__all__ = ["TOOLS", "TOOLS_BY_NAME", "lookup_notes", "add"]
