from ast import arg
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

print(type(sys.argv[2]))
print(type(str(sys.argv[2])))


if len(sys.argv) % 2 !=0 :
    print("Il n'y pas le bon nombre d'argument!")
elif sys.argv[1] == "find" :
        res = top250.find({sys.argv[2] : sys.argv[3]})
        for doc in res :
            x.append(doc)
            print(doc)
        exit
elif sys.argv[1] == ""