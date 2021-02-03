import argparse
import sys
import mysql.connector
import logging



logging.basicConfig(filename="logfacture.log", level=logging.DEBUG,
format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logging.debug("on ouvre le dossier et on met en place les arguments")
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
logging.debug("on définit des variables pour mieux s'y retrouver dans nos arguments")
addu = args.ajouter_user
addc = args.ajouter_client
#addl = args.ajouter_ligne
addf = args.ajouter_facture
modc = args.modifier_client
rechc = args.rechercher_client 
rechf = args.rechercher_facture 
betf = args.factures
supp = args.supprimer
#remi = args.remise
#sup = args.suprimmer

# conn = mysql.connector.connect(host='192.168.242.195', database='GESTION', user='employer', password='AzErTy123*')
# cursor = conn.cursor()

# def add_user(cursor):             
#     #Créé un utilisateur 
#     cursor.execute("""CREATE USER '?' IDENTIFIED WITH mysql_native_password""", (addu))
#     return 0
# # def user_connect():
# #     cursor.execute('SELECT user, host, plugin, authentication_string FROM mysql.user)

def add_client(cursor):
#Ajouter les informations d'un client
    cursor.execute("""INSERT INTO Clients VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""", (addc[0], addc[1], addc[2], addc[3], addc[4], addc[5], addc[6], addc[7]))
    logging.info("lancement de la fonction d'ajout de client")
    return 0

def add_facture(cursor):
    #Ajouter une ligne facture à la bdd
    cursor.execute('INSERT INTO Facture (id_Clients, id, DATE_EMISSION) VALUES (%s,%s,%s)', (addf[0], addf[1], addf[2]))
    logging.info("lancement de la fonction d'ajout de facture ")
    return 0

def add_ligne(cursor):
#Ajouter une facture détaille à la bdd
    cursor.execute('INSERT INTO Lignes (NOM_DU_PRODUIT, REFERENCE, QUANTITE, PRIX_UNITE) VALUES (%s;%s,%s,%s)', (addf[0],addf[1],addf[2],addf[3]))
    logging.info("lancement de la fonction d'ajout de produit")
    return 0

def rech_factures(cursor):
# rechercher une facture avec le numéro dans la bdd
    cursor.execute("""SELECT n_Facture FROM Facture WHERE '%s' """, (rechf))
    logging.info("lancement de la fonction recherche facture")
    return 0

def rech_client(cursor): 
#rechercher un client avec son nom et/ou son mail
    cursor.execute("""SELECT RAISON_SOCIAL AND EMAIL FROM Clients WHERE '%s' AND '%s' """, (rechc[0], rechc[1]))
    logging.info("lancement de la fonction recherche client")
    return 0

def modif_client(cursor):
#Modifier les infos d'un client
    cursor.execute("""UDPDATE Clients SET '%s' = '%s' WHERE '%s' """, (modc[0], modc[1], modc[3]))
    logging.info("lancement de la fonction modifier client")
    return 0

def between_date(cursor):
#Ajouter une date à la facturation
    cursor.execute("""SELECT * FROM Facture WHERE DATE_EMISSION BETWEEN '%s' AND '%s' """, (betf[0],betf[1]))
    for i in cursor.fetchall():
        factures = (f'id_Clients{i[0]} n_Facture{i[1]} DATE_EMISSION{i[2]} MONTANT_TOTAL{i[3]}')
        print(factures)
    logging.info("lancement de la fonction qui ajoute une date a la facture")

# def montant_total():
#     Total = []
#     if addl:
#         result = QUANTITE*PRIX_UNITE
#         Total.append(result)

#     cursor.execute("""  """)

def remise():
#Ajouter une remise pour la déduire sur le prix
    remise = (remi)*100/result
    return 0

def supprimer(cursor):
#Supprimer une ligne dans la bdd
    cursor.execute("""DELETE FROM `'%s' `WHERE '%s'""", (supr[0], supr[1]))
    return 0


def main():
#Création de la db, des tables de gestion client et facture

    # cursor.execute("""CREATE DATABASE GESTION""")
    #Créé un utilisateur 
    # cursor.execute("""CREATE USER '?' IDENTIFIED WITH mysql_native_password""", (addu))
    conn = mysql.connector.connect(host='192.168.1.133', database='Gestion', user='stephanie', password='AzErTy123*')
    c = conn.cursor()

    # cursor.execute("""USE GESTION""")
    # cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion_client" (
    # "TYPE_DE_CLIENT" TEXT,
    # "RAISON_SOCIALE" TEXT,
    # "EMAIL" TEXT,
    # "TELEPHONE" INTEGER,
    # "ADRESSE" INTEGER
    # );""")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion_ligne" (
    # "NOM_DU_PRODUIT" TEXT,
    # "REFERENCE" INTEGER,
    # "QUANTITE" INTEGER,
    # "PRIX_UNITE" INTEGER,
    # );""")

    # cursor.execute("""CREATE TABLE IF NOT EXISTS "gestion_facture"(
    # "N_FACTURE" TEXT,
    # "CLIENT" TEXT,
    # "DATE_EMISSION"	DATE,
    # "MONTANT_TOTAL" INTEGER
    # );""")

    if addc:
        add_client(c)
    if addf:
        add_facture(c)
    if betf:
        between_date(c)
    if rechf:
        rech_factures(c)
    if rechc:
        rech_client(c)
    conn.commit()

if __name__ == "__main__":
    sys.exit(main())