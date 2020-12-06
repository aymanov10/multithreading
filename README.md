# Multithreading

Objectif :
Le but est de simuler le fonctionnement d’une machine multi-processeur capable d’évaluer des expressions Python.


# Partie I : version mono-tâche

Dans cette partie, les évaluations se font séquentiellement.
## Question 1

Réaliser ce simulateur dans lequel les instructions à évaluer et les résultats des évaluations sont stockées dans une structure de données en mémoire. Le programme choisit une expression à évaluer dans la file, l’évalue, lui associe le résultat, et recommence. Le programme n’affiche rien pendant sa boucle d’évaluation. Les résultats sont affichés (et associés aux expressions dont ils sont issus) seulement en fin de programme, quand toutes les évaluations ont été réalisées.
## Question 2

Créer un fichier de données externe contenant les expressions à évaluer. Modifier la version précédente de façon à ce que les expressions soient lues depuis le fichier dont le nom est fourni sur la ligne de commande.
## Question 3

Modifier la version précédente de façon à ce qu’une exception issue d’une évaluation n’arrête pas le programme. La nature de l’exception sera associée à l’expression l’ayant déclenchée (par exemple à la place du résultat attendu).
# Partie II : version multi-thread

On souhaite maintenant que la machine à modéliser soit multi-processeurs, chacun des processeurs étant capables d’évaluer une expression Python.
## Question 1

A l’aide du module threading, modéliser cette machine en implémentant chaque processeur comme un thread. Le nombre de processeurs n est récupéré en argument depuis la ligne de commande.

Les instructions à évaluer, stockées au départ dans un fichier, sont chargées dans une structure de données partagée par tous les processeurs. Au début, celle-ci ne contient que des expressions sans résultat. Chaque processeur choisit une expression à évaluer, l’évalue, lui associe le résultat obtenu, et recommence. Au fil du temps, le nombre d’expressions sans valeur dans la file diminue. Une tâche s’arrête lorsqu’elle ne trouve plus d’expression à évaluer. Lorsque toutes les tâches ont terminé, le programme affiche les évaluations.
	
## Question 2

En plus du résultat de l’évaluation, on souhaite savoir en fin de programme :

    quel processeur a évalué chaque expression

    l’ordre d’obtention des résultats

Faire varier n ainsi que la complexité des expressions à évaluer, et observer le comportement de la machine.

