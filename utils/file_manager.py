import os
import pandas as pd

DATA_FOLDER = "data"

def load_csv(filename):
    """Safely load a CSV file from the data folder."""
    path = os.path.join(DATA_FOLDER, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"'{filename}' not found in /data.")
    
    return pd.read_csv(path)

def save_csv(df, filename):
    """Save a DataFrame to the data folder."""
    path = os.path.join(DATA_FOLDER, filename)
    df.to_csv(path, index=False)
