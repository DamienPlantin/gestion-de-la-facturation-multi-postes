::echo off affiche seulement la sortie de la commande
@echo off
::Permet d'afficher les accents
chcp 65001 > nul

::-------------------------------------------------------------------------------------------------------------------
:: INFORMATION IMPORTANTES
::-------------------------------------------------------------------------------------------------------------------

echo AVANT DE LANCER LE RESTE DU SCRIPT, PENSER A CHANGER L'@IP DU BIND ADDRESS DANS LE SCRIPT POST-INSTALL_V2.SH 
pause
echo.
echo AVANT DE LANCER LE RESTE DU SCRIPT, PENSER A MODIFIER LE USER DANS SCRIPT_MYSQL.SQL AVEC VOTRE NOM ET L'@IP DE VOTRE MACHINE WINDOWS
pause
::-------------------------------------------------------------------------------------------------------------------
:: INSTALLATION MYSQL-CONNECTOR PYTHON
::-------------------------------------------------------------------------------------------------------------------

::Installation de la mise a jour de pip
python -m pip install --upgrade pip
::Installation de la librairie mysql.connector
pip install mysql-connector-python

::-------------------------------------------------------------------------------------------------------------------
:: INFORMATION DE CONNEXION
::-------------------------------------------------------------------------------------------------------------------

::set /p attend une saisie de l'utilisateur pour passer à la suite
::Ici on demande le nom du login sur la machine distante
set /p login=Nom de la session distante : 
::Ici on demande l'adresse ip de la machine distante
set /p ip=@Ip distante :

::-------------------------------------------------------------------------------------------------------------------
:: COPIE DES CLES PUBLICS/PRIVEES SUR LA MACHINE DISTANTE
::-------------------------------------------------------------------------------------------------------------------

::On se connecte sur la machine distante, on créer le dossier caché ssh et on se déconnecte
ssh %login%@%ip% "mkdir ~/.ssh"
echo On as créer le dossier .ssh dans la machine distante
::Ici on demande le chemin d'accès du fichier à copier
set /p path_key=Chemin d'acces de la cle a copier : 
::scp permet de copier le contenu d'un fichier vers un autre fichier dans la machine distante
scp %path_key% %login%@%ip%:.ssh/authorized_keys
echo Copie de la clé windows dans le fichier authorized_keys sur la machine distante
pause
::-------------------------------------------------------------------------------------------------------------------
:: COPIE DU SCRIPT .SH SUR LA MACHINE DISTANTE
::-------------------------------------------------------------------------------------------------------------------

::Ici on demande le chemin d'accès du script à copier dans la VM
set /p path_script_sh=Chemin d'acces du script .sh a copier : 
::Ici on demande le nom que prendre le fichier script dans la VM (sans oublier le .sh a la fin)
set /p name_script_sh=Nom du script .sh pour la VM ? 
::Ici on copie le contenu du script vers un autre fichier dans la machine distante
scp %path_script_sh% %login%@%ip%:/home/%login%/%name_script_sh%
echo Script %name_script_sh% copié sur la machine distante
:: On rend le script executable
ssh %login%@%ip% "chmod +x %name_script_sh%"
echo %name_script_sh% rendu exécutable
:: On retire les mauvais caractère "made in windows" du script que Linux ne comprend pas
ssh %login%@%ip% "sed -i -e 's/\r$//' %name_script_sh%"
echo \r supprimé de %name_script_sh%
pause
::-------------------------------------------------------------------------------------------------------------------
:: COPIE DU SCRIPT .SQL SUR LA MACHINE DISTANTE
::-------------------------------------------------------------------------------------------------------------------

:Ici on demande le chemin d'accès du script à copier dans la VM
set /p path_script_sql=Chemin d'acces du script .sql a copier : 
::Ici on demande le nom que prendre le fichier script dans la VM (sans oublier le .sh a la fin)
set /p name_script_sql=Nom du script .sh pour la VM ? 
::Ici on copie le contenu du script vers un autre fichier dans la machine distante
scp %path_script_sql% %login%@%ip%:/home/%login%/%name_script_sql%
echo Script %name_script_sql% copié sur la machine distante
:: On rend le script executable
ssh %login%@%ip% "chmod +x %name_script_sql%"
echo %name_script_sql% rendu exécutable
:: On retire les mauvais caractère "made in windows" du script que Linux ne comprend pas
ssh %login%@%ip% "sed -i -e 's/\r$//' %name_script_sql%"
echo \r supprimé de %name_script_sql%
pause
::-------------------------------------------------------------------------------------------------------------------
:: COPIE DU FICHIER .TXT POUR LA CONF DE MYSQL_SECURE SUR LA MACHINE DISTANTE
::-------------------------------------------------------------------------------------------------------------------

::Ici on demande le chemin d'accès du script à copier dans la VM
set /p path_script_txt=Chemin d'acces du fichier .txt pour la conf de mysql_secure a copier : 
::Ici on demande le nom que prendre le fichier script dans la VM (sans oublier le .sh a la fin)
set /p name_script_txt=Nom du fichier .txt pour la VM ? 
::Ici on copie le contenu du script vers un autre fichier dans la machine distante
scp %path_script_txt% %login%@%ip%:/home/%login%/%name_script_txt%
echo Fichier de conf %name_script_txt% copié sur la machine distante
:: On retire les mauvais caractère "made in windows" du script que Linux ne comprend pas
ssh %login%@%ip% "sed -i -e 's/\r$//' %name_script_txt%"
echo \r supprimé de %name_script_txt%
pause
::-------------------------------------------------------------------------------------------------------------------
:: EXECUTION DE SCRIPT SUR LA MACHINE DISTANTE
::-------------------------------------------------------------------------------------------------------------------

::Exécution du script
ssh -t %login%@%ip% "sudo ./%name_script_sh%"
echo ///installation des dernière MaJ, ainsi que d'autres option terminées\\\
pause

ssh %login%@%ip%

exit /b