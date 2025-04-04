import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__inti__.py",
    f"src/{project_name}/components/__inti__.py",
    f"src/{project_name}/utils/__inti__.py",
    f"src/{project_name}/config/__inti__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__inti__.py",
    f"src/{project_name}/entity/__inti__.py",
    f"src/{project_name}/constants/__inti__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb" 


]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")

    