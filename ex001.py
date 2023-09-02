from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []

def adicionarcontato() -> None:
    #pegar os valores digitado
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categoria.get()
    contato = {
        "nome":nome,
        "telefone": telefone,
        "categoria":categoria

    }
    agenda.append(contato)
    messagebox.showinfo("adicionado!","contato adícinado com sucesso!")
    limparcampos()
    atualizartabela()



def editarcontato() -> None:
    contatoselecinado = tabela.selection()[0]
    if not contatoselecinado:
        return
    index = tabela.index(contatoselecinado)
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_telefone.get(),
        "categoria": cb_categoria.get()
    }
    limparcampos()
    atualizartabela()

def deletarcontato() ->None:
    contatoselecinado = tabela.selection()[0]
    if not contatoselecinado:
        return
    index = tabela.index(contatoselecinado)
    del agenda[index]
    limparcampos()
    atualizartabela()




def limparcampos() ->None:
    txt_nome.delete(0,END)
    txt_telefone.delete(0,END)
    cb_categoria.delete(0,END)


def atualizartabela() -> None:
    #limpando a tabela
    for linha in tabela.get_children():
        tabela.delete(linha)




    for contato in agenda:
        tabela.insert("", END,values=(contato["nome"],contato["telefone"],
                                      contato["categoria"]))


def tabelaClique(event) -> None:
    contatoselecinado = tabela.selection()[0]
    if not contatoselecinado:
        return
    index = tabela.index(contatoselecinado)
    contato = agenda[index]
    limparcampos()
    txt_nome.insert(0,contato["nome"])
    txt_telefone.insert(0,contato["telefone"])
    cb_categoria.set(0,contato["categoria"])




janela = Tk()
#como adicionar titulo na janela
janela.title("agenda telefonica")

#como criar um label
label_nome = Label(janela, text="nome: " , fg="navy", font="taghoma 14 bold")
#como adicionar na janela
label_nome.grid(row=0,column=0)
#como criar um campo de texto => entry
txt_nome = Entry(janela, font="tahoma 14", width=27)
txt_nome.grid(row=0, column=1)


label_telefone = Label(janela, text="telefone: " , fg="navy", font="taghoma 14 bold")
label_telefone.grid(row=1,column=0)

txt_telefone = Entry(janela, font="tahoma 14", width=27)
txt_telefone.grid(row=1, column=1)

label_categoria = Label(janela, text="categoria: ", fg="navy" ,font="tahoma 14 bold")
label_categoria.grid(row=2,column=0)
categorias = ["amigos", "família", "trabalho"]
cb_categoria = ttk.Combobox(janela, values=categorias,width=23,
                            font="tahoma 14")
cb_categoria.grid(row=2,column=1)


btn_adicionar = Button(janela, text= "adicionar", fg="navy" , bg="green", font="tahoma 12 bold" ,width=8, height=1 ,
                       command=adicionarcontato)
btn_adicionar.grid(row=3,column=0)

btn_editar = Button(janela, text= "editar", fg="navy" , bg="green", font="tahoma 12 bold" ,width=8, height=1 ,
                       command=editarcontato)
btn_editar.grid(row=3,column=1)

btn_excluir = Button(janela, text= "excluir", fg="navy" , bg="green", font="tahoma 12 bold" ,width=8, height=1 ,
                       command=deletarcontato)
btn_excluir.grid(row=3,column=2)

#como criar uma tabela => treeview

tabela = ttk.Treeview(janela,columns=("nome", "telefone" , "categoria"),
                      show="headings")
tabela.heading("nome", text="nome")
tabela.heading("telefone", text="telefone")
tabela.heading("categoria", text="categoria")
tabela.bind("<ButtonRelease-1>", tabelaClique)
tabela.grid(row=4,columnspan=3)




janela.mainloop()