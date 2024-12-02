# Oriented Object Programming

> Created by alex lamizana in 31/10/2024
----------------------------------------------------------------------------

## Formation Piscine Python pour la science des données - 3

### [Index](/README.md)

- Apprendre à charger, manipuler et afficher des tableaux de données.

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Instructions spécifiques.](#instructions-spécifiques)
3. [Exercice 00: GOT S1E9.](#exercice-00)
4. [Exercice 01: GOT S1E7.](#exercice-01)
5. [Exercice 02: Now it’s weird.](#exercice-02)
6. [Exercice 03: Calculate my vector.](#exercice-03)
7. [Exercice 04: Calculate my dot product.](#exercice-04)

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

### GOT S1E9

- Turn-in directory : ***ex00/***
- Files to turn in : [S1E9.py](/OOP/ex00/S1E9.py)
- Allowed functions : Aucune.

Créer une classe abstraite ***Character***.

- Prend un ```first_name``` comme premier paramètre.
- Prend ```is_alive``` comme second paramètre **non obligatoire fixé à True par défaut** et peut changer l'état de santé du personnage avec une méthode qui fait passer is_alive de True à False.

Créer une classe  ***Stark***  qui hérite de ***Character***.

Le prototype de la Classe est :

```python
# OOP/ex00/S1E9.py
from abc import ABC, abstractmethod

class Character(ABC):
  """Your docstring for Class"""
  @abstractmethod
  #your code here

class Stark(Character):
  """Your docstring for Class"""
  #your code here
```

Le main():

```python
# OOP/ex00/main.py
from S1E9 import Character, Stark

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
```

Résultat attendu (les chaînes de documentation peuvent être différentes):

```bash
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
```

> [!NOTE]
> Assurez-vous que vous avez utilisé une classe abstraite.

```python
from S1E9 import Character
hodor = Character("hodor")
```

```python
TypeError: Can't instantiate abstract class Character with abstract method
$>
```

### Notions abordées

#### Classes abstraite

Pour créer une classe abstraite en Python, on utilise le module ***abc*** (Abstract Base Classes) qui fournit les mécanismes nécessaires pour définir les méthodes abstraites.

> [!NOTE]
> Une méthode devient abstraite quand elle est décorée avec le décorateur ***@abstractmethod***

----------------------------------------------------------------------------

## Exercice 01

### GOT S1E7

- Turn-in directory : ***ex01/***
- Files to turn in : Files from previous exercises + [S1E7.py](/OOP/ex01/S1E7.py)
- Allowed functions : Aucune.

Créer deux familles qui héritent de la classe Character, que nous pouvons instancier sans passer par la classe Character.

- Trouver une solution pour que  ```__str__``` et ```__repr__``` renvoient des chaînes de caractères et non des objets.

- Ecrire une méthode Class pour créer des caractères dans une chaîne.

Le prototype de la Classe est :

```python
# OOP/ex01/S1E7.py
from S1E9 import Character

class Baratheon(Character):
  #your code here


class Lannister(Character):
  #your code here
  # decorator

  def create_lannister(your code here):
  #your code here
```

Le main():

```python
# OOP/ex01/main.py
from S1E7 import Baratheon, Lannister

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
```

Résultat attendu (les chaînes de documentation peuvent être différentes):

```bash
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>
```

----------------------------------------------------------------------------

## Exercice 02

### Now it’s weird

- Turn-in directory : ***ex02/***
- Files to turn in : Files from previous exercises + [DiamondTrap.py](/OOP/ex02/DiamondTrap.py)
- Allowed functions : Aucune.

Dans cet exercice, vous allez créer un monstre : Joffrey Baratheon.
**C'est très risqué !**

Il y a quelque chose d'incohérent avec ce nouveau « faux » roi:

- Vous devez utiliser les propriétés pour modifier les caractéristiques physiques de notre nouveau roi.

> [!NOTE]
> Depuis python 2.3, le langage utilise la linéarisation C3 pour contrer le problème de l'héritage dans diamand.

Le prototype de la Classe est :

```python
# OOP/ex02/DiamondTrap.py
from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
  #your code here
```

Le main():

```python
# OOP/ex02/main.py
from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
```

Résultat attendu (les chaînes de documentation peuvent être différentes):

```bash
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
```

----------------------------------------------------------------------------

## Exercice 03

### Calculate my vector

- Turn-in directory : ***ex03/***
- Files to turn in : [ft_calculator.py](/OOP/ex03/ft_calculator.py)
- Allowed functions : Aucune.

Ecrire une classe de calculatrice capable d'effectuer des calculs (addition, multiplication, sous- traction, division) sur un vecteur avec un scalaire.

Le prototype de la Classe est :

```python
# OOP/ex03/ft_calculator.py
class calculator:
  #your code here
  def __add__(self, object) -> None:
    #your code here

  def __mul__(self, object) -> None:
    #your code here

  def __sub__(self, object) -> None:
    #your code here

  def __truediv__(self, object) -> None:
  #your code here
```

Le main():

```python
# OOP/ex03/ft_calculator.py
from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
Print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
Print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
```

Résultat attendu (les chaînes de documentation peuvent être différentes):

```bash
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
```

> [!NOTE]
> Vous ne devez pas gérer les erreurs, sauf pour la division par 0.

----------------------------------------------------------------------------

## Exercice 04

### Calculate my dot product

- Turn-in directory : ***ex04/***
- Files to turn in : [ft_calculator.py](/OOP/ex04/ft_calculator.py)
- Allowed functions : Aucune.

Ecrire une classe de calculatrice capable d'effectuer des calculs (produit en points, addition, soustraction) **de 2 vecteurs**.

- Les vecteurs auront toujours des tailles identiques, pas de gestion des erreurs.

- C'est à vous de trouver un décorateur qui vous permettra d'utiliser les méthodes de la classe calculatrice sans instancier cette classe.

Le prototype de la Classe est :

```python
# OOP/ex04/ft_calculator.py

class calculator:
  #your code here
  
  # decorator
  def dotproduct(V1: list[float], V2: list[float]) -> None:
    #your code here

  # decorator
  def add_vec(V1: list[float], V2: list[float]) -> None:
    #your code here

  # decorator
  def sous_vec(V1: list[float], V2: list[float]) -> None:
    #your code here
```

Le main():

```python
# OOP/ex04/ft_calculator.py
from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
```

Résultat attendu (les chaînes de documentation peuvent être différentes):

```bash
$> python tester.py
Dot product is: 56
Add Vector is : [7.0, 14.0, 5.0]
Sous Vector is: [3.0, 6.0, -1.0]
$>
```

> [!NOTE]
> Vous ne devez pas gérer les erreurs.

Si on souhaite aller plus loin dans les calculs vectoriels ou matriciels, consulter le ***projet matrix*** après cette « piscine ».
