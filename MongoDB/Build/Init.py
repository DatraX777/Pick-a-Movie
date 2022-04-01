from pymongo import MongoClient


def initialize():
    client = MongoClient('10.5.0.5',27017)
    film = client.Film
    top250 = film.Top250

    profil = client.Profil
    users = profil.User
    admin = profil.Admin

    x = []
