import pandas as pd
from datetime import datetime

def get_focus_summary(df: pd.DataFrame):
    """Return focus time summary and weekly trend DataFrame."""
    df['date'] = pd.to_datetime(df['date'])
    df['duration_minutes'] = pd.to_numeric(df['duration_minutes'], errors='coerce')
    df = df.dropna(subset=["duration_minutes"])

    total_minutes = df["duration_minutes"].sum()
    session_count = len(df)

    summary = (
        f"You've logged {session_count} focus sessions\n"
        f"Total focus time: {int(total_minutes)} minutes ({int(total_minutes // 60)}h {int(total_minutes % 60)}m)"
    )

    # Weekly summary
    df['week'] = df['date'].dt.to_period("W").apply(lambda r: r.start_time.date())
    weekly_df = df.groupby("week")["duration_minutes"].sum().reset_index()

    return summary, weekly_df
