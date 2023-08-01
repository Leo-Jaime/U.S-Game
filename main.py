import  turtle

screen = turtle.Screen()
screen.title("U.S States Game")
imagem = "blank_states_img.gif"
screen.setup(width=750, height=600)
screen.addshape(imagem)
turtle.shape(imagem)

screen.textinput(title="Digite um Estado", prompt="Digite um Estado aqui")


screen.exitonclick()