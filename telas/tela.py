from tkinter .ttk import *
from tkinter import *
#import img

co0 = "#6A5ACD"
co1 = "#87CEEB"
co2 = "#FFFAFA"
co3 = "#E6E6FA"
co4 = "#FA8072"
co5 = "#708090" #Gray

# Janela/Widget Windows
janela = Tk()
janela.title("Gerenciamento")
janela.geometry('770x330')
janela.configure(background=co3)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")
# Containers
frameCima = Frame(janela, width=770, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1,column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co3, relief="raised")
frameDireita.grid(row=1,column=1, sticky=NSEW)

# Style Container Header
app_ = Label(frameCima, text="Gerenciamento de Estoque", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), fg=co4)
app_.place(x=50, y=7)
app_linha = Label(frameCima,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 ,fg=co4)
app_linha.place(x=0, y=47)




# Novo Carro

def adicionar_carros():

    app_ = Label(frameDireita, text="Inserir novo Carro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
    app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)
    app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 ,fg=co4)
    app_linha.place(x=0, y=47)
#Função para controlar menu

def controlMenu(i):
    if i == "Adicionar Carros":
        for widget in frameDireita.winfo_children():
            widget.destroy()
            
        #Chamando função
        adicionar_carros()




#Menu lateral

b_car = Button(frameEsquerda,command=lambda:controlMenu('Adicionar Carros'), compound=LEFT, anchor=NW, text="  Adicionar Carro", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_car.grid(row=0, column=0, sticky=NSEW, padx=5,pady=6)
b_verCar = Button(frameEsquerda, compound=LEFT, anchor=NW, text="  Exibir Carros", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_verCar.grid(row=1, column=0, sticky=NSEW, padx=5,pady=6)
b_carDelete = Button(frameEsquerda, compound=LEFT, anchor=NW, text="  Deletar Carro", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_carDelete.grid(row=2, column=0, sticky=NSEW, padx=5,pady=6)





janela.mainloop()
