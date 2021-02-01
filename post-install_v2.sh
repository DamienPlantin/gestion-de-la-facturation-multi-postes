#!/bin/bash

#La commande echo permet d'afficher un commentaire
#La commande timedateectl permet de changer de fuseau horaire au niveau du serveur
echo "Time zone change for Paris"
sudo timedatectl set-timezone Europe/Paris

echo "UBUNTU POST-INSTALL SCRIPT"
echo "Updating APT..."
sudo apt-get -y update
sudo apt-get -y upgrade
#La commande sudo permet d'exécuter la commande en super-utilisateur
#La commande apt-get permet d'effectuer l'installation et la désinstallation de paquets en provenance d'un dépôt APT.
#Update permet de mettre à jour la commande placer juste avant

echo "Password desactivation"

sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
#Désactive l'authentification ssh par mot de passe
sudo /etc/init.d/ssh restart
#Relance le servcie ssh pour appliquer les modifications
echo "Installing base packages"
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances
#install permet d'installer les applications ou paquets demandés juste après
#--yes permet de répondre yes si des questions sont demandées

pip install -U pip 
sudo apt update
sudo apt install -y mysql-server
sudo mysql_secure_installation

sudo mysql
test_user@localhost:~ yoyo
SET PASSWORD FOR root@localhost=PASSWORD('')
root@localhost:~ mysql -u root -p
mysql> CREATE DATABASE testing
mysql> GRANT ALL PRIVILEGES ON testing.* TO test_user@localhost IDENTIFIED BY 'test_pass'
#Installation de MySQL

exit