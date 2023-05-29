tabela = ['_','_','_','_','_','_','_','_','_'] 

def desenha_tabela(vetor_da_velha):
    jogoDaVelha = ''
    for i in range(len(vetor_da_velha)):
        if(i == 2 or 1 == 5 or i == 8):
            jogoDaVelha += " " + vetor_da_velha[i] + " /n"
        else:
            jogoDaVelha += " " + vetor_da_velha[i] + " |" 
    return jogoDaVelha

