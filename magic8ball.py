
from random import randint
from time import sleep

from colorama import Fore, Style

# lista de respostas..
resposta = [
    "certamente",
    "difícil de dizer",
    "sem duvida",
    "Absolutamente,Sim",
    "você pode contar com isso",
    "na minha opinião,Sim",
    "provavelmente",
    "perspectiva boa",
    "Sim",
    "Sinais apontam que sim",
    "Muito possivelmente",
    "Me pergunte depois",
    "melhor não te dizer agora",
    "não posso prever agora",
    "Concentre-se e pergunte denovo",
    "não conte com isso",
    "Minha resposta é não",
    "Minhas fontes dizem que não",
    "perspectiva não é tão boa",
    "muito duvidoso "]


#jogo...
def jogo():
    input("qual sua pergunta? ")
    print("pensando...")
    sleep(1)
    idx = randint(0, 20)
    if idx < 10:
        cor = Fore.GREEN
    elif idx >= 10 and idx < 15:
        cor = Fore.YELLOW
    else:
        cor = Fore.RED
    print(cor + resposta[idx] + Style.RESET_ALL )
    loop()


#função do loop...
def loop():
    continuar = str(input("Gostaria de perguntar novamente?(S/N): ")).lower()
    if(continuar == 's'):
        jogo()

    elif(continuar == 'n'):
      sair = randint(0,2)  
      if(sair == 0 ):
        print("tchau tchau")
      elif(sair == 1):
        print("até logo")
      else:
        print("bye bye")  
    else:
        print("valor invalido")
        loop()


if(__name__ == '__main__'):
  jogo()
