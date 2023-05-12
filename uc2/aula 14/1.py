from customtkinter import *



app = CTk()
app.title ("Teste")
largura = 800
altura = 600
app.geometry(f"{largura}x{altura}")
app.grid_columnconfigure((0),weight=1)

def cliqueInserir():
    texto = inserirTexto.get()
    corpoDoTexto.configure(text = texto)
    



tituloTopo = CTkLabel(master=app, text= "Ola Mundo", text_color="blue", font=CTkFont(size=50, weight="bold"))
tituloTopo.grid(row = 0, column = 0 , padx = 20, pady = 20)
corpoDoTexto = CTkLabel(master=app, text="Teste de Programa", font=CTkFont(size=36))
corpoDoTexto.grid(row = 1,column = 1,padx = 20, pady = 20)


inserirTexto = CTkEntry(master=app, placeholder_text="Digite uma mensagem: ")
inserirTexto.grid(row = 2,column = 0 , padx = 20 , pady = 20)

inserirBotao = CTkButton(master=app,bg_color="red", text="Enviar", command=cliqueInserir)
inserirBotao.grid(row = 3, column = 1,padx = 20, pady = 20)


app.mainloop()