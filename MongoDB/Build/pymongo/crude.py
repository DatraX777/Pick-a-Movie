from xml.etree.ElementTree import tostring
from pymongo import MongoClient
import sys


client = MongoClient('10.5.0.3',27017)
film = client.Film
top250 = film.Top250

profil = client.Profil
users = profil.User
admin = profil.Admin

x = []


if len(sys.argv) % 2 !=1 :
    print("Il n'y pas le bon nombre d'argument!")
elif sys.argv[1] == "top250" :
    if sys.argv[2] == "find" :
        res = (top250.find({ sys.argv[3] : sys.argv[4]}))
        for doc in res :
            x.append(doc)
        print(x)
        exit