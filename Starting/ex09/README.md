# ft_package

## Descrition du projet

### Aperçu

ft_package est un package Python simple qui calcule le nombre d'occurrences d'un élément spécifique dans une liste.

### Installation

Pour installer le package, vous pouvez le compiler localement puis utiliser pip :

```bash
pip install ft_package_chanwoong1
```

### Usage

Voici comment utiliser le package :

```bash
from ft_package import count_in_list
```

#### Calculer l'occurrence de « toto » dans la liste

```bash
print(count_in_list(["toto", "tata", "toto"], "toto")) # Output: 2
```

#### Calculer l'occurrence de 'tutu' dans la liste (renvoie 0 car il n'existe pas)

```bash
print(count_in_list(["toto", "tata", "toto"], "tutu")) # Output: 0
```

### Licence

Ce package est distribué sous licence MIT. Pour plus de détails, veuillez vous référer au fichier LICENSE.