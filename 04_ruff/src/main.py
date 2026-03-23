import os
import sys
import json
from collections import OrderedDict

def greet( name,age ):
    x=1
    message = "Hello, " +name+ "! You are " +str(age)+ " years old."
    print(message)
    unused_var = 42
    return message

class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

    def get_info( self ):
        info = dict()
        info["name"]=self.name
        info["age"]=self.age
        info["email"]=self.email
        return info

def calculate(a,b):
    result=a+b
    if result == True:
        print("true")
    elif result == False:
        print("false")
    return result

names = ["Alice","Bob","Charlie"]
for i in range(len(names)):
    print(names[i])

greet("World",25)
