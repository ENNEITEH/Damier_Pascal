from sympy import isprime,factorint
import time
import numpy as np
import matplotlib.pyplot as plt

# On utilise le type object pour que les calculs soit avec des 
# des ints aussi long que nécessaire sauf si 
# on utilise le modulo dès le calcul des matrices A et B

def triangle_pascal_gauche(N,Fmod=False):
    if Fmod:
        p = np.zeros((N, N), dtype='int')
        p[:, 0] = 1 # première colonne à 1
        for i in range(1, N): 
            p[i,1:i+1] = np.mod(p[i-1,1:i+1] + p[i-1,0:i],N)
    else:
        p = np.zeros((N, N), dtype=object)
        p[:, 0] = 1 # première colonne à 1
        for i in range(1, N): 
            p[i,1:i+1] = p[i-1,1:i+1] + p[i-1,0:i]
    return p

def damier_pascal_A(N,Fmod=False):
    p = triangle_pascal_gauche(N,Fmod=Fmod)
    return p+p.T-np.identity(N,dtype=object)

def triangle_pascal_droit(N,Fmod=False):
    if Fmod:
        p = np.zeros((N, N), dtype='int')
        p[:, -1] = 1         
        for i in range(N-2,-1,-1):
            p[i,i:N-1] = np.mod(p[i+1,i:N-1] + p[i+1,i+1:N],N)
    else:
        p = np.zeros((N, N), dtype=object)
        p[:, -1] = 1 
        for i in range(N-2,-1,-1):
            p[i,i:N-1] = p[i+1,i:N-1] + p[i+1,i+1:N]
    return p

def damier_pascal_B(N,Fmod=False):
    p = triangle_pascal_droit(N,Fmod=Fmod)
    if Fmod:
        return p+p.T-np.identity(N,dtype='int')
    else:
        return p+p.T-np.identity(N,dtype=object)

def damier_pascal_S(N,Fmod=False):
    return damier_pascal_A(N,Fmod=Fmod)+damier_pascal_B(N,Fmod=Fmod)

def damier_pascal_D(N,Fmod=False):
    return np.minimum(1,np.mod(damier_pascal_S(N,Fmod=Fmod),N))
    
def TestDamier(N,Fmod=False):
    D=damier_pascal_D(N,Fmod=Fmod).astype('bool')
    return not (np.any(D[:,:-1]==D[:,1:]) or np.any(D[:-1,:]==D[1:,:]))

def VerificationDamierPascal(Nmax=100,Fmod=False):
    temps={"x":[],"y":[]}
    ti=time.time()
    for N in range(3,Nmax+1):
        titmp=time.time()
        Nisprime=isprime(N)
        NDamier=TestDamier(N,Fmod=Fmod)
        if NDamier and Nisprime:
            # N premier et Damier regulier: conjecture vérifiée
            print(end=".")
        elif  (not NDamier) and (not Nisprime):
            # N pas premier et Damier pas vérifiée : conjecture vérifiée
            print(end=".")
        else:
            # conjecture non vérifiée
            print()
            print("Contre exemple N=",N,"NDamier",NDamier,"Nisprime",Nisprime)
            print()
        tftmp=time.time()
        temps["x"].append(N)
        temps["y"].append(tftmp-titmp)
        
        if N%100==0:
            print(N)
    tf=time.time()
    print()
    print("temps total (s)/N:",np.round((tf-ti)/N,5),"avec N=",N,"Fmod",Fmod)
    return temps

def AffichageDamierPascal(N):
    plt.figure()
    plt.imshow(damier_pascal_D(N,Fmod=True).astype('int')*255,cmap='gray', vmin=0, vmax=255, interpolation='none')
    if N>10:
        plt.xticks([])  
        plt.yticks([]) 
    else:
        plt.gca().xaxis.set_ticks_position('top')   
        plt.gca().xaxis.set_label_position('top')   
    plt.show()
     
