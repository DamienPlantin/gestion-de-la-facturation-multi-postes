# gestion-de-la-facturation-multi-postes

Auteurs : Damien, Stéphanie, Yanis, Yoan

Ce programme permet d'installer le logiciel mysql qui va interagir avec un script.sql, un script Python. 
Il permettra de gérer une base de donnée client, facture et facture détaillé avec certaines fonctions spécifiques.

Le programme est composé de 4 scripts:

1] Le script.bat:

Il permet de se connecter à la machine distante, la mettre à jour pour pouvoir y faciliter l'accès, on donne ensuite l'autorisation au dossier caché ssh pour
créer le fichier 'authorized_keys' dans le dossier caché ssh. Ceci nous permet de copié le contenu d'un fichier vers un autre fichier dans la machine distante.

2] Le script.sh:

Il permet de mettre à jour le package de la machine virtuelle, de désactiver le mot de passe, installer github et de mettre à jour pip pyhton pour pouvoir
installer mysql -server. 

3]Le script.sql:

Il contient toutes les commandes SQL nécéssaire au script, création de la base de données, des tables, et toutes les fonctionnalité nécéssaire au programme
qui seront listé dans le dernier script.

4]Le Script Python:

C'est lui qui va interagir avec la base de donnée et qui possède toutes les fonctionnalités du programme qui sont:
- Enregistré un/des client(s), une/des ligne(s) ou une/des facture(s)
- Apporter des modifications à une tables ou supprimer une/des lignes dans une table
- Rechercher un client, une facture ou plusieurs factures émise entre deux dates
- Calculer et afficher le montant_total d'une facture ainsi que le total de toutes les factures
- Faire une remise sur le montant total d'une facture






