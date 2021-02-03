import argparse
import sys
import mysql.connector



# logger = logging.getLogger('Date')
# logger.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()
# ch = logging.FileHandler('Log.txt', encoding='utf-8')
# ch.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
# ch.setFormatter(formatter)
# logger.addHandler(ch)



parser = argparse.ArgumentParser("Script to interact with data from the Facturation")

parser.add_argument("-au", "--ajouter_user", help="ajouter un utilisateur à mysql")
parser.add_argument("-ac", "--ajouter_client", nargs="*", help="Ajouter un client avec les infos nécéssaires")
parser.add_argument("-af", "--ajouter_facture", nargs="*", help="Ajouter une facture à la base de donnee")
# parser.add_argument("-al", "--ajouter_ligne", nargs="*", "ajouter la facture du produit detaille")
parser.add_argument("-m", "--modifier_client", help="Modifier les infos du client")
parser.add_argument("-r", "--rechercher_client", nargs="*", help="Rechercher un client avec son nom ou son e-mail")
parser.add_argument("-f", "--rechercher_facture", help="rechercher une facture avec son numero")
parser.add_argument("-fs", "--factures", nargs="*", help="afficher toutes les factures entre deux dates")
parser.add_argument("-s", "--supprimer", nargs="*", help="Suprimmer des informations de la base de donnée")
# parser.add_argument("-r", "--remise", help="Modifier le montant total avec une remise")
args = parser.parse_args()

# conn = mysql.connector.connect(host="localhost", user = "root", password = "",database = "GESTION")

# conn.close()

addu = args.ajouter_user
addc = args.ajouter_client
# addl = args.ajouter_ligne
addf = args.ajouter_facture
modc = args.modifier_client
rechc = args.rechercher_client 
rechf = args.rechercher_facture 
betf = args.factures
supp = args.supprimer
# remi = args.remise
# supp = args.suprimmer

conn = mysql.connector.connect(host='192.168.239.195', database='Gestion', user='employer', password='AzErTy123*')
cursor = conn.cursor()

# def add_user():             
#     #Créé un utilisateur 
#     cursor.execute("""CREATE USER '?' IDENTIFIED WITH mysql_native_password""", (addu))
# def user_connect():
#      cursor.execute('SELECT user, host, plugin, authentication_string FROM mysql.user)

def add_client():
    #Ajouter les informations d'un client

    cursor.execute('INSERT INTO Clients (TYPE_DE_CLIENT, RAISON_SOCIALE, EMAIL, TELEPHONE, ADRESSE, CODE_POSTAL, VILLE ) VALUES (?,?,?,?,?,?,?)', (addc[0],addc[1], addc[2], addc[3], addc[4], addc[5], addc[6]))

def add_ligne():
    #Ajouter une ligne facture à la bdd

    cursor.execute('INSERT INTO Lignes (N_FACTURE, CLIENT,DATE_EMISSION) VALUES (?,?,?)', (addl[0], addl[1], addl[2]))

def add_facture():
    #Ajouter une facture détaille à la bdd

    cursor.execute('INSERT INTO Factures (NOM_DU_PRODUIT, REFERENCE, QUANTITE, PRIX_UNITE) VALUES (?,?,?,?)', (addf[0],addf[1],addf[2],addf[3]))

def rech_facture():
    # rechercher une facture avec le numéro dans la bdd

    cursor.execute("""SELECT N_FACTURE FROM Lignes WHERE '?' """, (rechf))

def rech_client(): 
    #rechercher un client avec son nom et/ou son mail

    cursor.execute("""SELECT RAISON_SOCIAL AND EMAIL FROM Clients WHERE '?' AND '?' """, (rechc[0], rechc[1]))

def modif_client():
    #Modifier les infos d'un client

    cursor.execute("""UDPDATE Clients SET '?' = '?' WHERE '?' """, (modc[0], modc[1], modc[3]))

def between_date():
    #Ajouter une date à la facturation

    cursor.execute("""SELECT * Factures WHERE DATE_EMISSION BETWEEN '?' AND '?' """, (betf[0],betf[1]))
    for i in cursor.fetchall():
        factures = (f'NOM_DU_PRODUIT{i[0]} REFERENCE{i[1]} QUANTITE{i[2]} PRIX_UNITE{[3]} N_FACTURE{i[4]} CLIENT{i[5]} DATE_EMISSION{i[6]} MONTANT_TOTAL{i[7]}')
        print(factures)

# def montant_total():
#     Total = []
#     if addl:
#         result = QUANTITE*PRIX_UNITE
#         Total.append(result)

#     cursor.execute("""  """)

def remise():
    #Ajouter une remise pour la déduire sur le prix
    remise = (remi)*100/result

def supprimer():
    #Supprimer une ligne dans la bdd
    cursor.execute("""DELETE FROM '?' WHERE '?'""", (supp[0], supp[1]))
    

def main():
    #Création de la db, des tables de gestion client et facture
    
    # cursor.execute("""CREATE DATABASE GESTION""")
    # #Créé un utilisateur 
    # cursor.execute("""CREATE USER '?' IDENTIFIED WITH mysql_native_password""", (addu))
    conn = mysql.connector.connect(host='192.168.239.195', database='GESTION', user='employer', password='AzErTy123*')
    cursor = conn.cursor()

    # cursor.execute("""USE GESTION""")
    # cursor.execute("""CREATE TABLE IF NOT EXISTS "Clients" (
    # "TYPE_DE_CLIENT" TEXT,
    # "RAISON_SOCIALE" TEXT,
    # "EMAIL" TEXT,
    # "TELEPHONE" INTEGER,
    # "ADRESSE" INTEGER
    # );""")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS "Lignes" (
    # "NOM_DU_PRODUIT" TEXT,
    # "REFERENCE" INTEGER,
    # "QUANTITE" INTEGER,
    # "PRIX_UNITE" INTEGER,
    # );""")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS "Factures"(
    # "N_FACTURE" TEXT,
    # "CLIENT" TEXT,
    # "DATE_EMISSION"	DATE,
    # "MONTANT_TOTAL" INTEGER
    # );""")




    if addc:
        add_client()
    if addf:
        add_facture()
    if affs:
        date()
    if rechf:
        rech_facture()
    if rechc:
        recherche_client()
    conn.commit()






if __name__ == "__main__":
    sys.exit(main())