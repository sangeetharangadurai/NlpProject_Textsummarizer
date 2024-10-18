import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = 'textsummarizer'

list_files = [
    ".github/workflows/.gitkeep/"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "tests/__init__.py",
    "tests/test_text_summarizer.py",
    "tests/conftest.py",
]

for file in list_files:
    file_path = Path(file)
    filedir,filename = os.path.split(file_path)

    if filedir!= "":
        if not os.path.exists(filedir):
            logging.info(f"Creating directory: {filedir}")
            os.makedirs(filedir,exist_ok=True)
    
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        logging.info(f"Creating file: {file}")
        with open(file, 'w') as f:
            pass
    else:
        logging.info(f"File {file} already exists and is not empty.")
    
    