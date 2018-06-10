#!/usr/bin/python
# -*- coding:utf-8 -*-
from click._compat import raw_input
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

db_user = MongoClient()["book_service"]["user"]
db_job = MongoClient()["book_service"]["job"]


def add_user():
    # Ask for data to store
    user = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        db_user.insert({"username": user, "password": pass_hash})
        print("User created.")
    except DuplicateKeyError:
        print("User already present in DB.")


def get_user():
    user = raw_input("Enter your username: ")
    result = db_user.find_one({'username': user})
    print(result)


def add_job():
    name = raw_input("Enter job name: ")
    content = raw_input("Enter job content: ")
    # Insert the user in the DB
    try:
        db_job.insert({"name": name, "job_content": content})
        print("job created.")
    except DuplicateKeyError:
        print("job already present in DB.")

def add_jobs():
    for i in range(100):
        name = 'j' + str(i)
        content = 'this is job ' + str(i)
        db_job.insert({"name": name, "job_content": content})
        print("job created.")

if __name__ == '__main__':
    # get_user()
    # add_user()
    # add_jobs()
    b = 1
    c = 2
    a = 1 if b == c else 0
    a = 1 if b == 1 else 0
    print(a)
