from tkinter import *


janela = Tk()
janela.title('Login')  # Titulo da janela.
janela.geometry('350x450+400+50')  # Dimensão da janela e onde ela "Nasce".
# janela.iconbitmap('icons/icon_janela/icone.ico')
janela.resizable(0, 0)  # JANELA TRAVADA.
# janela.state('zoomed')  # O programa já abre em tela cheia
#janela.config(background="#000") # cor de fundo


# FUNDO COM CANVAS
#Label(janela, image=fundo_noite).place(relheight=1, relwidth=1)
frame = Frame(janela)
frame.place(x=0, y=0, relwidth=1, relheight=1)

canvas = Canvas(frame, bg="#000", width=350, height=450, relief=RAISED)
canvas.place(x=-2, y=0)

fundo_noite = PhotoImage(file='icons/bg/noite.png')
canvas.create_image(175,224,image=fundo_noite)


# -Estilos-
# Texto Label
cor_letra = '#000'
cor_fundo = '#EEEEEE'
fonte = 'Calibri'


# NOME USER
login_icone = PhotoImage(file='icons/user.png')
canvas.create_image(111,161,image=login_icone)

# SENHA
senha_icone = PhotoImage(file='icons/senha.png')
canvas.create_image(110,192,image=senha_icone)


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


# BEM-VINDO
canvas.create_text(
    180,320,fill="#f2f2f2",font="Trevor 20", text="BEM-VINDO")


janela.mainloop()
