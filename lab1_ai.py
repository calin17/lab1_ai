# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import collections

def pb_2_lab1(a,b,c,d):
    """Calculeza distanta intre doua punte
          -a x pt prinul punct
          -b y pt punctul punct
          -c x pt prinul al doilea
          -d y pt punctul al doilea
        :return distanta dintre cele 2 puncte"""
    dist=math.sqrt(((a-c) * (a-c)) + ((b-d) * (b-d)))
    return dist


def pb_4_lab1(cuvinte):
    """Returneaza un string care contine cuvintele care apar o singura data
         :parameter cuvinte :vector de cuvinte
         return :elm(string de cuvinte)

          """
    elm=""
    cuv = cuvinte.split()
    frecvente = collections.Counter(cuv)
    for (key, value) in frecvente.items():
        if(value==1):
             elm=elm+key+" "
    return elm

def pb_1_lab1(t):
    """Calculeza ultimul cuv dnpdv lexicogrtafic
       retuneaza ultp
          """
    cmax=""
    cuvinete=t.split()
    for cuvant in cuvinete:
        if cuvant>cmax:
            cmax=cuvant
    return cmax

def pb_3_lab1(vect1,vect2):
    """Returneaza produsul vectorial a doi vectori
         :parameter vect1 :sir de numere
        :parameter vect2 :sir de numere
         return pr
          """
    p=int(0)
    for a, b in zip(vect1, vect2):
        p=p+a*b

    return p
def pb_5_lab1(vect):
    """Returneaza elementul care apare de 2 ori
         :parameter vect :sir de numere
         return elm cu fr 2

          """
    frecvente = collections.Counter(vect)
    for (key, value) in frecvente.items():
        if(value==2):
             elm=key
    return elm

def pb_7_lab1(vect,k):
    """Gaseste al k cel mai mare element
         :parameter vect :vector de numere

          """
    vect.sort()
    inv = vect[::-1]
    return inv[k-1]

def pb_8_lab1(n):
    """Retuneaza o lista cu numerele de la i la n in rep binara
         :parameter n :numar intreg
         :return:un string cu numerele
          """
    rez=""
    for i in range(1, n + 1):
       num=""
       i=int(i)
       while i!=0:
           st=str(i%2)
           num=num+st
           i=i//2
       rez=rez+num[::-1]+" "

    return rez

def pb_6_lab1(vect):
    """Returneaza elemnentul majoritar ar sirului
         :parameter vect :sir de numere
         return elm:int

          """

    frecvente = collections.Counter(vect)
    elm=int(0)
    for (key, value) in frecvente.items():
        if(value>len(vect)/2):
             elm=key
    if(elm==0):
        return "Nu exista un astfel de numar"
    else:
        return elm


def pb_9_lab1(mat,lst):
    """Determinarea sumei a unor portiuni din matrice
         :parameter mat :matrice
         :parameter lst:vector
         return rez:string

          """
    st=""
    for perechi in lst:
        v=perechi.split()
        su=int(0)
        p = int(v[0])
        q=int(v[1])
        r=int(v[2])
        s=int(v[3])
        for i in range(p,r+1):
            for j in range(q,s+1):
                    su=su+int(mat[i][j])
        st=st+str(su)+" "

    return st

def pb_10_lab1(mat):
    """Determina indexul liniei cu cele mai multe elemente egale cu 1
         :parameter mat :matrice
         return ind:int

          """
    m=int(0)
    ind=0
    for i in range(0,len(mat)):
        nr=int(0)
        for j in mat[i][::-1]:
            if(j==1):
                nr=nr+1
            else:
                break

        if(nr>m):
            ind=i
            m=nr

    return ind





def pb_2_lab1_test():
    """Testeza pb2_lab1
    """
    assert pb_2_lab1(int(1), int(5), int(4), int(1))==5.0
    assert pb_2_lab1(int(0), int(0), int(0), int(0)) == 0

def pb_5_lab1_test():
    """Testeza pb5_lab1
    """
    assert pb_5_lab1([2,4,5,6,7,8,9,10,4])==4
    assert pb_5_lab1([2, 4, 5, 6, 7, 8, 9, 10, 10]) == 10
    assert pb_5_lab1([2, 4, 5, 6, 7,22,45,45,90]) != 2
    assert pb_5_lab1([1,5,7,8,9,2,5]) == 5

