from KMEANS import *
print ('Proyecto de Clasificacion de fruta con algoritmo Kmeans')

x1=np.array([[49],[1.43]]) # ninos
x2=np.array([[51],[1.55]])
x3=np.array([[57],[1.58]])
x4=np.array([[47],[1.55]])
x5=np.array([[54],[1.60]])
x6=np.array([[56],[1.58]])
x7=np.array([[59],[1.64]])
x8=np.array([[53],[1.61]])
x9=np.array([[58],[1.63]])
x10=np.array([[52],[1.60]]) # adultos
x11=np.array([[75],[1.73]])
x12=np.array([[80],[1.75]])
x13=np.array([[75],[1.69]])
x14=np.array([[65],[1.71]])
x15=np.array([[75],[1.79]])
x16=np.array([[77],[1.76]])
x17=np.array([[65],[1.71]])
x18=np.array([[70],[1.70]])
x19=np.array([[78],[1.81]])
x20=np.array([[70],[1.67]])

X=np.concatenate((x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20),axis=1)
k=2
maxIter=10
kmeans(k,X,maxIter)

