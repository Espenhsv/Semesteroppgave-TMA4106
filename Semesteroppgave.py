import numpy as np
import matplotlib.pyplot as plt


#eksplisitt euler
h=0.025
k=0.025
x = np.arange(0, 1+h, h)
t = np.arange(0, 0.1+k, k).round(3)
boundaryConditions = [0, 0]
initialConditions = np.sin(np.pi*x)
factor = k/h**2


n = len(x)
m = len(t)
T = np.zeros((n,m))
T[0,:] = boundaryConditions[0]
T[-1, :] = boundaryConditions[1]
T[:,0] = initialConditions
T.round(3)

for j in range(1,m):
    for i in range(1,n-1):
        T[i,j] = factor*T[i-1, j-1]+(1-2*factor)*T[i,j-1] + factor*T[i+1,j-1]
T.round(3)
plt.plot(T)
plt.xlabel('Avstand')
plt.ylabel('Tid')


#implisitt euler

A = np.diag([1+2*factor]*(n-2),0) + np.diag([-factor]*(n-3), -1) + np.diag([-factor]*(n-3), 1)

for j in range(1, m):
    b = T[1:-1,j-1].copy()
    b[0] = b[0] + factor*T[0 , j]
    b[-1] = b[-1] + factor*T[-1, j]
    solution = np.linalg.solve(A,b)
    T[1:-1,j] = solution
    print(solution)
R = np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0
for j in range(m):
    plt.plot(x,T[:,j], color= [R[j-2],G,B[j-2]])
plt.xlabel('Avstand')
plt.ylabel('Tid')

#Crank-Nicholsen
B = np.diag([2+2*factor]*(n-2),0) + np.diag([-factor]*(n-3),-1)+ np.diag([-factor]*(n-3), 1)
C = np.diag([2-2*factor]*(n-2),0) + np.diag([factor]*(n-3),-1)+ np.diag([factor]*(n-3), 1)

for j in range(0, m-1):
    c = T[1:-1,j].copy()
    c = np.dot(C, c)
    c[0] = c[0] + factor*(T[0,j]+T[0,j+1])
    c[-1] = c[-1] + factor*(T[-1,j] + T[-1,j+1])
    solution = np.linalg.solve(B,c)
    T[1:-1,j+1]=solution
T.round(2)

R = np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0

#analytisk
def analytisk(x,t):
    return np.exp(-np.pi**2*t/k)*np.sin(np.pi*x)

for j in range(m):
    plt.plot(x,T[:,j], color= [R[j],G,B[j]])
    plt.plot(x,analytisk(x,t[j]),'--')
    


    
plt.xlabel('Avstand')
plt.ylabel('Tid')
plt.legend(t)

    
    