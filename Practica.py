# -*- enconding: utf-8 -*-
import os
import ctypes
from tkinter import *
from tkinter import filedialog
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from Prac1gui import *
import time
import math
from deep_translator import GoogleTranslator

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_ingresar.clicked.connect(self.operaciones)

    def operaciones(self):
        raiz=Tk()
        self.ui.CaracTo.setText('#')
        self.ui.Entropia.setText('#')
        self.ui.CantidadDeI.setText('#')
        self.ui.Redundancia.setText('#')
        self.ui.Eficiencia.setText('#')
        self.ui.cantletra.setText('#')
        self.ui.letra_incorrecta.setText('')
        self.abrirArchivo()
        #print (archivo)
        fichero= open(archivo)
        fraseinicio=fichero.read()

        #traductor de idiomas para guardar la frase en español
        traductor = GoogleTranslator(source='auto', target='es')
        resultado = traductor.translate(fraseinicio)
        frase = resultado
        #test
        #frase = "..Este es un test para la practica 1. @ # "

        #convierte las letras en minusculas
        frase= frase.lower()
        #tamaño de la frase
        longitud=len(frase)

        #variables definidas para evitar errores    
        caract = []
        caract_prob = []
        entropia=0
        info_tot=0
        L=0
        p=26
        s=27

        #calcula la cantidad de letras del abecedario con codigo ascci
        for j in range(97,122):
            count=0
            for i in range(len(frase)):
                if frase[i]== chr(j):
                    count +=1
            caract.append(j-97)
            caract[j-97]=count

        #calcula cantidad de puntos
        count=0
        for i in range(longitud):
            if frase[i]== chr(46):
                count +=1
        caract.append(p)
        caract[p-1] = count;

        #calcula la cantidad de espacios
        count=0
        for i in range(longitud):
            if frase[i] == chr(32):
                count +=1
        caract.append(s)
        caract[s-1]= count;

        #calcula la probabilidad de cada caracter
        for i in range(0,27):
            caract_prob.append(i)
            caract_prob[i]= (caract[i]/longitud)

        #calcular entropia
        for i in range(0,25):
            if caract[i]!=0:
                entropia= float(entropia)+ float((caract_prob[i])*float(math.log2(1/caract_prob[i])))

        #calcula informacion total
        for i in range(0,25):
            if caract[i] != 0:
                info_tot = float(info_tot)+ float(math.log(1/ caract_prob[i])/math.log(2))

        #calcula longitud media
        for i in range(0,25):
            L = L +(caract[i]*longitud)

        #calcular eficencia
        efic= (entropia/L)

        #calcula redundancia
        red = float(1-efic)

        #impresion de resultados
        #print("El programa funciona con letras del alfabeto español por lo tanto el documento es traducido a este idoma")
        #print("El archivo contiene la frase: * "+ frase +" * en el idioma español")
        #print("Longitud: "+ str(longitud))
        #print("Entropia: "+ str(entropia))
        #print("Cantidad de informacion total: "+ str(info_tot))
        #print("Eficacioa: "+ str(float(100*efic))+"%")
        #print("Redundancia: "+ str(red))
        self.ui.CaracTo.setText(str(longitud))
        self.ui.Entropia.setText(str(entropia))
        self.ui.CantidadDeI.setText(str(info_tot))
        self.ui.Redundancia.setText(str(red))
        self.ui.Eficiencia.setText(str(float(100*efic)))

        #Solicita al usuario una letra e imprime la cantidad de veces que se repite
        letra = self.ui.letra.text()
        letra=letra.lower()
        #print(letra)
        if letra.isalpha() and len(letra)==1:
            indice=ord(letra)-97
            self.ui.cantletra.setText(str(caract[indice]))
        else:
            self.ui.usuario_incorrecto.setText('Ingrese un caracter valido')
            #print("la letra "+ letra +" se repite "+ str(caract[indice])+" veces")

    def abrirArchivo(self,text="Abrir Archivo"):
        global archivo
        archivo= filedialog.askopenfilename(title="Abrir")
        self.ui.rutadelArc.setText(archivo)
        return archivo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    entropia= MiApp()
    entropia.show()
    sys.exit(app.exec())
