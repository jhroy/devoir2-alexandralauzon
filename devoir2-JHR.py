# coding : utf-8

import csv, json
import requests

#Je crée un fichier lobbying pour plus tard.

fichier = "lobbying.csv"

url = "http://jhroy.ca/uqam/lobby.json"

#Je créé également une en-tête, par politesse.

entetes = {
    "User-Agent":"Alexandra : requête envoyée dans le cadre d'un cours de journalisme de données",
    "From":"alexandra.lauzon@hotmail.com"
}

#Je vérifie que tout fonctionne. 

req = requests.get(url,headers=entetes)

# print(req)

#J'ai mon "Response 200", donc je continue.
#Je met tout de même une condition si je n'ai pas mon Response 200.

#Ensuite, j'établis mes données 

# lobby = req.json()

# code = lobby["registre"][0][0]["client_org_corp_num"]
# orgFR = lobby["registre"][0][0]["fr_client_org_corp_nm"]
# orgAN = lobby["registre"][0][0]["en_client_org_corp_nm"]
# date = lobby["registre"][0][0]["date_comm"]
# objet1 = lobby["registre"][0][1][0]["objet"]
# objet2 = lobby["registre"][0][1][0]["objet_autre"]

# for b in (objet1,objet2):
#     infos = []
#     if (objet1,objet2) == "limat":
#         print(code,orgFR,orgAN,date,objet1,objet2)
        

# for nb in lobby:
#     infos = []
#     if req.status_code != 200:
#         print("Ça ne fonctionne pas")
#     elif (objet1, objet2) == "limat":
#         print(code,orgFR,orgAN,date,objet1,objet2)
    #     infos.append(code)
    #     infos.append(orgFR)
    #     infos.append(orgAN)
    #     infos.append(date)
    #     infos.append(objet1)
    #     infos.append(objet2)
    #     print(infos)

    #     journalisme = open(fichier,"a")
    #     donnees = csv.writer(journalisme)
    #     donnees.writerow(infos)
    # print(req)

n=0

# nombres = list()

# for nb in nombres:
#     infos = []

infos = []
    
#le req doit être dans la boucle ### NON, JUSTEMENT, À L'EXTÉRIEUR. UNE SEULE REQUÊTE SUFFIT
    # req = requests.get(url,headers=entetes)

req = requests.get(url,headers=entetes)

    #condition si le 200 ne marche pas ### PAS VRAIMENT NÉCESSAIRE DANS CE CAS-CI
    # if req.status_code != 200:
    #     print("Ça ne marche pas")
    # else: 
lobby = req.json()

# print(lobby)
# n += 1
#         infos.append(n)
#         infos.append(nb)

### TES CONDITIONS CI-DESSOUS SONT BONNES...
### MAIS ELLES NE TESTENT QUE LE PREMIER DES 72000 ÉLÉMENTS À VÉRIFIER...
if lobby["registre"][0][1][0]["objet"]== "limat":
    objet1 = lobby["registre"][0][1][0]["objet"]
    infos.append(objet1)
elif lobby["registre"][0][1][0]["objet_autre"]== "limat":
    objet2 = lobby["registre"][0][1][0]["objet_autre"]
    infos.append(objet2)
print(infos)
#         else:
#             code = lobby["registre"][0][0]["client_org_corp_num"]
#             infos.append(code)
#             orgFR = lobby["registre"][0][0]["fr_client_org_corp_nm"]
#             infos.append(orgFR)
#             orgAN = lobby["registre"][0][0]["en_client_org_corp_nm"]
#             infos.append(orgAN)
#             date = lobby["registre"][0][0]["date_comm"]
#             infos.append(date)
#             print(infos)

#             dead = open(fichier,"a")
#             obies = csv.writer(dead)
#             obies.writerow(infos)

#         print(req)

# #Ça ne fonctionne pas, mais malgré plusieurs essais, je ne trouve malheureusement pas la façon de créer mon fichier csv.
# # J'ai fait beaucoup de recherches sur des forums et des sites de tutoriels, mais je n'ai pas trouvé de solution. 