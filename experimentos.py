import subprocess, random, re, math, itertools, time
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

def run(a):
    inp = f"{len(a)}\n{' '.join(map(str,a))}\n"
    p = subprocess.run(["./sol"], input=inp, capture_output=True, text=True)
    b = list(map(int, p.stdout.split()))
    m = re.search(r"costo=(\d+) estados=(\d+) ms=([\d.]+)", p.stderr)
    return b, int(m[1]), int(m[2]), float(m[3])

def harmony(b): return all(math.gcd(x,y)==1 for x,y in itertools.combinations(b,2))
def cost(a,b): return sum(abs(x-y) for x,y in zip(a,b))

def brute(a, vmax):
    best=[10**9]
    def rec(i, cur, c):
        if c>=best[0]: return
        if i==len(a): best[0]=c; return
        for v in range(1,vmax+1):
            if all(math.gcd(v,u)==1 for u in cur):
                rec(i+1, cur+[v], c+abs(a[i]-v))
    rec(0,[],0); return best[0]

print("=== PRUEBAS ===")
casos = {
 "Ej.1 (todos 1)":[1]*5, "Ej.2":[1,6,4,2,8], "n=1, a=30":[30], "n=1, a=1":[1],
 "n=2, a=[4,2]":[4,2], "n=3, a=[30,30,30]":[30,30,30], "n=2 iguales [6,6]":[6,6],
 "n=100 todos 1":[1]*100, "n=100 todos 30":[30]*100,
}
for k,a in casos.items():
    b,c,s,ms = run(a)
    assert harmony(b) and cost(a,b)==c
    print(k, "| b =", (b if len(b)<=8 else str(b[:10])+"..."), "| costo =", c, "| harmony:", harmony(b))
b,c,_,_=run([30]*100); print("n=100 todos 30: no-1 en b:", [x for x in b if x!=1], "cantidad:", sum(x!=1 for x in b))

print("=== CONTRASTE CON FUERZA BRUTA ===")
random.seed(7); ok=0; tot=0
for n in (1,2,3):
    for _ in range(40):
        a=[random.randint(1,30) for _ in range(n)]
        _,c,_,_=run(a); assert c==brute(a,100),(a); tot+=1
for _ in range(25):
    a=[random.randint(1,30) for _ in range(4)]
    _,c,_,_=run(a); assert c==brute(a,60),(a); tot+=1
print("casos aleatorios iguales a fuerza bruta:", tot, "de", tot)

print("=== TIEMPOS ===")
ns=list(range(5,101,5)); res=[]
for n in ns:
    ts=[]
    for r in range(7):
        a=[random.randint(1,30) for _ in range(n)]
        _,c,s,ms=run(a); ts.append(ms)
    ts.sort(); res.append((n,ts[3],s)); print(n, "ms=%.1f"%ts[3], "estados=",s)
fig,ax=plt.subplots(1,2,figsize=(11,4))
ax[0].plot([r[0] for r in res],[r[1] for r in res],"o-"); ax[0].set_xlabel("n (tamaño de la entrada)"); ax[0].set_ylabel("tiempo (ms)"); ax[0].set_title("Tiempo de ejecución vs n"); ax[0].grid(alpha=.3)
ax[1].plot([r[0] for r in res],[r[2] for r in res],"s-",color="C1"); ax[1].set_xlabel("n"); ax[1].set_ylabel("estados (i,S) visitados"); ax[1].set_title("Subproblemas resueltos vs n"); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.savefig("tiempos.png",dpi=150)
# ajuste lineal t = c*n
import numpy as np
x=np.array([r[0] for r in res]); y=np.array([r[1] for r in res]); 
A=np.vstack([x,np.ones_like(x)]).T; m,c0=np.linalg.lstsq(A,y,rcond=None)[0]
print("ajuste t ~ %.3f*n + %.2f ; R2=%.4f"%(m,c0,1-((y-(m*x+c0))**2).sum()/((y-y.mean())**2).sum()))
