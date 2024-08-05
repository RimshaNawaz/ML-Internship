import pandas as pd

def load_data(file_path):
    """Load data from an Excel file."""
    df = pd.read_excel(file_path, sheet_name=None)
    data = df[list(df.keys())[0]]  # Get the first sheet's data
    data.columns = ['Disease Name', 'Symptoms', 'Specialist Doctor']
    return data
