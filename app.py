from tkinter import *
import socket

tela_inicial = Tk()
tela_inicial.title('LOCALIZADOR DE IP')
tela_inicial.geometry("300x150+800+450")
tela_inicial.resizable(False, False)
tela_inicial.iconbitmap("image/icone.ico")
resultado = StringVar()
def buscar():
    nome = socket.gethostname()
    ip = socket.gethostbyname(nome)
    resultado.set(str(ip))

#label
lbl_espaco = Label(tela_inicial, width = 45, ).grid(row=0, columnspan=2)
lbl_ip = Label(tela_inicial, text= 'IPV4: ', width=20, ).grid(columnspan=2, sticky='WE')
lbl_resultado = Label(tela_inicial, textvariable=resultado, width=15, height=3, fg='red').grid(columnspan=2,row=2)

#button
btn = Button(tela_inicial, text="Pesquisar", command=buscar).grid(columnspan=2,row=3)

tela_inicial.mainloop()