import pandas as pd
import os


def load_raw_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded CSV: {os.path.basename(file_path)}")
        return df
    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error loading CSV {file_path}: {e}")
        return None
