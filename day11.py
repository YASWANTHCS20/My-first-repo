from flask import Flask, jsonify, request

import sqlite3

from sql import deletes, insert,updates
from sql import getall

app =Flask(__name__)
@app.get('/')
def vk():
    return "mainpage"

@app.post('/h')


def s1():
    data= request.get_json()
    insert(data)
    print(data)
    return 'DATA IS RETRIEVED'

@app.post('/v')
def s2():
    data= getall()
    return (jsonify(data))

@app.patch('/upd')
def update():
    data = request.get_json();
    updates(data);
    print(data)
    return("Updated");

@app.delete('/del/<roll_no>')
def delete(roll_no):
    deletes(roll_no);
    return("Deleted")


@app.patch('/pat/<inputId>')
def patchmethod(inputId):
    data = request.get_json()
    users = data 

    #print(inputId)
    #print (f'The users data is{users}')

    if inputId in users.values():
        users["Id"] = 1000
        print(f"The data after updating is{users}")
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"

@app.delete('/del/<inputId>')
def deletemethod(inputId):
    data = request.get_json()
    users = data 

    #print(inputId)
    #print (f'The users data is{users}')

    if inputId in users.values():
        del users["Id"]
        #print(f"The data after deleting is{users}")
        print(f"the data is deleted {users}")
        res = "Data deleted"
        
        return res
    res = "Data not found"
    return res

app.run(debug=True)
