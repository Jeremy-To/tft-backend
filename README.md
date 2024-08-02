# Analyseur de Malware et Forensique

Cette application Flask fournit une API pour analyser des fichiers à des fins de détection de malware et d'investigation forensique.

## Fonctionnalités

### Analyse de Malware
- Extraction de chaînes de caractères
- Calcul d'entropie
- Énumération des en-têtes
- Détermination du langage de programmation
- Analyse des sections
- Détection de packer
- Liste des imports et exports
- Recherche de signatures YARA

### Analyse Forensique
- Extraction de chaînes de caractères
- Extraction de métadonnées

## Prérequis

- Python 3.7+
- Flask
- pefile
- yara-python
- Autres dépendances listées dans `requirements.txt`

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :
pip install -r requirements.txt
## Utilisation

1. Lancez l'application :
python app.py
ou avec Gunicorn :
gunicorn app:application

2. Envoyez une requête POST à `/analyze` avec les paramètres suivants :
- `file` : Le fichier à analyser
- `analysis_type` : `malware` ou `forensic`
- `operation` : L'opération spécifique à effectuer

### Exemple de requête

```python
import requests

url = "http://localhost:5000/analyze"
files = {"file": open("sample.exe", "rb")}
data = {"analysis_type": "malware", "operation": "strings"}

response = requests.post(url, files=files, data=data)
print(response.json())
Opérations disponibles
Malware

strings : Extraction de chaînes
entropy : Calcul d'entropie
headers : Énumération des en-têtes
language : Détermination du langage
sections : Analyse des sections
packer : Détection de packer
imports : Liste des imports
exports : Liste des exports
yara : Recherche de signatures YARA

Forensique

strings : Extraction de chaînes
metadata : Extraction de métadonnées

Configuration YARA
Pour utiliser la recherche de signatures YARA, spécifiez le répertoire des règles YARA avec le paramètre yara_dir dans la requête.
Sécurité
Assurez-vous de déployer cette application dans un environnement sécurisé, car elle manipule potentiellement des fichiers malveillants.
Licence
Ce projet est sous licence MIT.
