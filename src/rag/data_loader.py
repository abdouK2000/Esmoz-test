"""
Module to load data from the data folder
"""
import json
from typing import List, Dict
from conf.config_file import DATA_PATH


def clean_text(text: str) -> str:
    """
    Helper function to clean text
    
    Args:
        text: text to clean and pre-process.
    
    Returns:
        Cleaned text"""

    return text.lower().split()

def load_entretiens(data_path: str = DATA_PATH) -> List[Dict]:
    """
    Helper function that loads meeting data.

    Args:
        data_path

    Returns:
        A list of entretiens objects and their associated contents.
    """

    entretiens_path = DATA_PATH / "entretiens"
    if not entretiens_path.exists():
        print("Dossier des entretiens indisponible.")
    else : 
        print("Dossier des entretiens retrouvé.")

    entretiens = []

    for file in DATA_PATH.rglob("*"):
        try:
            with open(file) as json_data:
                data = json.load(json_data)
                print(data)
                entretiens.extend(data)

        except Exception as e:
            print(str(e))

    return entretiens

def load_documents(data_path: str = DATA_PATH) -> List[Dict]:
    pass # à définir


