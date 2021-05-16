import numpy as np
import matplotlib.pyplot as plt

#Defining the general model
def lotkaVolterraModel(x, params):

        
        a = params["a"]
        
        b = params["b"]
    
        c = params["c"]
        
        d = params["d"]
        
        #time to relative other states
        #functions
        xdot = np.array([a*x[0] - b*x[0]*x[1], d*x[0]*x[1] - c*x[1]])
        return xdot
    
#RK4 Method

def rungeKutta4(f,x0,t0,tf,h): 
    
    t = np.arange(t0,tf,h)
    nt = t.size
    
    nx = x0.size    
    #filling with zeros nx, nt)
    x = np.zeros((nx,nt))
    
    x[:,0] = x0 
    
    for i in range (nt -1):
        
        k1 = h*f(t[i], x[:,i])
        k2 = h*f(t[i] + h/2, x[:,i] + k1/2)
        k3 = h*f(t[i] + h/2, x[:,i] + k2/2)
        k4 = h*f(t[i] + h, x[:,i] + k3)
        
        dx = (k1 + 2*k2 + 2*k3 + k4)/6
        
        x[:,i + 1] = x[:,i] + dx
        
    return (x, t)

#Definimg Params

params = {"a":  2*1.2, "b": 2*0.6, "c": 2*0.8, "d": 2*0.3}

f = lambda t,x : lotkaVolterraModel(x, params)

#x_initialization
x0 = np.array([2,1])



#solve the diff eq.

t0 = 0
tf = 30
h = 0.1
x,t = rungeKutta4(f, x0, t0, tf, h)


#Plot Results

plt.subplot(1, 2, 1)
plt.plot(t, x[0,:], "r", label= "Preyers")
plt.plot(t, x[1,:], "b", label= "Predators")
plt.xlabel("Time (t)")
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x[0,:], x[1,:])
plt.xlabel("Preys")
plt.ylabel("Predators")
plt.grid()

plt.show()

