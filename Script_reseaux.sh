#!/bin/bash


conn = sqlite3.connect(args.db_path)
c = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion de la facturation " (
    "Factures"	TEXT,
    "nom du "produit", TEXT
    "référence" produit ("SKU"), INTEGER
    "quantité" INTEGER
    "prix à l'unité" INTEGER

    "Numero de la facture"	TEXT,
    "CLIENT" TEXT
    "DATE D'EMISSION"	INTEGER,
    "MONTANT TOTAL
   
    );""")


echo "UNBUTU POST-INSTALL SCRIPT"

sudo timedalect1 set timezone Europe/Paris

echo "Update APT..."
sudo apt-get update -y


echo "Installing bases packages"

sudo apt-get install --yes git-extras python3-pip

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation


~/.ssh/authorized_keys du serveur
	
# Le port SSH par défaut est 22
ssh-copy-id -i ~/.ssh/informatix.pub "<utilisateur>@<hote> -p <port>"
 
# ou si ça ne fonctionne pas
 
cat ~/.ssh/informatix.pub | ssh <utilisateur>@<hote> 'cat >> ~/.ssh/authorized_keys'


