from tkinter import *
import sqlite3

class Gui():
    """
    Classe que define a interface gráfica da aplicação
    """
    
    #Criando a janela
    window = Tk()
    window.wm_title("Cadastro Clientes")
    
    
    #Criando variáveis que armazenarão o texto inserido pelo usuário
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCpf = StringVar()
    
    #Criando os objetos que estarão na janela
    #O primeiro argumento (window) define a qual janela este label pertence.
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblcpf = Label(window, text="Cpf")
    
    entNome = Entry(window, textvariable=txtNome)
    entSobrenome = Entry(window, textvariable=txtSobrenome)
    entEmail = Entry(window, textvariable=txtEmail)
    entCPF = Entry(window, textvariable=txtCpf)
    
    #ListBox que listará todos os clientes cadastrados
    listClientes = Listbox(window)
    
    #Funcionar em conjunto com o ListBox
    scrollClientes = Scrollbar(window)
    
    #criar os botões que estarão disponíveis na interface
    btnViewAll = Button(window, text="Ver todos")
    btnBuscar = Button(window, text="Buscar")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")
    
    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0)
    lblsobrenome.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnBuscar.grid(row=5, column=0, columnspan=2)
    btnInserir.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)
    
    #Associando a Scrollbar com a Listbox...
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)
    
    x_pad = 5
    y_pad = 3
    width_entry = 30
    
    #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    
    def run(self):
        Gui.window.mainloop()
        
    
    