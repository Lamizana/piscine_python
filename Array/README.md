# Array

> Created by alex lamizana in 11/09/2024
----------------------------------------------------------------------------

## Formation Piscine Python pour la science des données - 1

### [Index](/README.md)

- Découvrir les tableaux, leurs manipulations et le travail sur les images.

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Instructions spécifiques.](#instructions-spécifiques)
3. [Exercice 00: Give my BMI.](#exercice-00)
4. [Exercice 01: 2D array.](#exercice-01)
5. [Exercice 02: Load my image.](#exercice-02)

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

----------------------------------------------------------------------------

## Exercice 00

### Give my BMI

- Turn-in directory : ***ex00/***
- Files to turn in : [give_bmi.py](/Array/ex00/give_bmi.py)
- Allowed functions :  ```numpy``` or any lib of table manipulation

Votre fonction, ```give_bmi```, prend 2 listes d'entiers ou de flottants en entrée et **renvoie une liste de valeurs d'IMC**.

Votre fonction, ```apply_limit```, accepte comme paramètres une liste d'entiers ou de flottants et un entier représentant une limite comme paramètres. Elle **renvoie une liste de booléens** (True si la limite est dépassée).

- Gérer les cas d'erreur si les listes ne sont pas de la même taille, ne sont pas des int ou des float...

Le prototype des fonctions est :

```python
# Array/ex00/give_bmi.py

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #your code here

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    #your code here
```

Le main():

```python
# Array/ex00/main.py

from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

resultat attendu:

```python
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
$>
```

----------------------------------------------------------------------------

## Exercice 01

### : 2D array

- Turn-in directory : ***ex01/***
- Files to turn in : [array2D.py](/Array/ex01/array2D.py)
- Allowed functions :  ```numpy``` or any lib of table manipulation

Écrire une fonction qui prend en paramètre un **tableau 2D**, print sa forme et renvoie une version tronquée du tableau en fonction des arguments de début et de fin fournis.

- Vous devez utiliser ***la méthode de découpage en tranches***.

- Vous devez gérer les cas d'erreur si les listes ne sont pas de la même taille, ne sont pas une liste ...

Le prototype de la fonctions est :

```python
# Array/ex02/array2D.py

def slice_me(family: list, start: int, end: int) -> list:
    # your code here
```

Le main():

```python
# Array/ex01/main.py
from array2D import slice_me

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

Resultat attendu:

```python
$> python test_array2D.py
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
$>
```

### Notions abordées

- Utilisation de ```numpy```.

- Méthode de découpage en tranches.

```python
# Créer un tableau
original_array = np.array([1, 2, 3])
# Ajouter des éléments à la place
original_array = np.append(original_array, [4, 5, 6])
# Créer un tableau NumPy
arr = np.array([1, 2, 3, 4, 5])
# Supprimer l'élément à l'index 2 (valeur 3)
new_arr = np.delete(arr, 2)
# Créer un tableau NumPy 2D
arr = np.array([[1, 2, 3], [4,5, 6], [7, 8, 9]])
# Supprimer la deuxième ligne (index 1)
new_arr = np.delete(arr, 1, axis=0)
```

- Considerer ```np.size()``` et ```np.shape()```

----------------------------------------------------------------------------

## Exercice 02

### Load my image

- Turn-in directory : ***ex02/***
- Files to turn in : [load_image.py](/Array/ex02/load_image.py)
- Allowed functions : all libs for load images and table manipulation

Ecrire une fonction qui charge une image, imprime son format et ses pixels au format **RGB**.

- Gérer les formats ***JPG*** et ***JPEG***.

- **Gérer toute erreur** avec un message d'erreur clair.

Le prototype de la fonctions est :

```python
# Array/ex02/load_image.py

def ft_load(path: str) -> array: (you can return to the desired format)
  #your code here
```

Le main():

```python
# Array/ex02/main.py

from load_image import ft_load

print(ft_load("landscape.jpg"))
```

Resultat attendu:

```python
$> python tester.py
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
$>
```

### Notions abordées

Nouvelle librairie:

```python
# Permet de travailler sur les images :
from PIL.Image import Image
```

Pour recupérer les valeurs du ***canal rouge (R)***, du ***canal vert (G)*** et du ***canal bleu (B)*** du pixel de coordonnées (100,250).

- Par convention:
  - **r** correspondra à la valeur du canal rouge.
  - **g** correspondra à la valeur du canal vert.
  - **b** correspondra à la valeur du canal bleu.

Exemple:

```python
# Récupere les valeurs d'un pixel à la position x, y :
img.getpixel((190,250)
print("canal rouge : ",r,"canal vert : ",g,"canal bleu : ",b)
```

- sites: https://moncoachdata.com/blog/10-outils-de-traitement-dimages-en-python/
