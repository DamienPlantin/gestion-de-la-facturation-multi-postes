import mysql.connector
import argparse
import sys


# logger = logging.getLogger('Transport')
# logger.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()
# ch = logging.FileHandler('Log.txt', encoding='utf-8')
# ch.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
# ch.setFormatter(formatter)
# logger.addHandler(ch)

# sudo apt update
# sudo apt install mysql-server
# sudo mysql_secure_installation

# sudo mysql
# test_user@localhost:~$ su 
# SET PASSWORD FOR root@localhost=PASSWORD('azerty');
# root@localhost:~ mysql -u root -p
# # mysql> CREATE DATABASE testing
# # mysql> GRANT ALL PRIVILEGES ON testing.* TO test_user@localhost IDENTIFIED BY 'test_pass'

parser = argparse.ArgumentParser("Script to interact with data from the Facturation")

parser.add_argument("-ac", "--ajouter_client", nargs="*", help="Ajouter un client avec les infos nécéssaires")
parser.add_argument("-af", "--ajouter_facture", nargs="*", help="Ajouter une facture à la base de donnee")
parser.add_argument("-m", "--modifier_client", help="Modifier les infos du client")
parser.add_argument("-r", "--rechercher_client", nargs="*", help="Rechercher un client avec son nom ou son e-mail")
parser.add_argument("-f", "--rechercher_facture", help="rechercher une facture avec son numero")
parser.add_argument("-fs", "--factures", nargs="*", help="afficher toutes les factures entre deux dates")
parser.add_argument("-s", "--suprimmer", nargs="*", help="Suprimmer des informations de la base de donnée")

args = parser.parse_args()
conn = mysql.connect("Facture2.db")
cursor = conn.cursor()
# conn.close()


addc = args.ajouter_client
addf = args.ajouter_facture
modc = args.modifier_client
rechc = args.rechercher_client 
rechf = args.rechercher_facture 
affs = args.factures
sup = args.suprimmer

# def add_user():             
#     #Créé un utilisateur 
#     cursor.execute('CREATE USER 'buzut'@'localhost' IDENTIFIED BY 'XXXX'');
# def user_connect():
#     cursor.execute('SELECT user, host, plugin, authentication_string FROM mysql.user)

def add_client():
    #Ajouter les informations d'un client
    
    cursor.execute('INSERT INTO gestion_client (TYPE_DE_CLIENT, RAISON_SOCIALE, EMAIL, TELEPHONE, ADRESSE ) VALUES (?,?,?,?,?)', (addc[0],addc[1], addc[2], addc[3], addc[4]))

def add_facture():
    #Ajouter une facture à la bdd

    cursor.execute('INSERT INTO gestion_facture (NOM_DU_PRODUIT, REFERENCE, QUANTITE, PRIX_UNITE, N_FACTURE, CLIENT,DATE_EMISSION,MONTANT_TOTAL ) VALUES (?,?,?,?,?,?,?,?)', (addf[0],addf[1],addf[2],addf[3], addf[4], addf[5],addf[6],addf[7]))
    cursor.execute("""SELECT DATE_FORMAT({addf[6]}, '%Y %c %e')""")

def rech_factures():
    # rechercher une facture avec le numéro dans la bdd

    cursor.execute('SELECT N_FACTURE FROM gestion_facture', (rechf))

def rech_client(): 
    #rechercher un client avec son nom et/ou son mail

    cursor.execute('SELECT ? AND ? FROM gestion_client', (rechc[0], rechc[1]))

def modif_client():
    #Modifier les infos d'un client
    cursor.execute('UDPDATE gestion_client SET ? = ? WHERE ?', (modc[0], modc[1], modc[3]))

def date():
    #Ajouter une date à la facturation
    
    cursor.execute("SELECT * FROM gestion_facture WHERE DATE_EMISSION BETWEEN '?' AND '?' ", (affs[0],affs[1]))
    for i in cursor.fetchall():
        factures = (f'NOM_DU_PRODUIT{i[0]} REFERENCE{i[1]} QUANTITE{i[2]} PRIX_UNITE{[3]} N_FACTURE{i[4]} CLIENT{i[5]} DATE_EMISSION{i[6]} MONTANT_TOTAL{i[7]}')
        print(factures)

def main():

    cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion_client" (
    "TYPE_DE_CLIENT" TEXT,
    "RAISON_SOCIALE" TEXT,
    "EMAIL" TEXT,
    "TELEPHONE" INTEGER,
    "ADRESSE" INTEGER
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion_facture" (
    "NOM_DU_PRODUIT" TEXT,
    "REFERENCE" INTEGER,
    "QUANTITE" INTEGER,
    "PRIX_UNITE" INTEGER,

    "N_FACTURE" TEXT,
    "CLIENT" TEXT,
    "DATE_EMISSION"	INTEGER,
    "MONTANT_TOTAL" INTEGER
    );""")

    if addc:
        add_client()
    if addf:
        add_facture()
    conn.commit()
    if affs:
        date()
    if rechf:
        rech_facture()
    if rechc:
        recherche_client()
    conn.commit()






if __name__ == "__main__":
    sys.exit(main())