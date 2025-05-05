import pandas as pd
import os
from logic.task_analyzer import get_priority_tasks, get_task_summary
from logic.focus_analyzer import get_focus_summary
from logic.charts import plot_task_status, plot_focus_trend
import streamlit as st

DATA_PATH = "data"

def handle_priority_tasks(user_input: str) -> str:
    try:
        tasks_df = pd.read_csv(os.path.join(DATA_PATH, "tasks.csv"))
        top_tasks = get_priority_tasks(tasks_df)

        if top_tasks.empty:
            return "You have no high priority tasks right now."

        st.markdown("### 🔥 Top Priority Tasks")
        st.dataframe(top_tasks[["title", "priority", "due_date"]])
        return f"You have {len(top_tasks)} high priority tasks."
    except Exception as e:
        return f"Error reading tasks: {e}"

def handle_task_summary(user_input: str) -> str:
    try:
        tasks_df = pd.read_csv(os.path.join(DATA_PATH, "tasks.csv"))
        summary = get_task_summary(tasks_df)

        st.markdown("### 📊 Task Status Overview")
        fig = plot_task_status(tasks_df)
        st.pyplot(fig)

        return summary
    except Exception as e:
        return f"Could not generate task summary: {e}"

def handle_focus_summary(user_input: str) -> str:
    try:
        timer_df = pd.read_csv(os.path.join(DATA_PATH, "timer_log.csv"))
        summary, weekly_df = get_focus_summary(timer_df)

        st.markdown("### 🧠 Focus Time This Week")
        fig = plot_focus_trend(weekly_df)
        st.pyplot(fig)

        return summary
    except Exception as e:
        return f"Unable to analyze focus sessions: {e}"

def handle_unknown(user_input: str) -> str:
    return "I'm not sure how to help with that yet. Try asking about your tasks, progress, or focus time."
