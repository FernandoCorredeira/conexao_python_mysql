from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from main import *
from tkinter import messagebox
from main import create_cars

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

    def btn_add_car():

        #Atribuição dos dados em uma variavel para manipulação
        data_model_car = i_model_car.get()
        data_mark_car = i_mark_car.get()
        data_year_car = i_year_car.get()

        list_car = [data_mark_car, data_model_car, data_year_car]

        #Verificação de dados
        for i in list_car:
            if i == '':
                messagebox.showerror("Error","Insira dados")
                return
            
            #Inserção
            create_cars(data_mark_car, data_model_car, data_year_car)
            messagebox.showinfo("Sucesso","Carro cadastrado")

            #limpando campos do input
            i_model_car.delete(0,END)
            i_mark_car.delete(0,END)
            i_year_car.delete(0,END)


    app_ = Label(frameDireita, text="Inserir novo Carro", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
    app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)

    app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
        
        #Texto de modelo do carro
    l_model_car = Label(frameDireita, text="Nome do modelo carro", font=('Ivy 12'), bg=co3, fg=co5)
    l_model_car.grid(row=2, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do modelo
    i_model_car = Entry(frameDireita, width=25,justify='left', relief='solid')
    i_model_car.grid(row=2, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto de marca do carro
    l_mark_car = Label(frameDireita, text="Nome da marca do carro", font=('Ivy 12'), bg=co3, fg=co5)
    l_mark_car.grid(row=3, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do marca
    i_mark_car = Entry(frameDireita, width=25,justify='left', relief='solid')
    i_mark_car.grid(row=3, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto de ano do carro
    l_year_car = Label(frameDireita, text="Ano do carro", font=('Ivy 12'), bg=co3, fg=co5)
    l_year_car.grid(row=4, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do ano
    i_year_car = Entry(frameDireita, width=25,justify='left', relief='solid')
    i_year_car.grid(row=4, column=1, padx=5,pady=10, sticky=NSEW)

        #btn salvar
    b_car_salvar = Button(frameDireita, command=btn_add_car, compound=LEFT, width=25, anchor=NW, text=" Salvar Carro", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_car_salvar.grid(row=5, column=1, sticky=NSEW, pady=5)



# Exibir Carros
def view_car():
    app_ = Label(frameDireita, text="Exibir Carros", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
    app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)

    app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_carros()

    list_header = ['ID','Marca','Modelo','Ano']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show='headings')

    #Vertical Scrollbar

    vsb = ttk.Scrollbar(frameDireita, orient='horizontal',command=tree.yview)

    #Horizontal Scrollbar

    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h=[20, 80, 80, 120, 120, 76, 100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')

        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

        for item in dados:
           tree.insert('', 'end', values=item)




#Função para controlar menu

def controlMenu(i):
    if i == "Adicionar Carros":
        for widget in frameDireita.winfo_children():
            widget.destroy()
            
        #Chamando função
        adicionar_carros()
        
        #Exibir carros
        #if i == "Exibir Carros":
          #  for widget in frameDireita.winfo_children():
         #       widget.destroy()
            
        #Chamando função
        #view_car()




#Menu lateral

b_car = Button(frameEsquerda, command=lambda:controlMenu('Adicionar Carros'), compound=LEFT, anchor=NW, text="  Adicionar Carro", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_car.grid(row=0, column=0, sticky=NSEW, padx=5,pady=6)

b_verCar = Button(frameEsquerda, command=lambda:controlMenu('Exibir Carros'), compound=LEFT, anchor=NW, text="  Exibir Carros", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_verCar.grid(row=1, column=0, sticky=NSEW, padx=5,pady=6)

b_carDelete = Button(frameEsquerda, compound=LEFT, anchor=NW, text="  Deletar Carro", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_carDelete.grid(row=2, column=0, sticky=NSEW, padx=5,pady=6)





janela.mainloop()
