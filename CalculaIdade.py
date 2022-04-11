def perguntaAlgumaCoisa():
    pergunta = input( "Digita alguma coisa: ")
    print("Você digitou: " + str(pergunta))

#perguntaAlgumaCoisa()

from datetime import datetime


def calcularIdade():
    print ("Qual ano que você nasceu?")
    dataNascimento = input()
    Idade = int(datetime.now().strftime("%Y")) - int(dataNascimento)
    
    print ("Sua idade é: " + str(Idade))
while(True):
    calcularIdade()


