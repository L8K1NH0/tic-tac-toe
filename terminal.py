posicao = [ 1, 2, 3,
            4, 5, 6,
            7, 8, 9]


def VerificarReta(ranger,jogador): # verificar uma reta especifica foi concluida
    cont = 0 
    for i in ranger:#loop ajustado para cada reta

        if (posicao[i] == jogador): # comparando conteudo da posicao informada
            cont += 1 # quantidade de 'X' ou 'O' que tem, em uma reta
            if(cont == 3): #caso tenha 3 'X' ou 'O'  em um linha, significa que ganhou
                print(f"O jogador '{jogador}' Ganhou!! ")
                return False
            
def Verificar(jogador): # verificar se alguma reta foi concluida

    #*Caso seja retornado False, que diser que alguma reta foi concluida, assim fecha o loop
     
    #* VERIFICAR NA HORIZONTAL
    if( VerificarReta(range(3),jogador) == False ) : return False

    elif( VerificarReta(range(3,6),jogador) == False ) : return False

    elif( VerificarReta(range(6,9),jogador) == False ) : return False

    #* VERIFICAR NA VERTICAL
    if( VerificarReta(range(0,9,3),jogador) == False ) : return False

    elif( VerificarReta(range(1,8,3),jogador) == False ) : return False

    elif( VerificarReta(range(2,9,3),jogador) == False ) : return False
    
    #* VERIFICAR NA DIAGONAL
    if( VerificarReta(range(0,9,4),jogador) == False ) : return False

    elif( VerificarReta(range(2,7,2),jogador) == False ) : return False

    velha = 0
    for num in posicao : #Verificar se chegou ao final == velha
        if( type(num) == int ):
            velha += 1            
        
    if(velha == 0): # caso a variavel "velha" seja maior que 0, significa que ainda ha posições para serem escolhidas
        print("!!_DEU_VELHA_!!")
        return False

    
    return True

def Tabela():
    print('\n\n{:*^19}'.format('-'))
    print(posicao[:3])
    print(posicao[3:6])
    print(posicao[6:])
    print('{:*^19}'.format('-'))

def Vez(jogador):
    x = int(input(f"Vez do {jogador}\nDigite a posição: "))

    if (posicao.count(x) == 0):
        raise ValueError('\nPosição Invalida!\nPerdeu a vez...\n')

    posicaoEscolhida =  posicao.index(x)
    posicao[posicaoEscolhida] = jogador

    Tabela()

Tabela()

while True :
    try:
        #*X*#
        Vez('X')
        if (Verificar("X") == False):
            break

        #*O*#
        Vez('O')
        if (Verificar("O") == False): 
            break    

    except ValueError as e:
        print(e)

print('{:*^19}'.format('FIM'))