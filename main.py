from tkinter import *


janela = Tk()
janela.title('Login')  # Titulo da janela.
janela.geometry('500x600+400+50')  # Dimensão da janela e onde ela "Nasce".
# janela.iconbitmap('icons/icon_janela/icone.ico')
janela.resizable(0, 0)  # JANELA TRAVADA.
# janela.state('zoomed')  # O programa já abre em tela cheia
janela.config(background="#EEEEEE") # cor de fundo


# -Estilos-
# Texto Label
cor_letra = '#000'
cor_fundo = '#EEEEEE'
fonte = 'Calibri'


# -Label-
# NOME USER
login_texto = Label(
    janela,
    text='Usuário:',
    bg=f'{cor_fundo}',
    fg=f'{cor_letra}',
    font=f'{fonte}')
login_texto.place(x=126, y=220)

# SENHA
senha_texto = Label(
    janela,
    text='Senha:',
    bg=f'{cor_fundo}',
    fg=f'{cor_letra}',
    font=f'{fonte}')
senha_texto.place(x=126, y=245)


# -Entry-
# USUARIO
user = Entry(janela)
user.place(x=190, y=225)

# SENHA
senha = Entry(janela, show='*')
senha.place(x=190, y=250)


# -Button-
# ENTRAR
entrar_icone = PhotoImage(file='icons/entrar.png')
entrar = Button(janela, image=entrar_icone, text='Entrar')
entrar.place(x=270, y=280)



janela.mainloop()
