#Adriano Siqueira - 06-13-21 - Semana 6 - Tarefa de programação: Programa completo - Jogo do NIM

#RESOLVER SCORE DO CAMPEONATO
#ACERTAR JOGADAS DO COMPUTADOR
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
   
    if m >= n or not type(n) == int or type(m) == int:
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
                    if (n > 0):
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
                    if (n > 0):
                        print("usuario venceu");
                else:
                    print("Computador venceu");

    #aqui fica o looping (laço) do game (turno de cada um)
    #if(n <= 0):
    #    print("Fim do jogo! O computador ganhou!");
    #    score(1, 0);
    #else:        
    #    usuario_escolhe_jogada(n, m); 
    #**********************************************************
    #    if(n <= 0):
    #    print("O Jogador venceu! - FALHA NO ALGORITMO!!!");
    #    score(0, 1);
    #else:
    #    computador_escolhe_jogada(n, m); 
        
def campeonato():
    print("\n**** Rodada 1 ****\n");
    partida();
    print("\n**** Rodada 2 ****\n");
    partida();
    print("\n**** Rodada 3 ****\n");
    partida();
    print(score(0, 0));
    
def computador_escolhe_jogada(n, m):
    if(n >= m):
        if n % (m + 1) == 0:
            retC = n % m + 1;
        else:
            retC = m;
    else:
        retC = n        

    n -= retC;
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