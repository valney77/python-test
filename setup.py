from random import randint
import os
import  sys


os.system("clear")

# cores
red = '\033[03;31m' # Red
white = '\033[0;37m' # White
green = '\033[32m' # Green
orange = '\033[05;33m' # Orange
blue = '\033[05;34m' # blue
pink = '\033[0;35m' # pink


os.system("uname -a")
nome=input("Qual o seu nome?\n"+blue)

b=('★')*41
messagem='★SEJA BEM V1ND0 '+nome+ '  4 4ul4 D PR0GR4M4Ç40★'
print (red+b)
print (messagem)
print (b)

idade=int(input(green+'digite sua idade:\n'+blue))

velho='40'
velh=int(velho)


velh0= idade > velh
nov0= idade < velh
mode = idade == velh


if (velh0):
    print (red+'voce esta meio velho!')
elif (mode):
    print (white+'voce esta na idade padrao!')
elif (nov0):
    print (blue+'voce ainda é novo!')
peso=int(input(green+'digite seu peso:\n'+blue))
gordo='90'
G=int(gordo)
muitoG= peso >= G
magru= peso < G

if (muitoG):
    print (red+'voce é gordo!')
else:
    print (white+'voce dev ser belico!')

os.system("clear")

SIT="ola {} ,voce tem {} anos e seu peso é de {}kg \n ".format(nome,idade,peso)

print (pink+SIT.upper())
N=int(randint(1,20))
tentativas=5
rodada = 0
T=0


#while (rodada <= tentativas):



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

   # rodada = rodada + 1


#x=1,234 print('{:.2f}'.format(x))  



#zona d test
TEST='ZRR'
TEST.upper()#retorna caracteres maíusculo
TEST.capitalize()#retorna caractereres minú

   #estes valores func fora de parenteses
bool(2==2) #valores booleano
bool(3>2)#verdadeiro
