# DataTable

> Created by alex lamizana in 18/09/2024
----------------------------------------------------------------------------

## Formation Piscine Python pour la science des données - 2

### [Index](/README.md)

- Apprendre à charger, manipuler et afficher des tableaux de données.

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Instructions spécifiques.](#instructions-spécifiques)
3. [Exercice 00: Load my Dataset.](#exercice-00)

----------------------------------------------------------------------------

### Règles générales

- Effectuer le rendu des modules à partir d'un ordinateur du cluster, soit en utilisant une machine virtuelle :
  - Choisir le système d'exploitation à utiliser pour votre machine virtuelle
  - Votre machine virtuelle doit disposer de tous les logiciels nécessaires à la réalisation de votre projet.
  - Ces logiciels doivent être configurés et installés.

- On peux également utiliser l'ordinateur directement si les outils sont disponibles.
  - S'assurer d'avoir l'espace nécessaire sur notre session pour installer ce dont on à besoin pour tous les modules (utilisez le goinfre si votre campus en dispose).
  - Tous doit etre installé installé avant les évaluations.

- Nos fonctions ne doivent pas se terminer de manière inattendue (erreur de segmentation, erreur de bus, double libération, etc.)

> Si cela se produit, votre projet sera considéré comme non fonctionnel et recevra un 0 lors de l'évaluation.

- Nous vous encourageons à créer des programmes de test pour votre projet, même si ce travail ne devra pas être présenté et ne sera pas noté.
Cela vous donnera l'occasion de tester facilement votre travail et celui de vos camarades.
Ces tests vous seront particulièrement utiles lors de votre soutenance.
En effet, lors de la soutenance, vous êtes libre d'utiliser vos tests
et/ou les tests du pair que vous évaluez.

- Soumettez votre travail au dépôt git qui vous a été attribué. Seul le travail dans le dépôt git sera noté. Si Deepthought est chargé de noter votre travail, il le fera
après l'évaluation par les pairs.

> [!NOTE]
> Si une erreur se produit dans une section de votre travail
> pendant l'évaluation de Deepthought, l'évaluation sera interrompue.

- Vous devez utiliser la version 3.10 de Python.
- Vous pouvez utiliser n'importe quelle fonction intégrée si elle n'est pas interdite dans l'exercice.
- Vos importations de librairies doivent être explicites, par exemple vous devez:

```python
import numpy as np
```

Importer:

```python
from pandas import *
```

n'est pas autorisé, et vous obtiendrez 0 à l'exercice.

- Il n'y a pas de variable globale.

----------------------------------------------------------------------------

## Instructions spécifiques

- Pas de code dans le champ d'application global. ***Utilisez des fonctions !***

- Chaque programme doit avoir sa partie principale et ne pas être un simple script :

```python
def main():
# your tests and your error handling

if __name__ == "__main__":
  main()
```

- ***Toute exception non levée invalidera les exercices***, même en cas d'erreur que l'on vous a demandé de tester.

- Toutes vos fonctions doivent avoir une documentation (```__doc__```)

- Votre code doit être à la norme:

```bash
pip install flake8
alias norminette=flake8

# Pour lancer la commande:
python3 -m flake8 main.py 
```

- Pour ce module, nous utiliserons les données de ***FREE SCHOOL MATERIALS FROM GAP-
MINDER.ORG, LICENCE CC-BY***

- Nous vous encourageons à consulter les données disponibles si vous souhaitez vous former à la manipulation des données ou à la vision des données.

----------------------------------------------------------------------------

## Exercice 00

### Load my Dataset

- Turn-in directory : ***ex00/***
- Files to turn in : [load_csv.py](/DataTable/ex00/load_csv.py)
- Allowed functions :  ```pandas``` or any lib for data set manipulations

Créez une fonction qui prend un chemin comme argument, écrit les dimensions de l'ensemble de données et le renvoie. 

- Vous devez gérer les cas d'erreur et renvoyer None si le chemin est mauvais,
mauvais format...


Le prototype de la fonction est :

```python
# DataTable/ex00/load_csv.py

def load(path: str) -> Dataset: (You have to adapt the type of return according to your library)
  #your code here
```

Le main():

```python
# DataTable/ex00/main.py

from load_csv import load

print(load("life_expectancy_years.csv"))
```

resultat attendu:

```python
$> python tester.py
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
$>
```

> [!NOTE]
> Vous pouvez afficher l'ensemble de données dans le format de votre choix, le format donné n'étant pas restrictif.

### Notions abordées

En France, la loi reconnaît le droit d'obtenir la communication des documents détenus par une administration,
quels que soient leur forme ou leur support. C’est ce que l’on appelle ***l’OpenData*** (données ouvertes).
Ainsi, de nombreux sites mettent à la disposition des citoyens des données. En voici quelques exemples:

https://www.data.gouv.fr/fr/
http://www.geonames.org/
http://www.opendatafrance.net/
https://data.nantesmetropole.fr/pages/home


Le format CSV (pour **Comma Separated Values**, soit en français valeurs séparées par des virgules) est un format très pratique pour représenter des données structurées. Dans ce format, chaque ligne représente un enregistrement et, sur une même ligne, les différents champs de l’enregistrement sont séparés par une virgule (d’où le nom).
En pratique, on peut spécifier le caractère utilisé pour séparer les différents champs. On utilise fréquemment un point-virgule, une tabulation ou deux points. Notons enfin que la première ligne d’un tel fichier est souvent utilisée pour indiquer le nom des différents champs.

Ouverture d'un ficher **csv** avec un script python.
- La méthode classique est simplement d’utiliser la fonction ```read_csv()```en indiquant le chemin du fichier csv :
```python
import pandas as pd

fichier = pd.read_csv('chemin/happiness.csv')
```

----------------------------------------------------------------------------

## Exercice 01

### Draw my country

- Turn-in directory : ***ex01/***
- Files to turn in : [load_csv.py, aff_life.py](/DataTable/ex01/aff_life.py)
- Allowed functions : ```matplotlib```, ```seaborn``` or any lib for Data Visualization

Créez un programme qui appelle la fonction load de l'exercice précédent, charge le fichier
```life_expectancy_years.csv```, et affiche les informations sur le pays de votre campus. 
- Votre graphique doit avoir **un titre et une légende pour chaque axe**.