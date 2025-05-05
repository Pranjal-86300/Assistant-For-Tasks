import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_task_status(df: pd.DataFrame):
    """Generate a bar plot showing task status distribution."""
    df = df.copy()
    df["status"] = df["status"].str.title()

    status_counts = df["status"].value_counts()

    fig, ax = plt.subplots()
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="Set2", ax=ax)
    ax.set_title("Task Status Overview")
    ax.set_ylabel("Number of Tasks")
    ax.set_xlabel("Status")
    plt.xticks(rotation=15)
    return fig


def plot_focus_trend(weekly_df: pd.DataFrame):
    """Plot total focus time per week."""
    fig, ax = plt.subplots()
    sns.lineplot(data=weekly_df, x="week", y="duration_minutes", marker="o", ax=ax)
    ax.set_title("Weekly Focus Time Trend")
    ax.set_xlabel("Week")
    ax.set_ylabel("Minutes Focused")
    plt.xticks(rotation=45)
    return fig
