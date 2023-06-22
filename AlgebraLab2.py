import random


def rozlosujWektor():
    lista = []
    for i in range(0,7):
        for j in range(0,7):
            for k in range(0,7):
                x = (2*i + j + 5*k) % 7
                y = (4*i + 6 * k) % 7
                var = [i,j,k,x,y]
                if var in lista:
                    continue
                else:
                    lista.append(var)
    return lista
def Hamming(u,v):

    counter = 0
    for i in range(0,len(u)):
        if u[i] != v[i]:
            counter+=1
    return counter

def minimizehammingdistance(X, v, B):
    assert type(X) is list or type(v) is list
    P = [0,v]
    wart = 15
    for i in range (0,len(X)):
        z = Hamming(X[i],v)
        if z < wart:
            wart = z
            P[0] = i
    L = []
    for j in range(0, len(X)):
        if Hamming(X[j],v) == wart:
                L.append(X[j])
    index = random.randint(0,len(L)-1)
    z = L[index]
    wspolczynniki = [z[0], z[1], z[2]]

    return wspolczynniki, wart



def main():
    list = rozlosujWektor()
    for i in range(0,len(list)):
        print(list[i])
  #  print(list)
    B = [[1,0,0,2,4], [0,1,0,1,0], [0,0,1,5,6]]
    print("Dekodowanie wektora [0, 0, 2, 3, 5]")
    print("list - rozlosujWektor(), B- baza ")

    print("wektor = minimizehammingdistance(list,[0,0,2,3,5], B)")
    wektor, wart  = minimizehammingdistance(list,[0,0,2,3,5], B)
    print(wektor)
    print(wart)
if __name__ == '__main__':
    main()
