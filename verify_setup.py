import sys
import os

def check_setup():
    print("Checking setup...")
    
    # 1. Check Python version
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print("WARNING: Python version is less than 3.8. Recommended 3.8+")
    else:
        print("Python version OK.")
        
    # 2. Check Directory Structure
    required_dirs = [
        "api", "data", "frontend", "models", "notebooks", 
        "src", "src/chatbot", "src/utils", "tests"
    ]
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming this script is run from project root c:\Chatbot
    # If run via tool, we can hardcode or rely on CWD.
    # Let's verify relative to CWD.
    
    missing_dirs = []
    for d in required_dirs:
        if not os.path.isdir(d):
            missing_dirs.append(d)
            
    if missing_dirs:
        print(f"MISSING DIRECTORIES: {missing_dirs}")
    else:
        print("Directory structure OK.")
        
    # 3. Check Files
    required_files = ["requirements.txt", ".gitignore", "README.md"]
    missing_files = []
    for f in required_files:
        if not os.path.isfile(f):
            missing_files.append(f)
            
    if missing_files:
        print(f"MISSING FILES: {missing_files}")
    else:
        print("Essential files OK.")
        
    print("\nSetup verification complete.")

if __name__ == "__main__":
    check_setup()
