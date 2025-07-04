import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s]:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "DockerFile",
    "setup.py",
    "research/research.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir  = filepath.parent
    
    if filedir:
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")        