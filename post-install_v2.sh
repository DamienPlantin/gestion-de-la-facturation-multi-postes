#!/bin/bash

echo "[[[PASSWORD SUDO DISABLE]]]"
sudo sed -i "s/%sudo ALL=(ALL) ALL/%admin ALL=(ALL) NOPASSWD:ALL/" /etc/ssh/sshd_config
#Désactive le mot de passe sudo le temps de l'installation

#La commande echo permet d'afficher un commentaire
#La commande timedateectl permet de changer de fuseau horaire au niveau du serveur
echo "[[[Time zone change for Paris]]]"
sudo timedatectl set-timezone Europe/Paris
echo
echo "[[[UBUNTU POST-INSTALL SCRIPT]]]"
echo "[[[Updating APT...]]]"
sudo apt-get -y update
sudo apt-get -y upgrade
#La commande sudo permet d'exécuter la commande en super-utilisateur
#La commande apt-get permet d'effectuer l'installation et la désinstallation de paquets en provenance d'un dépôt APT.
#Update permet de mettre à jour la commande placer juste avant

echo "[[[Password desactivation]]]"
sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/" /etc/ssh/sshd_config
#Désactive l'authentification ssh par mot de passe
sudo /etc/init.d/ssh restart
#Relance le servcie ssh pour appliquer les modifications
echo "[[[Installing base packages]]]"
sudo apt-get install --yes git git-extras build-essential python3-pip
sudo myvenv/bin/pip install --upgrade pip
#install permet d'installer les applications ou paquets demandés juste après
#--yes permet de répondre yes si des questions sont demandées

echo "[[[INSTALLATION MYSQL-SERVER AND SERVICE]]]"
sudo apt-get install mysql-server -y
#Installation de MySQL
cat mysql_config.txt | sudo -S mysql_secure_installation
#Configure le mysql_secure

echo "[[[UPLOAD SCRIPT .SQL]]]"
sudo mysql < ./Script_mysql.sql
#Applique le script.sql pour la création de la BdD

echo "Updating mysql configs in /etc/mysql/mysql.conf.d/mysqld.cnf."
sudo sed -i 's/^bind-address.*/bind-address = 192.168.1.21/' /etc/mysql/mysql.conf.d/mysqld.cnf
#Pour le bind-address, mettre l'@IP de VOTRE MACHINE VIRTUELLE
echo "Updated mysql bind address in /etc/mysql/mysql.conf.d/mysqld.cnf to 0.0.0.0 to allow external connections."
#Applique une adresse ip au service mysql pour communiquer
sudo systemctl restart mysql
#redémarre le service mysql

echo "[[[PASSWORD SUDO ENABLE]]]"
sudo sed -i "s/%sudo ALL=(ALL) NOPASSWD:ALL/%admin ALL=(ALL) ALL/" /etc/ssh/sshd_config
#Remet le mot de passe sudo à la fin de l'installation
exit

