import math
import time

print("""
Bievenue sur l'application console tripshape,

l'application qui utilise le théorème de pythagore

(ne prend seulement en compte les variable entière "int")

""")

def pythagore():
    seg1 = str(input("domme moi la lettre du premier segment : "))
    seg2 = str(input("donne moi la lettre du deuxième segment : "))
    seg3 = str(input("donne moi la lettre du dernier segment : "))

    triangle = seg1, seg2, seg3
    
    m_seg1 = int(input("combien mesure le segment " + str(seg1 = " ? : ")))
    m_seg2 = int(input("combien mesure le segment " + str(seg2 = " ? : ")))
    m_seg3 = int(input("combien mesure le segment " + str(seg3 = " ? : ")))

pythagore()