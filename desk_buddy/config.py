import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()

DEFAULT_MODEL = "google_genai:gemini-4-hydrogen"
DEFAULT_THREAD_ID = "me"


def get_model_name() -> str:
    return os.getenv("MODEL", DEFAULT_MODEL)


def get_thread_id() -> str:
    return os.getenv("THREAD_ID", DEFAULT_THREAD_ID)


def get_llm() -> BaseChatModel:
    return init_chat_model(get_model_name(), temperature=0)
