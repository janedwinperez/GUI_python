from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table, TableModel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import warnings
warnings.filterwarnings("ignore")

def imprimir():
    nombre = entry_1.get()
    print(nombre)
    entry_1.delete(0, END)

def close_window():
    raiz.destroy()


df = pd.read_csv("../Iris.csv")


   
raiz = Tk()
raiz.title("SOFTWARE DE REDES NEURONALES")
raiz.geometry("1200x800")

marco_1 = Frame(raiz, width=400, height=300)
marco_1.grid(row=0, column=0)
marco_1.config(bd=20)

boton_1 = Button(marco_1, text="Oprima", command=imprimir)
boton_1.place(x=0, y=0)

label_1 = Label(marco_1, text="Nombre:")
label_1.place(x=0, y=30)

entry_1 = Entry(marco_1)
entry_1.place(x=0, y=50)

marco_2 = Frame(raiz, width=400, height=200)
marco_2.grid(row=1, column=0)

table_1 = Table(marco_2, dataframe=df)
table_1.place(x=0, y=0)
table_1.show()

marco_3 = Frame(raiz, width=600, height=500)
marco_3.grid(row=0, column=1)
marco_3.config(bd=20, relief="sunken")

#fig = Figure(figsize=(4, 4), dpi=100)
#t = np.arange(0, 3, .01)
#fig.add_subplot(121).plot(t, 2 * np.sin(2 * np.pi * t))
#fig.add_subplot(122).plot(t, t**2)

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.boxplot(df["SepalLengthCm"])
ax1.set_ylabel('Damped oscillation')
ax2.bar(df["Species"], df["SepalLengthCm"])


canvas = FigureCanvasTkAgg(fig, master=marco_3)
canvas.draw()
canvas.get_tk_widget().place(x=0, y=0)

#Button for close window raiz
boton_2 = Button(raiz, text="Close", command=close_window)
boton_2.grid(row=1, column=1)

raiz.mainloop()

