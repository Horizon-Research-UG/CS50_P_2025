# Name: indoor.py 
# Meta: implement a program in Python
# Ticket 1: that prompts the user for input and then 
# print()
# x = input("Hallo, schreib mal bitte was : )  ---->  : ")
# print()

# outputs that same input in lowercase.
# print(x.lower())
# print()
#   Punctuation and whitespace should be outputted unchanged. 
# 
# You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.


# so Aufgabe erfüllt -> schonmal pushen


# ---
# jetzt das ganze aufs nächste Level bringen:

"""

def abstand():
    print()

def eingang():
    abstand()
    x = input("Hallo, schreib mal bitte was : )  ---->  : ")
    abstand()
    return x

def i_V():
    print(x.lower())

eingang()
i_V()

# Name Error

"""

"""

# Versuch 3

def abstand(): # für abstand = Übersicht im Terminal
    print()


def eingang(): # holt input und gibt aus

    abstand()

    x = input("Hallo, schreib mal bitte was : )  ---->  : ")

    abstand()

    return x

def iv():
    return eingang().lower()

print(iv())

abstand()

# funktioniert - sieht aber nicht schön aus 

"""
"""

# Versuch 4

def abstand():
    print("Hallo " * 2)

a = abstand

a()

a() * 2

# abgedriftet -> versuch funktionen erst sinnvoll zu bennen und definieren und dann später einfacher (mit weniger tippen) nutzten zu können

"""


# Versuch 5



#############################
#############################


## Abstand


def abstand():
    print("\n" * 2)
# definiert abstand für Terminal

a = abstand
# kürzt die Funktion, um einfacher zu schreiben

#####################################################


## text holen


text = input("Was möchtest du eingeben? :     ---->     : ")
# packt den string aus der Input frage in die Variable text

t = text
#kürzen


###########################


## Text klein schreiben


indoor_Voice = t.lower()
# text klein schreiben

iv = indoor_Voice
#kürzen



#############################

## drucken

#print(iv)
# druckt die iv



#################


## was eigenes ergänzen


print("deine geflüstere Eingabe ist: ----> " +  iv)


