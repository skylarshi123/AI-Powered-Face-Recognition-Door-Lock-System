import json
import pyperclip
import sys

def copy_ipynb_to_clipboard(file_path):
    try:
        # Read the .ipynb file
        with open(file_path, 'r', encoding='utf-8') as file:
            notebook = json.load(file)
        
        # Extract all cell contents
        cell_contents = []
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                cell_contents.append('```python\n' + ''.join(cell['source']) + '\n```\n')
            elif cell['cell_type'] == 'markdown':
                cell_contents.append(''.join(cell['source']) + '\n')
        
        # Join all cell contents
        full_content = '\n'.join(cell_contents)
        
        # Copy to clipboard
        pyperclip.copy(full_content)
        print(f"Contents of {file_path} have been copied to clipboard.")
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_ipynb_file>")
    else:
        file_path = sys.argv[1]
        copy_ipynb_to_clipboard(file_path)