import os

def create_scaffold(scaffold: dict, base_dir="generated_project"):
    os.makedirs(base_dir, exist_ok=True)
    for folder, files in scaffold.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for filename, code in files.items():
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)