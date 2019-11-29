# SMA

SMA est un ensemble de simulations centrées individus réalisé dans le cadre du cours **Simulation Centrée Individus (SCI)** du Master 2 MoCAD (Modèles Complexes Algorithmes et Données) de l'Université de Lille.

Deux simulations différentes sont disponibles, **particules** et **wator**.

Le projet est écrit en Python.

## Installation
Ce projet a une dépendance pour PyGame uniquement.
Elle peut-être installée via pip:

```bash
pip install pygame
```

Ou en utilisant le makefile fourni (à noter: le makefile lance une installation en mode utilisateur):

```bash
make install
```

## Utilisation
Le programme fonctionne avec un système d'options pour choisir la simulation à charger.

Pour charger la simulation particules, exécutez la commande:
```bash
python3 SMA.py particles
```

Pour le Wa-Tor:
```bash
python3 SMA.py wator
```

En cas de doute sur l'utilisation du programme, l'option ```-h``` affichera l'aide:
```bash
python3 SMA.py -h
```
