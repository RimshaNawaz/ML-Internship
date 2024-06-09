'Synchronizes files between different directories'
import os
import shutil
import filecmp
import time
def sync_directories(source_dir, target_dir):
    """
    Synchronize files between source and target directories.

    Parameters
    ----------
    source_dir : str
        The path to the source directory.
    target_dir : str
        The path to the target directory.

    Returns
    -------
    None
    """
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        
        if os.path.isdir(source_item):
            sync_directories(source_item, target_item)
        else:
            if not os.path.exists(target_item) or not filecmp.cmp(source_item, target_item, shallow=False):
                shutil.copy2(source_item, target_item)
                print(f"Copied {source_item} to {target_item}")
    for item in os.listdir(target_dir):
        target_item = os.path.join(target_dir, item)
        source_item = os.path.join(source_dir, item)
        
        if not os.path.exists(source_item):
            if os.path.isdir(target_item):
                shutil.rmtree(target_item)
                print(f"Removed directory {target_item}")
            else:
                os.remove(target_item)
                print(f"Removed file {target_item}")

def main():
    """
    Main function to run the file synchronization tool.
    Returns
    -------
    None
    """
    source_dir = input("Enter the path to the source directory: ")
    target_dir = input("Enter the path to the target directory: ")

    while True:
        sync_directories(source_dir, target_dir)
        print(f"Synchronized {source_dir} with {target_dir}")
        time.sleep(10) 
        

if __name__ == "__main__":
    main()
