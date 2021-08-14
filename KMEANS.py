import numpy as np
import matplotlib.pyplot as plt
import math
'''
    Funciones creadas para poder ejecutar K-MEANS
'''
def centroides(k):
    i=0
    c=np.zeros((k,2))
    while(i<k):
        x=np.random.randint(49,80)
        y=np.random.randint(1,2)
        c[i,0]=x
        c[i,1]=y
        i+=1    
    return c

'''
    Calcula la distancia Euclidiana
'''

def DEuclidiana(c,X,k):
    cantidad=len(X[0][:])
    d=np.zeros((k,cantidad))    
    j=0
    while(j<k):
        i=0
        while(i<cantidad):
            dx=c[j][0]-X[0][i]     #distancia en x
            dy=c[j][1]-X[1][i]     #distancia en y
            d[j][i]=(math.sqrt(dx*dx+dy*dy))
            i+=1
        j+=1
    return d
'''
    Agrupar , la funcion agrupa los datos con sus centroides
'''

def Agrupar(k,X,c,dist):
       
    g1x=[]
    g1y=[]
    g2x=[]
    g2y=[]
    
    i=0
    while(i<len(X[0][:])):
        if(dist[0][i]<dist[1][i]):
            g1x.append(X[0][i])
            g1y.append(X[1][i])
        elif(dist[1][i]<dist[0][i]):
            g2x.append(X[0][i])
            g2y.append(X[1][i])
        i+=1
    
    return g1x,g1y,g2x,g2y


def newCen(grupos,k,c):
    c=np.zeros((2,k))
    j=0
    while(j<k):
        i=0
        while(i<2):
            if(j==1):
                c[j][i]=((np.sum(grupos[:][i+1+j]))/(len(grupos[:][i+1+j])))
            elif(j==0):
                c[j][i]=((np.sum(grupos[:][i+j]))/(len(grupos[:][i+j])))
            i+=1
        j+=1
    
    return c
def grafica1(X,c):
    cx=[c[0][0],c[1][0]]
    cy=[c[0][1],c[1][1]]
    plt.plot(X[0,:],X[1,:],'k.')
    plt.plot(cx,cy,'*')
    plt.show()
def grafica2(grupos,cn):
    plt.plot(grupos[:][0],grupos[:][1],"k.",color="red")
    plt.plot(grupos[:][2],grupos[:][3],'k.',color="blue")
    plt.plot(cn[0][0],cn[0][1],'*',color="red")
    plt.plot(cn[1][0],cn[1][1],'*',color="blue")
    plt.show()

def kmeans(k,X,maxIter):
    c=centroides(k) #primer centroide al azar
    grafica1(X,c) #grafica con centroides y datos sin clasificar
    error=1000
    i=0
    while(i<maxIter and error>0.00001):
        dist=DEuclidiana(c,X,k) #calcula las distancais de los centroides a todos los puntos
        grupos=Agrupar(k,X,c,dist) #agrupo datos con centroides por minima distancia
        cn=newCen(grupos,k,c)  #calculo los nuevos centroides
        error=abs(max((sum(c)-sum(cn))/(sum(c)))) #calcula el maximo error entre centroides
        print("Error : "+str(error))
        grafica2(grupos,cn) #grafica con centroides y datos clasificados
        i+=1
        c=cn