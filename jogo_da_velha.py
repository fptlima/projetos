#Criar cerquilha -> #
def jogo():
    print("_",casa[1],"_|_",casa[2],"_|_",casa[3],"_")
    print("_",casa[4],"_|_",casa[5],"_|_",casa[6],"_")
    print(" ",casa[7]," | ",casa[8]," | ",casa[9],"")

#definindo a casa onde cada player vai jogar
def play(player,x):
            n = 0
            while n == 0:
                print("Vez do",player ,end="") 
                position = int(input(", escolha uma casa (1 até 9):"))
                if position <= 9 and position >= 1:
                    if casa[position] == " ":
                        casa[position] = x 
                        n = 1
                elif  position > 9 or position < 1:
                     print("Digite um valor entre 1 e 9")
                
                else:
                    print("Essa casa já foi escolhida, tente outro número") 

#definindo o campeão
def winner(player, x):
    if (casa[1] == x and casa[2] == x and casa[3] == x) or (casa[4] == x and casa[5] == x and casa[6] == x) or (casa[7] == x and casa[8] == x and casa[9] == x) or (casa[1] == x and casa[4] == x and casa[7] == x) or (casa[2] == x and casa[5] == x and casa[8] == x) or (casa[3] == x and casa[6] == x and casa[9]== x) or (casa[1] == x and casa[5] == x and casa[7]== x) or (casa[1] == x and casa[5] == x and casa[9] == x):
        win = player
        if win == player1 or win == player2:
            jogo()
            print("Jogador",win,"venceu!",end='')
            return True
        else:
            jogo()
            print("Deu velha isso aqui 🥺",end='')

# repetir até os jogadores não quiserem mais jogar
n = 0
casa = [" "," "," "," "," "," "," "," "," "," "]
while n == 0:

    #meu principal
    print("-="*33)
    print("-="*8,"Seja bem-vindo ao jogo da velha!","=-"*8)
    print("Ele é especial para mim, pois criei ele sozinho, sem nenhum google")
    print("-="*33)
    player1 = str(input("Digite o nome do player 1: "))
    print("Seja bem- vindo", player1, "você jogará com 'O'.")
    player2 = str(input("Digite o nome do player 2: " ))
    print("Seja bem- vindo", player2, "você jogará com 'X'.\n\n -=Start The Game=-")
    
    # definindo as rodadas
    for x in range(8):
        jogo() 
        if x % 2 == 0:
            play(player1,"O")
            if winner(player1,"O") == True:
                break           
        else:
            play(player2,"X")             
            if winner(player2,"X") == True: 
                break
    n = int(input("mais uma partida? (1)Sim /(2)Não:"))

#fim                   