##################################################################################
# Dicionario limitado em inglês - apenas digitar uma palavra e o dicionario irá 
# descrever a palavra, também procura por palavras parecidas.
# Nome: Matheus "Caps" Milani
# Data: 02/04/2021
# Rev: 0.0 
##################################################################################

##################################################################################
# Libs necessárias: json, difflib e tkinter 
# Todas libs padrão do python
##################################################################################
import json
import difflib
from tkinter import *

##################################################################################
# Instanciação e obtenção de itens
# window - Instanciação do Objeto Tkinter
# data - dicionario importado do arquivo "data.json"
##################################################################################
window = Tk()

with open("data.json") as json_file:
    data = json.load(json_file)


##################################################################################
# Função responsável por verificar se a palavra digitada encontra-se no dicionario
# Entrada:  word (srt) - palavra que deseja obter no dicionario
#           di (dict) - dicionario que deve procurar a palavra 
# Saída:    aux (str) - conjunto de significados encontrados no dicionario
##################################################################################
def foo(word, di):
    aux = ''
    if isinstance(di[word], list):
        for i in di[word]:
            aux = aux + i + "\n"
    else:
        aux = di[word]
    return aux

##################################################################################
# Função responsável por receber as "traduções" e inserir na tela, além de tratar
# de palavras parecidas não encontradas
# Entrada:  none
# Saída:    none
##################################################################################
def logic(): 
    word = e1_value.get()
    if word in data:
        meaning = foo(word, data)
        t1.delete('1.0', END)
        t1.insert(END, meaning)
    elif word.capitalize() in data:
        meaning = foo(word.capitalize(), data)
        t1.delete('1.0', END)
        t1.insert(END, meaning)
    elif word.upper() in data:
        meaning = foo(word.upper(), data)
        t1.delete('1.0', END)
        t1.insert(END, meaning)
    else:
        x = difflib.get_close_matches(word, data.keys(), 1)
        if x != []:
            global alert
            alert = Toplevel(window)
            f11 = Label(alert, text = "Did you mean {}?".format(x[0].upper()))
            f11.grid(row = 0, columnspan = 2)
            b11 = Button(alert, text = "Yes", command = lambda: choice('yes', foo(x[0], data)))
            b11.grid(row = 1, column = 0)
            b12 = Button(alert, text = "No", command = lambda : choice('no', ''))
            b12.grid(row = 1, column = 1)
            alert.mainloop()               
        else:
            meaning = "Wrong word! Please type another word or double check it!"
            t1.delete('1.0', END)
            t1.insert(END, meaning)


##################################################################################
# Função responsável por selecionar resposta do alerta de palavra proxima e 
# destruir a tela de alerta.
# Entrada:  r (str) - resposta do alerta (botão sim ou não)
#           i (str) - significado encontrado no dict            
# Saída:    none
##################################################################################
def choice(r, i):
    if r == 'yes':
        t1.delete('1.0', END)
        t1.insert(END, i)
    if r == 'no':
        meaning = "Wrong word! Please type another word or double check it!"
        t1.delete('1.0', END)
        t1.insert(END, meaning)
    alert.destroy()

##################################################################################
# Funções resposáveis por criar a interface gráfica do dicionario
# f2 - Título da interface gráfica (columnspan mescla espaços da tela)
# f1 - Escrita na tela "Type a word:"
# e1 - Entrada de texto (palavra digitada)
# t1 - Local destinado a resposta da palavra procurada
# b1 - Criação do botão para procurar a palavra digitada
# mainloop() - responsável por deixar a interface rodando
##################################################################################
f2 = Label(window, text = "Dictionary in English: type a word and the app will translate it for you!!")
f2.grid(row = 0, columnspan = 3)


f1 = Label(window, text = "Type a word: ")
f1.grid(row = 1, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 1, column = 1)

t1 = Text(window)
t1.grid(row = 2, columnspan = 3)

b1 = Button(window, text = "Meaning", command = logic)
b1.grid(row = 1, column = 2)



window.mainloop()





