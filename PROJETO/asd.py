from operator import itemgetter, attrgetter
from random import randint

class wukie:
    def __init__(self, indicie, carga):
        self.indice = indice
        self.carga = carga

    def __repr__(self):
        return repr([self.indice, self.carga])

def wookie_recebe(wk, carga):
    wk.append(carga)
    return True

def wookie_vazio(l_wk):
    if [] in l_wk:
        return True
    return False

def wookie_menor(carga, wk):
    if carga <= wk[-1]:
        return True
    return False

def separa_carga(l_wk, l_sobra, l_carga):
    for carga in l_carga:
        if wookie_vazio(l_wk):
            l_wk[l_wk.index([])].append(carga)
                
        else:
            for wk in l_wk:
                if wookie_menor(carga, wk):
                    wookie_recebe(wk, carga)
                    break
            else:
                wookie_recebe(l_sobra, carga)
    return l_wk, l_sobra


n = int(input())
l_sobra = list()
recebeu = bool()
l_wk = list()
for i in range(n):
    l_wk.append([])
    
l_carga = [int(x) for x in input().split()]

l_wk, l_sobra = separa_carga(l_wk, l_sobra, l_carga)




            
            
        
    
        



# while(l_carga != []):
#     recebeu = False
#     
#     for wk in l_wk:
#         if wk == [] or wk[-1] >= l_carga[0]:
#             recebeu = wookie_recebe(wk, l_carga)
#             
#     if not recebeu:
#         l_sobra.append(l_carga.pop(0))
#         
l_wk = sorted(l_wk, key=lambda x: sum(x), reverse=True)








if l_wk == []:
    print("Os Wookies foram para o lado sombrio da força!")
else:
    for i in range(len(l_wk)):
        if i == (len(l_wk)-1):
            print(l_wk[i])
        else:
            print(l_wk[i], end=" ")
        
if l_sobra == []:
    print("A força está com os Wookies!")
    
else:
    print(" ".join(str(x) for x in l_sobra))