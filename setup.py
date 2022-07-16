from random import randint
from os import system

system("clear")

# cores
red = '\033[03;31m' # Red
white = '\033[0;37m' # White
green = '\033[32m' # Green
orange = '\033[05;33m' # Orange
blue = '\033[05;34m' # blue
pink = '\033[0;35m' # pink

system("clear")
nome=input(green+"Qual o seu nome?\n"+white)

b=('#')*50
messagem='SEJA BEM VIND0+ nome'

print (orange+b+white+messagem+orange+b)

idade=int(input(green+'digite sua idade:\n'+white))

#obj
velh=int(50)
velho= idade > velh
novo= idade < velh
mode = idade == velh

#condiçoes
if (velho):
    print (red+'voce esta meio velho!')
elif (mode):
    print (white+'voce ta ficando velho!')
elif (nov0):
    print (green+'voce ainda é novo!')

peso=int(input(green+'digite seu peso:\n'+white))

#obj
G=int(85)
muitoG= peso >= G
magru= peso < G

#condiçoes
if (muitoG):
    print (red+'voce é gordo!')
else:
    print (white+'voce deve ser padrao!')

system("sleep 5s && clear")

print (green+"ola {} ,voce tem {} anos e seu peso é de {}kg \n ".format(nome,idade,peso))
print (b+'\nvamos começa o jogo de adivinhaçao\n'+b
#obj
N=int(randint(1,20))
tentativas=5
rodada = 0
T=0

for rodada in range(1,tentativas + 1):

    print (pink+"{} chance de {}".format(rodada,tentativas))

    adiv= int(input('adivinhe o numero secreto!!!\n-->'+orange))
    T +=1

    if  (N==adiv):
        print (green+"yeee , voce acertou!!")
        break

    elif (N > adiv):
        print (red+"voce errou,tente um numero mas alto!!!")
    elif (N < adiv):
        print (red+"voce errou , tente um numero mas baixo!!!")

print ("FIM DE JOG0")
print ("placar do jogo vc usou  %i chances de 5" % T)
