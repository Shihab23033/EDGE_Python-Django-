import os

def delete_file(file_path):
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")

if __name__ == "__main__":
    delete_file("test.txt")
   # input("Press Enter to continue...")  # This will pause execution until the user presses Enter