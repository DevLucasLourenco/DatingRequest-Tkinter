import tkinter as tk
import random
import turtle
from PIL import ImageTk, Image


class UcToday(tk.Tk):

    def __init__(self):
        TurtleHeart()
        
        super().__init__()

        self.title('Dating Request by Lucas Lourenço')  
        self.geometry('1000x600')
        self.resizable(False, False)
        
        self.background_image = tk.PhotoImage(file='bg.png')

        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        self.label = tk.Label(self, text='Namora comigo? rs', font=('Arial', 20, 'bold'), bg='pink', relief='solid')
        self.label.pack(side='top', pady=50)

        
        self.label_aguarde = tk.Label(self, text='By Lucas Lourenco\n@lucaslourencoo__', font=('Arial', 7, 'bold'), bg='black', fg='white')
        self.label_aguarde.pack(side='right', pady=10)

        self.botao_sim = tk.Button(self, text='Claro, gatinho', font=('Arial', 16, 'bold'), bg='red', fg='white', command=self._clicando_sim, width=12, height=2)
        self.botao_sim.pack(side='left', padx=50)

        self.botao_nao = tk.Button(self, text='Não', font=('Arial', 16, 'bold'), bg='red', fg='white', width=12, height=2)
        self.botao_nao.pack(side='right', padx=50)

        self.botao_nao.bind("<Enter>", self._proximidade_ao_nao)


    def _proximidade_ao_nao(self, event):
        self.botao_nao.place(x=random.randint(0, 800), y=random.randint(0, 550))
        

    
    def _clicando_sim(self):        
        self.label_aguarde = tk.Label(self, text='Aguarde...', font=('Arial', 20, 'bold'), bg='pink')
        
        nova_janela = NovaJanela(self)
        nova_janela.wait_window()



class TurtleHeart():

    def __init__(self) -> None:

        screen = turtle.Screen()
        screen.bgcolor("#800000")
        screen.title("rsrs")


        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("red")
        pen.pensize(5)
        pen.speed(0)
        pen.penup()
        pen.goto(0, -200)
        pen.pendown()

        
        pen.begin_fill()
        pen.left(140)
        pen.forward(180)
        pen.circle(-90, 200)
        pen.setheading(60)
        pen.circle(-90, 200)
        pen.forward(180)
        pen.end_fill()

        
        pen.penup()
        pen.goto(0, 100)
        pen.color("white")
        pen.write("Bem vinda, amor!", align="center", font=("Arial", 30, "bold"))

        pen.goto(0, -100)
        pen.write("OBS.: Clique no coração", align="center", font=("Arial", 10, "bold"))
        turtle.exitonclick()



class NovaJanela(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title('rsrsrs')
        self.geometry('800x600')
        self.resizable(False, False)

        self.img = ImageTk.PhotoImage(Image.open("sfd.png"))
        self.imagem_fundo_label = tk.Label(self, image=self.img)
        self.imagem_fundo_label.place(x=0, y=0, relwidth=1, relheight=1)



app = UcToday()
app.mainloop()
