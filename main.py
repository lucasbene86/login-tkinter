from tkinter import *
from tkinter.font import Font


janela = Tk()
janela.title('Login')  # Titulo da janela.
janela.geometry('500x600+400+50')  # Dimensão da janela e onde ela "Nasce".
# janela.iconbitmap('icons/icon_janela/icone.ico')
janela.resizable(0, 0)  # JANELA TRAVADA.
# janela.state('zoomed')  # O programa já abre em tela cheia
janela.config(background="#EEEEEE") # cor de fundo


# NOME USER
login_texto = Label(janela, text='Usuario:', bg='#0085FF', fg='#FFFFFF')
login_texto.place(x=130, y=225)

# SENHA
senha_texto = Label(janela, text='Senha:')
senha_texto.place(x=130, y=250)

# USUARIO
user = Entry(janela)
user.place(x=190, y=225)

# SENHA
senha = Entry(janela, show='*')
senha.place(x=190, y=250)






janela.mainloop()
