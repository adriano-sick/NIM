#Adriano Siqueira - 06-13-21 - Semana 6 - Tarefa de programação: Programa completo - Jogo do NIM

#TRATAR POSSIVEIS ERROS DE ENTRADA DO USUARIO EM n, E m



def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n");
    print("1 - para jogar uma partida isolada");
    m1 = input("2 - para jogar um campeonato ");

    if (m1 == "1"):
        print("\nVoce escolheu uma partida!\n");
        partida();
    elif (m1 == "2"):
        print("\nVoce escolheu um campeonato!");
        campeonato();
    else:
        main();




def partida():    
    n = input("Quantas peças? ");
    m = input("Limite de peças por jogada? ");

    while not(n.isdigit() and m.isdigit()):
        print("\nInsira um NÚMERO!!!")
        n = input("Quantas peças? ");
        m = input("Limite de peças por jogada? ");
    else:
        n = int(n);
        m = int(m);

    if m > n:
        partida();

    else:
        if n % (m + 1) == 0:
            print("\nVocê começa!\n");
            while (n > 0):
                n -= usuario_escolhe_jogada(n, m);
                pecas_rest(n);

                if (n > 0):
                    n -= computador_escolhe_jogada(n, m);
                    pecas_rest(n);

                    if (n <= 0):
                        print ("Fim do jogo! O computador ganhou!");
                        break
                else:
                    print("Fim do jogo! Você ganhou!");

        else:
            print("\nComputador começa!");
            while (n > 0):
                n -= computador_escolhe_jogada(n, m);
                pecas_rest(n);

                if (n > 0):
                    n -= usuario_escolhe_jogada(n, m);
                    pecas_rest(n);

                    if (n <= 0):
                        print("Fim do jogo! Você ganhou!");
                else:
                    print("Fim do jogo! O computador ganhou!");
                    break
        
def campeonato():
    print("\n**** Rodada 1 ****\n");
    partida();
    print("\n**** Rodada 2 ****\n");
    partida();
    print("\n**** Rodada 3 ****\n");
    partida();
    print("\n**** Final do campeonato! ****\n");
    print("Placar: Você 0 X 3 Computador");
    
def computador_escolhe_jogada(n, m):
    retC = 1

    while retC != m:
        if (n - retC) % (m + 1) == 0:
            if retC != 1:
                print("\nO computador tirou", retC, "peças.");
            else:
                print("\nO computador tirou uma peça.");
            return retC;
        else:
            retC += 1;
            
    if retC != 1:
        print("\nO computador tirou", retC, "peças.");
    else:
        print("\nO computador tirou uma peça.");
    
    return retC;    
    
def usuario_escolhe_jogada(n, m):
    retP = int(input("Quantas peças você vai tirar? "));
    while(retP > m or retP <= 0 or n < retP):
        retP = 0;
        print("\nOops! Jogada inválida! Tente de novo.\n");
        retP = int(input("Quantas peças você vai tirar? "));

    if retP != 1:
        print("Você tirou", retP, "peças.");
    else:
        print("\nVocê tirou uma peça.");
        
    n -= retP;
    return retP

def pecas_rest(n):
    if (n != 1):
        if(n > 0):
            print("Agora restam", n, "peças no tabuleiro.\n");
        else:
            return;
    else:
        print("Agora resta apenas uma peça no tabuleiro.");

#main();
