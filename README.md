# Step 1.

MODEL_PATH in src/conf/config_file.py must be set to the path of the local LLM model to be used, weights must be in GGUF format.

# Step 2.

uv venv

# Step 3.

source .venv/Script/activate

OU, Si la machine est type MacOS ou Linux:

source ./venv/Bin/activate

# Step 4.

uv sync

# Step 5.

python src/main.py

# SUITE DE L'ENTRETIEN

J'aurais continué d'implémenter la logique du fonctionnement, mettre en place les briques d'analyse et synthèse de l'entretien, boucler sur le contenu des règles dans le JSON. des documents plus longs auraient exigé les briques de chunking, et vectorisation (ChromaDB pour un projet local par exemple), puis une brique retrieval et finalement complétion.

le résultat serait stocké dans le dossier 'results/'

Idéalement, le projet serait sous forme de package installable.
