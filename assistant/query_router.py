from assistant.handlers import handle_task_summary, handle_priority_tasks, handle_focus_summary, handle_unknown
from assistant.nlp_utils import extract_keywords

def route_query(user_input: str) -> str:
    keywords = extract_keywords(user_input)

    if "priority" in keywords or "important" in keywords:
        return handle_priority_tasks(user_input)
    elif "complete" in keywords or "summary" in keywords or "report" in keywords:
        return handle_task_summary(user_input)
    elif "focus" in keywords or "session" in keywords or "time" in keywords:
        return handle_focus_summary(user_input)
    else:
        return handle_unknown(user_input)
