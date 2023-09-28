import math

def lookupWire(area):
    rc = -1
    len = 2*(area/3.1415926535)**(1/2)
    for AWG in range(40,0,-1):
        Bitola = 0.005*92**((36-AWG)/39)*25.4
        if len <= Bitola:
            rc = AWG
            break
    return rc    

# premissas
Vp = float(input("Tensao primario ? (V) "))
Vp1 = 0.0
Tipo = input("Primario com derivaçao ? (sim ou nao)")
if Tipo == "S" or Tipo=="s" or Tipo=="sim" or Tipo=="Sim":
    Vp1 = float(input("Tensao primario adicional ? (V) "))
Sec = int(input("Numero de secundarios ?"))
while Sec == 0 or Sec > 5:
    Sec = int(input("numero invalido de secundarios:"))
Vs1 = float(input("Tensao secundario 1 ? (V)"))
Is1 = float(input("Corrente secundario 1 ? (A)"))
Vs2 = 0.0
Is2 = 1.0
Vs3 = 0.0
Is3 = 1.0
Vs4 = 0.0        
Is4 = 1.0
Vs5 = 0.0
Is5 = 1.0
Ip1 = 0
        
if Sec > 1:
    Vs2 = float(input("Tensao secundario 2 ? (V)"))
    Is2 = float(input("Corrente secundario 2 ? (A)"))
if Sec > 2:
    Vs3 = float(input("Tensao secundario 3 ? (V)"))
    Is3 = float(input("Corrente secundario 3 ? (A)"))
if Sec > 3:
    Vs4 = float(input("Tensao secundario 4 ? (V)"))
    Is4 = float(input("Corrente secundario 4 ? (A)"))
if Sec > 4:
    Vs5 = float(input("Tensao secundario 5 ? (V)"))
    Is5 = float(input("Corrente secundario 5 ? (A)"))
F = float(input("Frequencia de operaçao ? (Hz)"))
Bm = float(input("Densidade de Fluxo ou induçao magnetica ? (gauss)"))
eta = float(input("Rendimento ? (%)"))
DC = 3.0

# calculos
Pw = (Vs1*Is1 + Vs2*Is2 +Vs3*Is3 + Vs4*Is4 + Vs5*Is5)/(eta/100)
Ip = Pw/Vp
if Vp1 != 0:
    Ip1 = Pw/Vp1

Sp = Ip/DC
Sp1 = Ip1/DC
Ss1 = Is1/DC
Ss2 = Is2/DC
Ss3 = Is3/DC
Ss4 = Is4/DC
Ss5 = Is5/DC

if Vs2 == 0 and Vp1 ==0:
    Sm = 7.5*(Pw/F)**(1/2)
else:
    if (Vs2 != 0 and Vp1 == 0) or (Vs2 == 0 and Vp1 != 0):
        Sm = 7.5*(1.25*Pw/F)**(1/2)
    else:
        Sm = 7.5*(1.5*Pw/F)**(1/2)
    
Sg = 1.1*Sm
L = 0.0
H = 0.0
print("Secçao minima do nucleo: " +  str(round(Sg,2)) + "cm2   perna central de " + str(round(Sg**(1/2),1)))
while Sg > (L*H):
    L = float(input("Largura da perna central (cm) ? "))
    H = float(input("Empilhamento do nucleo (cm) ? "))

Sgo = L * H
Smo = Sgo / 1.1
          
Wp = lookupWire(Sp)
Wp1 = lookupWire(Sp1)
Ws1 = lookupWire(Ss1)
Ws2 = lookupWire(Ss2)
Ws3 = lookupWire(Ss3)
Ws4 = lookupWire(Ss4)
Ws5 = lookupWire(Ss5)

Espiraporvolt = 100000000 / (4.44 * Bm * Smo * F)
Np = int(Vp * Espiraporvolt)
Np1 = int(Vp1 * Espiraporvolt)
Ns1 = int(Vs1 * Espiraporvolt * 1.05)
Ns2 = int(Vs2 * Espiraporvolt * 1.05)
Ns3 = int(Vs3 * Espiraporvolt * 1.05)
Ns4 = int(Vs4 * Espiraporvolt * 1.05)
Ns5 = int(Vs5 * Espiraporvolt * 1.05)

# Resultados
print("Potencia no primario (VA) = " + str(round(Pw,2)))      
print("Secçao usada " + str(round(Sgo,2)) + "cm2")
print("Tensao primario (V):" + str(round(Vp,1)) + "V @ " + str(round(Ip,3)) + "A")
print("Espiras primario:" + str(Np) + " @ AWG" + str(Wp))
if Vp1 != 0:
    print("Tensao adicional primario (V):" + str(round(Vp1,1)) + "V @ " + str(round(Ip1,3)) + "A")
    print("Espiras adicionais primario:" + str(Np1 - Np) + " @ AWG" + str(Wp1))
print("Tensao secundario1 (V):" + str(round(Vs1,1)) + "V @ " + str(round(Is1,3)) + "A")
print("Espiras secundario1:" + str(Ns1) + " @ AWG" + str(Ws1))
if Vs2 != 0:
    print("Tensao secundario2 (V):" + str(round(Vs2,1)) + "V @ " + str(round(Is2,3)) + "A")
    print("Espiras secundario2:" + str(Ns2) + " @ AWG" + str(Ws2))
if Vs3 != 0:
    print("Tensao secundario3 (V):" + str(round(Vs3,1)) + "V @ " + str(round(Is3,3)) + "A")
    print("Espiras secundario3:" + str(Ns3) + " @ AWG" + str(Ws3))
if Vs4 != 0:
    print("Tensao secundario4 (V):" + str(round(Vs4,1)) + "V @ " + str(round(Is4,3)) + "A")
    print("Espiras secundario4:" + str(Ns4) + " @ AWG" + str(Ws4))
if Vs5 != 0:
    print("Tensao secundario5 (V):" + str(round(Vs5,1)) + "V @ " + str(round(Is5,3)) + "A")
    print("Espiras secundario5:" + str(Ns5) + " @ AWG" + str(Ws5))