import pandas as pd

def get_priority_tasks(df: pd.DataFrame) -> pd.DataFrame:
    """Return high priority tasks that are not completed."""
    df = df.copy()
    df['priority'] = df['priority'].str.lower()
    df['status'] = df['status'].str.lower()

    high_priority = df[
        (df['priority'] == 'high') &
        (df['status'] != 'completed')
    ]
    return high_priority.sort_values(by="due_date")


def get_task_summary(df: pd.DataFrame) -> str:
    """Return a text summary of completed vs pending tasks."""
    total = len(df)
    completed = len(df[df['status'].str.lower() == 'completed'])
    pending = len(df[df['status'].str.lower() != 'completed'])

    return (
        f"You have {total} tasks in total.\n"
        f"- ✅ {completed} completed\n"
        f"- ⏳ {pending} pending"
    )
