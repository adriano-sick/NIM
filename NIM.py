#Adriano Siqueira - 06-13-21 - Semana 6 - Tarefa de programação: Programa completo - Jogo do NIM

#RESOLVER SCORE DO CAMPEONATO
#ACERTAR JOGADAS DO COMPUTADOR
#TRATAR POSSIVEIS ERROS DE ENTRADA DO USUARIO EM n, E m



def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n");
    print("1 - para jogar uma partida isolada");
    m1 = input("2 - para jogar um campeonato ");

    if (m1 == "1"):
        print("\nVoce escolheu uma partida!\n");
        partida();
    elif (m1 == "2"):
        print("\nVoce escolheu um campeonato!\n");
        campeonato();
    else:
        main();




def partida():    
    n = int(input("Quantas peças? "));
    m = int(input("Limite de peças por jogada? "));
   
    if m >= n:
        partida();

    else:
        if n % (m + 1) == 0:
            print("Você começa!");
            while (n > 0):
                n -= usuario_escolhe_jogada(n, m);
                print("Agora restam", n, "peças no tabuleiro.");
                if (n > 0):
                    n -= computador_escolhe_jogada(n, m);
                    print("Agora restam", n, "peças no tabuleiro.");
                    if (n <= 0):
                        print ("computador venceu");
                else:
                    print("jogador venceu");

        else:
            print("Computador começa!");
            while (n > 0):
                n -= computador_escolhe_jogada(n, m);  
                print("Agora restam", n, "peças no tabuleiro.");
                if (n > 0):
                    n -= usuario_escolhe_jogada(n, m);
                    print("Agora restam", n, "peças no tabuleiro.");
                    if (n <= 0):
                        print("usuario venceu");
                else:
                    print("Computador venceu");
        
def campeonato():
    print("\n**** Rodada 1 ****\n");
    partida();
    print("\n**** Rodada 2 ****\n");
    partida();
    print("\n**** Rodada 3 ****\n");
    partida();
    print("\n**** Rodada 3 ****\n");
    
def computador_escolhe_jogada(n, m):
    retC = 1

    while retC != m:
        if (n - retC) % (m + 1) == 0:
            print("O computador tirou", retC, "peças.");
            return retC

        else:
            retC += 1
 
    print("O computador tirou", retC, "peças."); 
    return retC
    
def usuario_escolhe_jogada(n, m):
    retP = int(input("Quantas peças você vai tirar? "));
    if (retP <= m):
        n -= retP;
    else:
        usuario_escolhe_jogada(n, m);

    return retP


main();