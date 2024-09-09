# Démarrage en python

> Created by alex lamizana in 31/07/2024
----------------------------------------------------------------------------

Formation Piscine Python pour la science des données

## Sommaire

1. [Règles générales.](#règles-générales)
2. [Exercice 00: First python script.](#exercice-00)
3. [Exercice 01: First use of package.](#exercice-01)
4. [Exercice 02: First function python.](#exercice-02)
5. [Exercice 03: NULL not found.](#exercice-03)
6. [Exercice 04: The Even and the Odd.](#exercice-04)
7. [Règles supplémentaires.](#règles-supplémentaires)
8. [Exercice 05: First standalone program python.](#exercice-05)




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

### Exercice 00

#### First python script

- Turn-in directory : ***ex00/***
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

----------------------------------------------------------------------------

### Exercice 02

#### First function python

- Turn-in directory : ***ex02/***
- Files to turn in : [find_ft_type.py](/Starting/ex02/find_ft_type.py)
- Allowed functions :  None

Écrire une fonction qui imprime les types d'objets et renvoie 42.
Voici comment il devrait être prototypé :

```python
def all_thing_is_obj(object: any) -> int:
  #your code here

```

Votre fichier tester.py :

```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

```

Résultat attendu :

```python
$> python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

> [!NOTE]
> L'exécution de la fonction seule n'apporte rien

```python
$> python find_ft_type.py | cat -e
$>
```

----------------------------------------------------------------------------

### Exercice 03

#### NULL not found

- Turn-in directory : ***ex03/***
- Files to turn in : [NULL_not_found.py](/Starting/ex03/NULL_not_found.py)
- Allowed functions :  None

L'exécution de votre fonction seule ne fait qu'écrire une fonction qui *imprime le type d'objet* de tous les types de "Null".

- Retournez 0 si tout se passe bien et 1 en cas d'erreur.

- Votre fonction doit imprimer tous les types de NULL.

Voici comment il devrait être prototypé:

```python
def NULL_not_found(object: any) -> int:
  #your code here

```

Votre tester.py:

```python
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ’’
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

```

> Empty = ”

Résultat attendu :

```python
$> python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

> [!NOTE]
> L'exécution de la fonction seule n'apporte rien

```python
$> python NULL_not_found.py | cat -e
$>
```

----------------------------------------------------------------------------

### Exercice 04

#### The Even and the Odd

- Turn-in directory : ***ex04/***
- Files to turn in : [whatis.py](/Starting/ex04/whatis.py)
- Allowed functions :  ```sys``` ou toute autre bibliothèque permettant de recevoir les args

Créez un script qui prend un nombre comme argument, vérifie s'il est pair ou impair, et imprime le résultat.
- Si plus d'un argument est fourni ou si l'argument n'est pas un entier, **imprimer une erreur d'assertion** (```AssertionError```).

Résultat attendu :

```python
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

----------------------------------------------------------------------------

### Règles supplémentaires

> [!NOTE]
> Voici de nouvelles régles à respecter à partir de maintenant.

- Pas de code dans le champ d'application global. **Utilisez des fonctions** !

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

### Exercice 05

#### First standalone program python

- Turn-in directory : ***ex05/***
- Files to turn in : [building.py](/Starting/ex05/building.py)
- Allowed functions :  ```sys``` ou toute autre bibliothèque permettant de recevoir les args.

Cette fois-ci, vous devez créer un véritable programme autonome, avec une fonction principale, qui prend en argument une seule chaîne de caractères et affiche la somme de ses majuscules, minuscules, des caractères de ponctuation, des chiffres et des espaces.

- Si aucune chaine n'est fournit ou si la chaine est vide, l'utilisateur est invité à fournir une chaîne de caractères.

- Si plus d'un argument est fourni au programme, une erreur d'assertion (AssertionError) est affichée.

Résultat attendu :

```python
$> python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

Résultats attendus : (le retour chariot compte comme un espace, si vous ne voulez pas en retourner un, utilisez ctrl + D).

```python
$> python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

----------------------------------------------------------------------------

### Exercice 06


- Turn-in directory : ***ex06/***
- Files to turn in : [ft_filter.py, filterstring.py](/Starting/ex06/ft_filter.py)
- Allowed functions :  ```sys``` ou toute autre bibliothèque permettant de recevoir les args.

#### Part 1: Recoder la fonction 'filter'

Recodez votre propre ft_filter, il doit se comporter comme la fonction intégrée originale (il doit retourner la même chose que « print(filter.__doc__) »).
- Utiliser des compréhensions de listes pour recoder votre ft_filter.

> [!WARNING]
> Bien entendu, il est interdit d'utiliser le filtre original intégré

> [!NOTE]
> Vous pouvez valider le module à partir d'ici, mais nous vous encourageons à continuer car il y a des choses que vous devrez savoir pour la suite.

#### Part 2: Le programme

Créez un programme qui accepte deux arguments : une chaîne de caractères (S) et un nombre entier (N). Le programme doit produire une liste de mots de S dont la longueur est supérieure à N.

- Les mots sont séparés les uns des autres par des caractères d'espacement.

- Les chaînes de caractères ne contiennent pas de caractères spéciaux. (ponctuation ou invisible).

- Le programme doit contenir au moins une expression de compréhension de liste et une expression lambda.

- Si le nombre d'arguments est différent de 2, ou si le type d'un argument est erroné, le programme imprime une AssertionError.

Résultats attendus :

```python
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```python
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```python
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```python
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

----------------------------------------------------------------------------

### Exercice 07

#### Dictionaries SoS

- Turn-in directory : ***ex07/***
- Files to turn in : [sos.py](/Starting/ex07/sos.py)
- Allowed functions :  ```sys``` ou toute autre bibliothèque permettant de recevoir les args.

Réaliser un programme qui prend une chaîne de caractères comme argument et l'encode en ***code morse***.

- Le programme prend en charge les **espaces et les caractères alphanumériques**.

- Un caractère alphanumérique est représenté par des points ```.``` et des tirets ```-```

- Les caractères morse complets sont **séparés par un seul espace**.

- Un espace est représenté par une barre oblique ```/```.

- Vous devez utiliser **un dictionnaire** pour stocker votre code morse.

```python
NESTED_MORSE = {
  " ": "/ ",
  "A": ".- ",
  ...
```

- Si le nombre d'arguments est différent de 1, ou si le type d'un argument est incorrect,
le programme imprime une AssertionError.

```python
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```


----------------------------------------------------------------------------

### Exercice 08

#### Loading ...

- Turn-in directory : ***ex07/***
- Files to turn in : [Loading.py](/Starting/ex08/Loading.py)
- Allowed functions : aucune

Créons donc une fonction appelée **ft_tqdm**.

- La fonction doit copier la fonction **tqdm** avec l'opérateur ```yield```.

Voici comment il devrait être prototypé :

```python
def ft_tqdm(lst: range) -> None:
# your code here
```

Votre **fichier test** : (vous comparez votre version avec l'original)

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
  sleep(0.005)
print()

for elem in tqdm(range(333)):
  sleep(0.005)
print()
```

**Résultat attendu** : (vous devez obtenir une fonction aussi proche que possible de la version originale)
```python
100%|[============================================================>]| 333/333
100%|                                                               | 333/333 [00:01<00:00, 191.61it/s]
```