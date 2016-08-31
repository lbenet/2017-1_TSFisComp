# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
from pylab import *w
from mpl_toolkits.mplot3d import Axes3D

def eigenvalores(a,b,c,d):
   return  linalg.eig(array([[a,b],[c,d]]))

def CampoPend(f):
    figure(figsize=(15,15))
    for i in arange(-10,10,1):
        for j in arange(-10,10,1):
            x=[i,j]
            y=f(x)
            
            quiver(i,j,y[0],y[1],width=0.001,scale=100,headlength=7)
         
    show()
        
def OsciladorArmonico(x):
    k=2
    y1=x[1]
    y2=-k*x[0]
    return [y1,y2]

def OsciladorAmortiguado(x):
    k=1
    B=1
    y1=x[1]
    y2=-k*x[0]-B*x[1]
    return [y1,y2]

def funcion(x):
    y1=3*x[0]+x[1]
    y2=x[0]-x[1]
    return [y1,y2]
    
def funcion1(x):
    y1=2*x[0]*x[1]
    y2=(x[1]**2)-(x[0]**2)
    return [y1,y2]    
    
def funcion2(x):
    y1=-2*x[0]+2*(x[0])**2
    y2=3*x[0]+x[1]+3*x[0]*x[1]
    return [y1,y2]
    
    
def funcion3(x):
    y1=x[1]
    y2=-sin(x[0])   
    return [y1,y2]
    
def lorenz(x): 
    b=8./3
    r=24.5
    s=10
    y0=s*(x[1]-x[0])
    y1=r*x[0]-x[1]-x[0]*x[2]
    y2=x[0]*x[1]-b*x[2]
    
    return [y0,y1,y2]
    
    

def euler(y0,t0,tf,h,f):
    Y=[]
    for i in range(len(y0)):
        Y.append([y0[i]])
        
    for k in arange(t0+h,tf,h):
        
        y=[]
        for l in range (len(y0)):
            y.append(Y[l][-1])
            
        for j in range(len(y0)):
           
            c=y[j]+(f(y)[j])*h
            Y[j].append(c)
        
    return Y
        
 
def euler2(y0,t0,tf,h,f):
    Y=[y0]
    p=y0
    for i in arange(t0+h,tf,h):
        y=[]
        for k in range(len(y0)):
            c=p[k]+h*f(p)[k]
            y.append(c)
        Y.append(y)
        p=y
    return Y

X=[]
for i in arange(0,100,0.001):
    X.append(i)
    
    
#Y1=euler([1,1,1],0,100,0.001,lorenz)
#Y2=euler([1.01,1,1],0,100,0.001,lorenz)

#sol = []
#for i in range(-10,10,5):
#    for j in range(-10,10,5):
#        for k in range(-10,10,5):
#            Y = euler([i,j,k],0,50,0.001,lorenz)
#            sol.append(Y) 
            
            

#figure(figsize=(15,10))
#plot(X,Y[0],'ro')
#show()


#
#fig = figure()
#ax = fig.add_subplot(111,projection='3d')
#ax.plot(Y1[0],Y1[1],Y1[2])
#ax.plot(Y2[0],Y2[1],Y2[2])
#show()

def Funcion(x):
    a=0
    b=1
    c=-1
    d=-1
    y0=a*x[0]+b*x[1]
    y1=c*x[0]+d*x[1]
    return [y0,y1]
  
  
Y=euler([0.03,0.20],0,100,0.001,Funcion)
Y1=euler([-.03,-.20],0,100,0.001,Funcion)
Y2=euler([-.01,.02],0,100,0.001,Funcion)
Y3=euler([.01,-.02],0,100,0.001,Funcion)

CampoPend(Funcion)

figure(figsize=(15,10))
plot(Y[0],Y[1])
plot(Y1[0],Y1[1])
plot(Y2[0],Y2[1])
plot(Y3[0],Y3[1])
axis([-5,5,-5,5])
show()



  
    
    
#
#figure(figsize=(15,15))
#for i in range(0,len(Y[0]),40):
#    quiver(Y[0][i],Y[1][i],Funcion([Y[0][i],Y[1][i]])[0],Funcion([Y[0][i],Y[1][i]])[1],width=0.001,scale=100,headlength=7)
#plot(Y[0],Y[1])
#axis([-20,20,-20,20])
#show()
    

print eigenvalores(7,1,-4,3)



    

#fig=figure(figsize=(15,10))
#plot(Y[0],Y[1])
#axis([0,10,0,10])
#show()
#






            
            
            
            