def pb_6_lab1_test():
    """Testeza pb6_lab1
    """
    assert pb_6_lab1([2,4,2,6,2,8,2,10,2])==2
    assert pb_6_lab1([2, 4, 5, 6, 7, 8, 9, 10, 10]) =="Nu exista un astfel de numar"
    assert pb_6_lab1([1,4,4,5,4]) ==4




def pb_1_lab1_test():
    """Testeza pb2_lab1
    """
    assert  pb_1_lab1("Ana are mere rosii si galbene")=="si"
    assert  pb_1_lab1("Ana bre")=="bre"

def pb_3_lab1_test():
    """Testeza pb3_lab1
    """
    assert pb_3_lab1([1,0,3,0],[1,0,0,2])==1
    try:
        assert pb_3_lab1([10,0,0,6,0,3],[2,3,0,1,4,0]) ==2
    except:
        print("Am ajuns in except")
    assert pb_3_lab1([2, 0,4],[3,0,1]) == 10



def pb_4_lab1_test():
    """Testeza pb4_lab1
    """
    assert  pb_4_lab1("ana mere rosii pere mere ana")=="rosii pere "
    assert  pb_4_lab1("Ana ana bere bere")=="Ana ana "
    assert pb_4_lab1("ana mere rosii pere mere") != "rosii pere "

def pb_7_lab1_test():
    """Testeza pb7_lab1
    """
    assert pb_7_lab1([2,4,5,6,7,8,9,10],int(2))==9
    assert pb_7_lab1([10,4,5,6,1,3],int(3)) ==5
    assert pb_7_lab1([2, 4, 5, 6, 7,22,45,45,90],int(1)) != 45
    assert pb_7_lab1([1,5,7,8,9,2,5],int(1)) == 9


def pb_8_lab1_test():
    """Testeza pb8_lab1
    """
    assert pb_8_lab1(int(4))=="1 10 11 100 "
    assert pb_8_lab1(3) =="1 10 11 "
    try:
       assert pb_7_lab1(4) =="1 10"
    except:
        print("Am ajuns in except in pb8")

def pb_10_lab1_test():
    """Testeza pb10_lab1
    """
    assert pb_10_lab1([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]])==1
    assert pb_10_lab1([[1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]])==0
    try:
        assert pb_10_lab1([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]) == 0
    except:
        print("Am ajuns in exept pt pb10")

def pb_9_lab1_test():
    """Testeza pb9_lab1
    """
    assert pb_9_lab1([[0,2,5,4,1], [4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]],["1 1 3 3","2 2 4 4"])=="38 44 "
    assert pb_9_lab1([[0,2,5,4,1], [4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]],["1 1 2 2"])=="17 "
    try:
        assert pb_9_lab1([[0,2,5,4,1], [4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]],["1 1 3 3","2 2 4 4"]) =="28 42 "
    except:
        print("Am ajuns in exept pt pb9")


if __name__ == '__main__':

    pb_2_lab1_test()
    pb_1_lab1_test()
    print(pb_1_lab1("Ana are mere rosii si galbene"))
    dist=pb_2_lab1(int(1),int(5),int(4),int(1))
    print(dist)
    v = [1,2,3,4,2]
    print(pb_5_lab1(v))
    pb_5_lab1_test()

    print(pb_4_lab1("ana are ana are mere rosii ana"))
    pb_4_lab1_test()

    ve = [7,4,6,3,9,1]
    print(pb_7_lab1(ve,int(2)))
    pb_7_lab1_test()

    v2 = [2,8,7,2,2,5,2,3,1,2,2]
    print(pb_6_lab1(v2))
    pb_6_lab1_test()

    s1= [1,0,2,0,3]
    s2=[1,2,0,3,1]
    print(pb_3_lab1(s1,s2))
    pb_3_lab1_test()

    print(pb_8_lab1(4))
    pb_8_lab1_test()

    m = [[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
    print(pb_10_lab1(m))
    pb_10_lab1_test()

    m2 = [[0,2,5,4,1], [4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]]
    l=["1 1 3 3","2 2 4 4"]
    print(pb_9_lab1(m2,l))
    pb_9_lab1_test()










