from pathlib import Path
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env"
    "requirements.txt",
    "setup.py",
    "aap.py"
    "README.md",
    "reserach/trails.ipnb"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent

    # Create directory if not exists
    if not file_dir.exists():
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}")

    # Create file if not exists or is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"File already exists: {file}")





