"""
Deprecated database module. The Render deployment is stateless and does not persist chats.
All functions are kept as no-ops to preserve imports if any legacy code references them.
"""

def create_chat_index(chat_id: str):  # pragma: no cover - legacy stub
    raise NotImplementedError("Database disabled: stateless deployment")


def store_chat_metadata(user_id: str, chat_id: str, title: str | None = None):  # pragma: no cover
    raise NotImplementedError("Database disabled: stateless deployment")


def fetch_user_chats(user_id: str):  # pragma: no cover
    return []


def update_chat_last_activity(user_id: str, chat_id: str):  # pragma: no cover
    return None


def store_query_response(chat_id: str, query: str, response: str, user_id: str | None = None):  # pragma: no cover
    return None


def fetch_similar_query_responses(chat_id: str, query: str, limit: int = 5):  # pragma: no cover
    return []


def fetch_chat_messages(chat_id: str, limit: int = 500):  # pragma: no cover
    return []


def delete_chat(user_id: str, chat_id: str):  # pragma: no cover
    return False