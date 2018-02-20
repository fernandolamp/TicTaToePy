import os

jogada = {'x00':" ",'x01':" ",'x02':" ",'x10':" ",'x11':" ",'x12':" ",'x20':" ",'x21':" ",'x22':" "}

def clear():
    # Clear Windows command prompt.
    if (os.name in ('ce', 'nt', 'dos')):
        os.system('cls')
    # Clear the Linux terminal.
    elif ('posix' in os.name):
        os.system('clear')


def print_board():
    clear()
    #      0 1 2
    print("   y0  y1  y2") 
    print("x0  {}' {} '{}".format(jogada['x00'], jogada['x01'], jogada['x02'] ))#0
    print("  ----------")
    print("x1  {}' {} '{}".format(jogada['x10'], jogada['x11'], jogada['x12']))
    print("  ----------")
    print("x2  {}' {} '{}".format(jogada['x20'], jogada['x21'], jogada['x22']))#4

def check_winner():
    # x00 x01 x02
    # x10 x11 x12
    # x20 x21 x22
    linha = []
    coluna =[]
    matriz =[]
    for x in range(0,3):               
        for y in range(0,3):        
            key = 'x{}{}'.format(x,y)
            linha.append(jogada[key])
        #verifica linha 
        if (linha[0] != ' ') and (linha[0] == linha [1] == linha[2]):
            return True            
        matriz.append(linha)                
        linha=[]
    for x in range (0,3):
        for y in range(0,3):
            coluna.append(matriz[y][x])
        if (coluna[0] != ' ' and coluna[0] == coluna[1] == coluna[2]):
            return True                
        coluna = []
    #verifica as diagonais
    return (matriz[0][1] != ' ' and matriz[0][1] == matriz[1][1] == matriz[2][2])  or ( matriz[0][2] != ' ' and matriz[0][2] == matriz[1][1] == matriz[2][0])

def check_draw():
    empatou =  not (" " in jogada.values())
    if empatou:
       print("Empatou!")
    return empatou  

ultima_jogada = ''
while (not check_winner()) and (not check_draw()):
    print_board()
    cordenada =  input("Entre com o a coordenada no formato xy: ")
    print(cordenada)        

    if jogada['x{}{}'.format(cordenada[0],cordenada[1])] != ' ':
        print("Jogada Invalida, essa coordenada ja foi usada")
        continue    
    
    entry = input("Entre com o seu valor (x ou O): ")
    jogada['x{}{}'.format(cordenada[0],cordenada[1])] = entry

print_board()

print("Fim")