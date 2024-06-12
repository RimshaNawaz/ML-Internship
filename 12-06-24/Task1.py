"Directory Metadata Analyzer"
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_directory_info(root_dir):
    """
    Recursively traverse the directory to gather information about all files and folders.
    
    Parameters:
    ----------
    root_dir (str): The root directory to start the traversal.
    
    Returns:

    list: A list of dictionaries containing metadata for each file and folder.
    """
    records = []
    
    for root, dirs, files in os.walk(root_dir):
        folder_size = 0
        num_files = len(files)
        
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            folder_size += file_size
            file_extension = os.path.splitext(file)[1]
            
            records.append({
                'file_name': file,
                'file_size': file_size,
                'folder': root,
                'file_extension': file_extension
            })
        
        records.append({
            'file_name': None,
            'file_size': folder_size,
            'folder': root,
            'file_extension': None,
            'num_files_in_folder': num_files
        })
    
    return records

def main(root_dir):
    """
    Main function to gather file metadata, generate summaries, save results, and create visualizations.
    
    Parameters:
    ----------
    root_dir (str): The root directory to start the traversal.

    Returns:
    -------
    None

    """
    records = get_directory_info(root_dir)
    df = pd.DataFrame(records)
    
    # Sorting by file extension
    df = df.sort_values(by='file_extension')
    
    # Generating summary
    summary = df.groupby('file_extension').agg(
        total_size=pd.NamedAgg(column='file_size', aggfunc='sum'),
        count=pd.NamedAgg(column='file_name', aggfunc='count')
    ).reset_index()
    
    # Saving the results
    df.to_csv('file_records.csv', index=False)
    summary.to_csv('summary.csv', index=False)
    
    # Visualizing the data
    plt.figure(figsize=(10, 6))
    sns.barplot(data=summary, x='file_extension', y='total_size')
    plt.xticks(rotation=90)
    plt.title('Total Size by File Extension')
    plt.xlabel('File Extension')
    plt.ylabel('Total Size (bytes)')
    plt.tight_layout()
    plt.savefig('total_size_by_extension.png')
    plt.show()

if __name__ == "__main__":
    root_dir = 'E:\\Check'
    main(root_dir)
