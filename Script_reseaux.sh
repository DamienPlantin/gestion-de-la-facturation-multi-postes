#!/bin/bash

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

sudo mysql
SET PASSWORD FOR root@localhost=PASSWORD('azerty');
GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY 'xxxxxx' WITH GRANT OPTION;

CREATE DATABASE gestion_de_la_facturation;
import mySQLite3
conn = mysql.connector.connect(host="192.168.60.18",
                               user="shadowleader", password="what-else?", 
                               database="magasin")
cursor = conn.cursor()
# Opérations à réaliser sur la base ...
conn.close()

cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion de la facturation " (
    "Factures"	TEXT,
    "nom du produit" TEXT,
    "référence" produit ("SKU"), INTEGER,
    "quantité" INTEGER,
    "prix à l'unité" INTEGER

    "Numero de la facture"	TEXT,
    "CLIENT" TEXT,
    "DATE D'EMISSION"	INTEGER,
    "MONTANT TOTAL" INTEGRER,
   
    );""")


echo "UNBUTU POST-INSTALL SCRIPT"

sudo timedalect1 set timezone Europe/Paris

echo "Update APT..."
sudo apt-get update -y


echo "Installing bases packages"

sudo apt-get install --yes git-extras python3-pip


/.ssh/authorized_keys du serveur
	
# Le port SSH par défaut est 22
ssh-copy-id -i ~/.ssh/informatix.pub "<utilisateur>@<hote> -p <port>"
 
# ou si ça ne fonctionne pas
 
cat ~/.ssh/informatix.pub | ssh <utilisateur>@<hote> 'cat >> ~/.ssh/authorized_keys'


