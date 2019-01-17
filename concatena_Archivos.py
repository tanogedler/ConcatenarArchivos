import os.path
from NewMarketimUI import *

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import datetime

import os

from tkinter.filedialog import askopenfilename
listaArchivo1 = []
listaArchivo2 = []
listaResultado = []
class MainWindow(QtWidgets.QMainWindow, Ui_GenerarMarketim):


    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.setText("Añadir Archivo base")
        self.pushButton_2.setText("Añadir Archivo números")
        self.pushButton_3.setText("Generar nuevo archivo")


        self.pushButton.clicked.connect(self.addFile)
        self.pushButton_2.clicked.connect(self.addFile2)
        self.pushButton_3.clicked.connect(self.imprimeResultado)
        self.commandLinkButton.clicked.connect(self.reiniciar)

    

    def addFile(self):
        if len(listaArchivo1) > 0:
            print(listaArchivo1)
            messagebox.showinfo(title="Información", message="Ya se agregó archivo base")
            return
        Tk().withdraw() 
        filename = askopenfilename()
        self.label.setText("Archivo Base: " + filename)
        file1 = open(filename, "r") 
        
        for line in file1:
            listaArchivo1.append(line.rstrip('\n'))

        print(listaArchivo1)


    def addFile2(self):
        if len(listaArchivo1) == 0:
            Tk().withdraw()
            messagebox.showinfo(title="Información", message="Agregar Archivo base")
            return
        if len(listaArchivo2) > 0:
            messagebox.showinfo(title="Información", message="Ya se agregó archivo números")
            return
        Tk().withdraw() 
        filename2 = askopenfilename()
        self.label_2.setText("Archivo Números: " + filename2)
        file2 = open(filename2, "r") 
        
        for line in file2:
            listaArchivo2.append(line.rstrip('\n'))

        print(listaArchivo2)

        
        tmp = listaArchivo1.copy()

        for i in listaArchivo2:
            tmp[2] = tmp[2] + i
            tmp[4] = tmp[4] + i
        
            for j in tmp:
                listaResultado.append(j)
                tmp = listaArchivo1.copy()
        
        for k in range(0,len(listaResultado)-1):
        	listaResultado[k] += '\n'

        print(listaResultado)



    def imprimeResultado(self):
        Tk().withdraw()
        if len(listaResultado) == 0 :
            print("")
            messagebox.showinfo(title="Información", message="Agregar archivos de texto")
            return       
        
        dirname = filedialog.askdirectory()
        print(dirname)
        horaNombre = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        nombreArchivo = os.path.join(dirname, "NewMarketim" + horaNombre + ".vcf")

        fh = open(nombreArchivo, "w+")
        for i in listaResultado:
            fh.write(i)
        fh.close 


        messagebox.showinfo(title="Información", message="Archivo NewMarketim.txt generado con éxito")


    def reiniciar(self):
        global listaArchivo1, listaArchivo2, listaResultado
        listaArchivo1 = []
        listaArchivo2 = []
        listaResultado = []
        filename = ""
        self.label.setText("Archivo Base: " + filename)
        filename2 = ""
        self.label_2.setText("Archivo números: " + filename2)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()









    

