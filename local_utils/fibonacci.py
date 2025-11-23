from sympy import binomial
import numpy as np

def Lucas(N,Verbose=False):
    if N==0:
        return 2
    elif N==1:
        return 1
    snm1=1
    snm2=2
    sn=snm1+snm2
    niter=2
    while niter!=N:
        snm2=snm1
        snm1=sn
        sn=snm1+snm2
        niter+=1
    if Verbose:
        return sn,niter
    else:
        return sn
        
def Fibo(N,Verbose=False):
    snm1=0
    snm2=1
    sn=snm1+snm2
    niter=1
    if N==0:
        return 0
    elif N==1:
        return 1
    #elif N==2:
    #    return 1
    
    while niter!=N:
        snm2=snm1
        snm1=sn
        sn=snm1+snm2
        niter+=1
    if Verbose:
        return sn,niter
    else:
        return sn
        
def G(n,N):
    if n>N+2 or n<0:
        return "ERROR"
    elif n==N:
        return Fibo(N)
    elif n==N+1:
        return Fibo(N-1)
    else:
        k=N-n
        #print("start",k,N)
        g=Fibo(k+1)*Fibo(N)+Fibo(k)*Fibo(N-1)
        #print("g",n,N,k,g,"detail",Fibo(k+1)*Fibo(N),Fibo(k)*Fibo(N-1))
        for j in range(0,k):
            g-=Fibo(k-j)*binomial(N,j)
        return g

def zetan(n,N):
    if n>N-1 or n<0:
        return "ERROR",n,N
    return Fibo(n+1)+G(n+1,N)

def zetanDamier(n,N):
    # Ligne complète du Damier
    # On doit distingguer
    if n%2==0:
        return 2*(zetan(n,N)-1)
    else:
        return 2*zetan(n,N)
    
def SigmaZetanDamier(N):
    # somme des termes du Damier Complet
    return 2*np.sum([zetanDamier(n,N) for n in range(N-1)])+zetanDamier(N-1,N)


def SigmaZetan(N):
    # somme des zetan
    # c'est à dire 2*la somme des
    # termes du triangle de Pascal
    return 2*np.sum([zetan(n,N) for n in range(N-1)])+zetan(N-1,N)



def SigmaZetanTheo(N):
    return 2*(2**N-1)

def SigmaZetanDamierTheo(N):
    return 2*(SigmaZetanTheo(N)-N)

def DisplaySijRecurrence(i,j,N):
    if (3<= i < N-1) and (1<= j <= i-2): 
        m=i+j
        print(f'S({i},{j})=S({i-1},{j-1})+',end="")
        kmin=0
        kmax=j-1
        for k in range(kmin,kmax+1):
            print(f'S({i-2-k},{j-k})+',end="")
        print(f'W({i-j-1},{0})')
    else:
        print("Condition non vérifiée i=",i,"j=",j)
        