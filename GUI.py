import cv2
from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.grid()

        self.frameObjetos = Frame(master)
        self.frameObjetos.grid()

        self.frameJumboMixNaranja = Frame(self.frameObjetos)
        self.frameJumboFlowBlanca = Frame(self.frameObjetos)
        self.frameJumboFlowNegra = Frame(self.frameObjetos)
        self.frameJumboMani = Frame(self.frameObjetos)
        self.frameJetAzul = Frame(self.frameObjetos)
        self.frameFrunasNaranja = Frame(self.frameObjetos)
        self.frameFrunasRojo = Frame(self.frameObjetos)
        self.frameFrunasAmarillo = Frame(self.frameObjetos)
        self.frameFrunasVerde = Frame(self.frameObjetos)


        self.frameJumboMixNaranja.grid(row = 0, sticky = E)
        self.frameJumboFlowBlanca.grid(row = 1, sticky = E)
        self.frameJumboFlowNegra.grid(row = 2, sticky = E)
        self.frameJumboMani.grid(row = 3, sticky = E)
        self.frameJetAzul.grid(row = 4, sticky = E)
        self.frameFrunasNaranja.grid(row = 5, sticky = E)
        self.frameFrunasRojo.grid(row = 6, sticky = E)
        self.frameFrunasAmarillo.grid(row = 7, sticky = E)
        self.frameFrunasVerde.grid(row = 8, sticky = E)

        self.numJumboMixNaranja = 0
        self.numJumboFlowNegra = 0
        self.numJumboFlowBlanca = 0
        self.numJumboMani = 0
        self.numJetAzul = 0
        self.numFrunasNaranja = 0
        self.numFrunasAmarillo = 0
        self.numFrunasRojo = 0
        self.numFrunasVerde = 0

        self.frameObjetos.grid(row=0)
        self.button = Button(master, text="Iniciar", command=self.greet())
        self.button.grid(row = 0, column = 1)


        self.labelJumboMixNaranja = Label(self.frameJumboMixNaranja, text="Número Jumbo Mix: ")
        self.labelNumJumboMixNaranja = Label(self.frameJumboMixNaranja, textvariable=self.numJumboMixNaranja)
        self.labelJumboMixNaranja.pack(side=LEFT)
        self.labelNumJumboMixNaranja.pack(side=RIGHT)

        self.labelJumboFlowBlanca = Label(self.frameJumboFlowBlanca, text="Número Jumbo Flow Blanca: ")
        self.labelNumJumboFlowBlanca = Label(self.frameJumboFlowBlanca, text=self.numJumboFlowBlanca)
        self.labelJumboFlowBlanca.pack(side=LEFT)
        self.labelNumJumboFlowBlanca.pack(side=RIGHT)

        self.labelJumboFlowNegra = Label(self.frameJumboFlowNegra, text="Número Jumbo Flow Negra: ")
        self.labelNumJumboFlowNegra  = Label(self.frameJumboFlowNegra, text=self.numJumboFlowNegra)
        self.labelJumboFlowNegra .pack(side=LEFT)
        self.labelNumJumboFlowNegra .pack(side=RIGHT)


        self.labelJumboMani = Label(self.frameJumboMani, text="Número Jumbo Maní: ")
        self.labelNumJumboMani = Label(self.frameJumboMani, text=self.numJumboMani)
        self.labelJumboMani.pack(side=LEFT)
        self.labelNumJumboMani.pack(side=RIGHT)


        self.labelJetAzul = Label(self.frameJetAzul, text="Número Jet: ")
        self.labelNumJetAzul = Label(self.frameJetAzul, text=self.numJetAzul)
        self.labelJetAzul.pack(side=LEFT)
        self.labelNumJetAzul.pack(side=RIGHT)


        self.labelFrunasNaranja = Label(self.frameFrunasNaranja, text="Numéro Frunas Naranja: ")
        self.labelNumFrunasNaranja = Label(self.frameFrunasNaranja, text=self.numFrunasNaranja)
        self.labelFrunasNaranja.pack(side=LEFT)
        self.labelNumFrunasNaranja.pack(side=RIGHT)


        self.labelFrunasAmarillo = Label(self.frameFrunasAmarillo, text="Numéro Fruna Amarillo: ")
        self.labelNumFrunasAmarillo = Label(self.frameFrunasAmarillo, text=self.numFrunasAmarillo)
        self.labelFrunasAmarillo.pack(side=LEFT)
        self.labelNumFrunasAmarillo.pack(side=RIGHT)


        self.labelFrunasRojo = Label(self.frameFrunasRojo, text="Numéro Fruna Rojo: ")
        self.labelNumFrunasRojo = Label(self.frameFrunasRojo, text=self.numFrunasRojo)
        self.labelFrunasRojo.pack(side=LEFT)
        self.labelNumFrunasRojo.pack(side=RIGHT)


        self.labelFrunasVerde = Label(self.frameFrunasVerde, text="Numéro Fruna Verde: ")
        self.labelNumFrunasVerde = Label(self.frameFrunasVerde, text=self.numFrunasVerde)
        self.labelFrunasVerde.pack(side=LEFT)
        self.labelNumFrunasVerde.pack(side=RIGHT)





    def greet(self):
        self.numFrunasVerde = 2
        root.update()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

