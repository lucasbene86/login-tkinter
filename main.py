from tkinter import *


janela = Tk()
janela.title('Login')  # Titulo da janela.
janela.geometry('350x450+400+50')  # Dimensão da janela e onde ela "Nasce".
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
login_icone = PhotoImage(file='icons/user.png')
login_texto = Label(
    janela,
    text='Usuário:',
    bg=f'{cor_fundo}',
    fg=f'{cor_letra}',
    font=f'{fonte}',
    image=login_icone)
login_texto.place(x=90, y=150)

# SENHA
senha_icone = PhotoImage(file='icons/senha.png')
senha_texto = Label(
    janela,
    text='Senha:',
    bg=f'{cor_fundo}',
    fg=f'{cor_letra}',
    font=f'{fonte}',
    image=senha_icone)
senha_texto.place(x=78, y=180)


# -Entry-
# USUARIO
user = Entry(janela)
user.insert(0, 'login')
user.place(x=130, y=154)

# SENHA
senha = Entry(janela, show='*')
senha.place(x=130, y=184)


# -Button-
# ENTRAR
entrar_icone = PhotoImage(file='icons/entrar.png')
entrar = Button(janela, image=entrar_icone, text='Entrar')
entrar.place(x=220, y=210)



janela.mainloop()
