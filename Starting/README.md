# Démarrage en python

> Created by alex lamizana in 3/07/2024
----------------------------------------------------------------------------

Formation Piscine Python pour la science des données

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Exercice 00: First python script.](#exercice-00)
3. [Exercice 01: First use of package.](#exercice-01)

----------------------------------------------------------------------------

### Règles générales

- Vous devez effectuer le rendu de vos modules à partir d'un ordinateur du cluster, soit en utilisant une
machine virtuelle :
  - Vous pouvez choisir le système d'exploitation à utiliser pour votre machine virtuelle
  - Votre machine virtuelle doit disposer de tous les logiciels nécessaires à la réalisation de votre projet.
  - Ces logiciels doivent être configurés et installés.

- Vous pouvez également utiliser l'ordinateur directement si les outils sont disponibles.
  - Assurez-vous d'avoir l'espace nécessaire sur votre session pour installer ce dont vous avez besoin pour tous les modules (utilisez le goinfre si votre campus en dispose).
  - Vous devez avoir tout installé avant les évaluations.

- Vos fonctions ne doivent pas se terminer de manière inattendue (erreur de segmentation, erreur de bus, double libération, etc.)

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

### Exercice 00

#### First python script

- Turn-in directory : *ex00/*
- Files to turn in : [Hello.py](/Starting/ex00/Hello.py)
- Allowed functions : None

Vous devez modifier la chaîne de caractères de chaque objet de données pour afficher les messages d'accueil suivants :

- "Hello World"
- "Hello «country of your campus»"
- "Hello «city of your campus»"
- "Hello «name of your campus»"

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Résultat attendu :

```python
$> python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

#### Notions utilisées

- listes.
- tuples.
- set.
- dictionnaire.

----------------------------------------------------------------------------

### Exercice 01

#### First use of package

- Turn-in directory : *ex01/*
- Files to turn in : [format_ft_time.py](/Starting/ex01/format_ft_time.py)
- Allowed functions :  time, datetime or any other library that allows to receive the date

Ecrire un script qui formate les dates de cette façon, bien sûr votre date ne sera pas la mienne comme dans l'exemple mais elle doit être formatée de la même façon.

Résultat attendu :

```python
$> python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```
