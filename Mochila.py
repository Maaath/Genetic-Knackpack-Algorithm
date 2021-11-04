
class Mochila():

    def __init__(self,lista,capacidade): #recebe os itens e a capacidade máxima da mochila
        self.lista=lista
        self.capacidade=capacidade
        self.ops=0
        self.itens=[ False ]*len(lista) #soluções da mochila


    def solve(self):
        n=len(self.lista)
        W=self.capacidade
        V=[[0]*(W+1) for i in range(n+1)] #Inicia Matriz n x W com 0
        tabela_troca=[[False]*(W+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,W+1):
                pesoI=self.lista[i-1]['peso']
                if pesoI>j: #Se o item i pesar mais que a coluna de capacidade mantem valor do item anterior
                    V[i][j]=V[i-1][j]
                    self.ops+=1
                else: #caso contrario pega o maior valor entre os valores removendo o item anterior e o seu peso e adicionando item i e seu valor ao valor anterior
                    V[i][j]=max(V[i-1][j-pesoI]+self.lista[i-1]['valor'],V[i-1][j])
                    if V[i-1][j-pesoI]+self.lista[i-1]['valor'] > V[i-1][j]:
                        tabela_troca[i][j]=True
                    self.ops+=1
        w=W
        for i in range(n,0,-1):
            if tabela_troca[i][w]:
                self.itens[i-1]=True
                w-=self.lista[i-1]['peso']
            else:
                self.itens[i-1]=False
        return V

def mochila_main(itens,peso): #fazendo a conversão de uma matriz para uma lista de dicionário

    itens_aux = []
    for i in range(0, len(itens)):
        itens_aux.append({'item': (i + 1), 'peso': itens[i][0], 'valor': itens[i][1]})

    mochila = Mochila(itens_aux, peso)

    return(mochila.solve()[-1][-1])



