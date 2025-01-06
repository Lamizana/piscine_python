# Oriented Object Programming

> Created by alex lamizana in 31/10/2024
----------------------------------------------------------------------------

## Formation Piscine Python pour la science des données - 4

### [Index](/README.md)

- Structure Design and **Data Oriented Design**

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Instructions spécifiques.](#instructions-spécifiques)
3. [Exercice 00: Calculate my statistics.](#exercice-00)
4. [Exercice 01: Outer_inner.](#exercice-01)
5. [Exercice 02: My first decorating.](#exercice-02)
5. [Exercice 03: Data class.](#exercice-03)

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

Une plainte fréquente des data scientists est qu'ils écrivent du shitcode (en passant, uniquement à des fins éducatives, vous pouvez trouver de nombreux exemples de shitcode Python ici).

Pourquoi ? Parce que le data scientist moyen utilise beaucoup de techniques inefficaces et de variables codées en dur et néglige la programmation orientée objet.
Ne soyez pas comme eux.

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

### Calculate my statistics

- Turn-in directory : ***ex00/***
- Files to turn in : [statistics.py](/Dot/ex00/statistics.py)
- Allowed functions : Aucune.

Vous devez prendre dans *args une quantité de nombre inconnu.

- Faire la Moyenne, la Médiane, Quartile (25% et 75%), Ecart-type et Variance **selon les **kwargs demandées.**

- Il faut gérer les erreurs.

Le prototype de la Classe est :

```python
# Dot/ex00/statistics.py

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    #your code here
```

Le main():

```python
# Dot/ex00/main.py
from statistics import ft_statistics

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

Résultat attendu :

```bash
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
$>
```

### Notions abordées

Gestion de plusieurs argument ```*args``` et ```**kwargs```.

----------------------------------------------------------------------------

## Exercice 01

### Outer_inner

- Turn-in directory : ***ex01/***
- Files to turn in : [in_out.py](/Dot/ex01/in_out.py)
- Allowed functions : Aucune.

Ecrire des fonctions mathemathiques.

- Ecrire une fonction ***square*** qui renvoie le carré de l'argument.
- Une fonction ***pow*** qui renvoie l'exponentiation de l'argument par lui-même.
- Une fonction ***outer*** une fonction qui prend comme argument un nombre
et une fonction , elle renvoie un objet qui, lorsqu'il est appelé, renvoie le résultat du calcul des arguments.

Le prototype des fonctions :

```python
# Dot/ex01/in_out.py

def square(x: int | float) -> int | float:
  #your code here

def pow(x: int | float) -> int | float:
  #your code here

def outer(x: int | float, function) -> object:
  count = 0
  def inner() -> float:
    #your code here
```

Le main():

```python
# Dot/ex01/main.py
from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```

Résultat attendu :

```bash
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
$>
```

> [!IMPORTANT]
> L'utilisation de global est interdite !

----------------------------------------------------------------------------

## Exercice 02

### My first decorating

- Turn-in directory : ***ex02/***
- Files to turn in : [callLimit.py](/Dot/ex02/callLimit.py)
- Allowed functions : Aucune.

Écrire une fonction qui prend comme argument une limite d'appel d'une autre fonction et qui bloque son exécution au-delà d'une limite.

Le prototype des fonctions :

```python
# Dot/ex02/callLimit.py

def callLimit(limit: int):
    """ """
    count = 0

    def callLimiter(function):
        """ """

        def limit_function(*args: any, **kwds: any):
            """ """

            
            #your code here
```

Le main():

```python
# Dot/ex02/main.py
from callLimit import callLimit

@callLimit(3)
def f():
  print ("f()")

@callLimit(1)
def g():
    print ("g()")
            
for i in range(3):
        f()
        g()
```

Résultat attendu :

```bash
$> python main.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

----------------------------------------------------------------------------

## Exercice 03

### Data class

- Turn-in directory : ***ex03/***
- Files to turn in : [new_student.py](/Dot/ex03/new_student.py)
- Allowed functions : dataclasses, random, string.

Écrire une classe de données qui prend comme arguments un nom et un surnom, et attribuez la valeur True à la classe active, crée le login de l'étudiant et génère un identifiant aléatoire avec la fonction generate_id.

- Vous ne devez pas utiliser ```__str__``` , ```__repr__``` dans votre classe.

Le prototype de la fonctions et de la classe :

```python
# Dot/ex03/new_student.py
import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
  return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
  #your code here
```

Le main():

```python
# Dot/ex03/main.py
from new_student import Student

student = Student(name = "Edward", surname = "agle")
print(student)
```

Résultat attendu (**id aleatoire**):

```bash
$> python main.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='trannxhndgtolvh')
$>
```

> [!IMPORTANT]
> Le login et l'id ne doivent pas être initialisables et doivent renvoyer une erreur.

Le main():

```python
# Dot/ex03/main.py
from new_student import Student

student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
```

Résultat attendu :

```bash
$> python main.py
...
TypeError: Student.__init__() got an unexpected keyword argument 'id'
$>
```
