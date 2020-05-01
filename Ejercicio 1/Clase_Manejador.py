import csv

from Clase_Email import Email

import re

class Manejador_Lista_Mail:
    def __init__(self):
        self.__listaEmails = []

    def agregaEmail(self, mail):
        self.__listaEmails.append(mail)

    def buscarMailporDom(self,dominio):
        contador=0
        for email in self.__listaEmails:
            id=email.split("@")
            domi= id[1].split(".")
            if(str(domi[0])== dominio):
                contador = contador +1
        return contador
