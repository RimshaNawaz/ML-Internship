'Basic Text Editor'
import os
def open_file(filename):
    """
    Open a file and read its contents.

    Parameters
    ----------
    filename : str
        The name of the file to open.

    Returns
    -------
    str
        The contents of the file.
    """
    if os.path.exists(filename):
        with open(filename, 'r',encoding="utf-8") as file:
            return file.read()
    else:
        print(f"File {filename} does not exist.")
        return ""

def save_file(filename, content):
    """
    Save the given content to a file.

    Parameters
    ----------
    filename : str
        The name of the file to save to.
    content : str
        The content to save in the file.

    Returns
    -------
    None
    """
    with open(filename, 'w',encoding="utf-8") as file:
        file.write(content)
    print(f"File {filename} saved successfully.")

def search_and_replace(content, search_term, replace_term):
    """
    Search for a term in the content and replace it with another term.

    Parameters
    ----------
    content : str
        The content to search within.
    search_term : str
        The term to search for.
    replace_term : str
        The term to replace the search term with.

    Returns
    -------
    str
        The content after search and replace.
    """
    return content.replace(search_term, replace_term)

def get_word_count(content):
    """
    Get the word count of the content.

    Parameters
    ----------
    content : str
        The content to count words in.

    Returns
    -------
    int
        The number of words in the content.
    """
    return len(content.split())

def display_content_with_line_numbers(content):
    """
    Display the content with line numbers.

    Parameters
    ----------
    content : str
        The content to display.

    Returns
    -------
    None
    """
    lines = content.split('\n')
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line}")

def main():
    """
    Main function to run the text editor.

    Returns
    -------
    None
    """
    content = ""
    filename = ""

    while True:
        print("\nBasic Text Editor")
        print("1. Open File")
        print("2. Edit Content")
        print("3. Save File")
        print("4. Search and Replace")
        print("5. Display Content with Line Numbers")
        print("6. Word Count")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filepath to open the file: ")
            content = open_file(filename)
            print(f"Content of {filename}:")
            print(content)
        elif choice == '2':
            print("Enter the content (end with an empty line):")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = '\n'.join(lines)
        elif choice == '3':
            if filename == "":
                filename = input("Enter the proper filepath to save the file: ")
            save_file(filename, content)
        elif choice == '4':
            search_term = input("Enter the search term: ")
            replace_term = input("Enter the replace term: ")
            content = search_and_replace(content, search_term, replace_term)
            print("Content after search and replace:")
            print(content)
        elif choice == '5':
            print("Content with line numbers:")
            display_content_with_line_numbers(content)
        elif choice == '6':
            word_count = get_word_count(content)
            print(f"Word count: {word_count}")
        elif choice == '7':
            print("Exiting the text editor.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
