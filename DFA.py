f=open("dfa.in")
states=[]
sigma=[]
trans=[]
fin=[]
start=None
sigmaok=0
statesok=0
transok=0
s=f.readline()
while s!="":
    s=s.strip()
    if s[0]=='#':
        pass
    elif s=="Sigma:":
        sigmaok=1
    elif s=="States:":
        statesok=1
    elif s=="Transitions:":
        transok=1
    elif s=="End":
        sigmaok=0
        statesok=0
        transok=0
        pass
    elif sigmaok==1:
        sigma.append(s)
    elif statesok==1:
        if s[len(s)-1]=='S':
            t=s.split(",")
            start=t[0]
            states.append(t[0])
        elif s[len(s)-1]=='F':
            t=s.split(",")
            fin.append(int(t[0][len(t[0])-2])-1)
            states.append(t[0])
        else:
            states.append(s)
    elif transok==1:
        s=s.split(", ")
        s[0]=s[0].strip()
        trans.append(tuple(s))
    s=f.readline()
# print(states)
# print(sigma)
# print(trans)
# print(start)
# print(fin)
# print(states)
# print(sigma)
# print(trans)
str=input("Input : ")
start=start.strip()
state=int(start[len(start)-1])-1 #starea de start primeste doar 3 din q3 (crae devine 2 pt ca in matrice am de la 0)
nrState=len(states)
matrix=[]
#fac o matrice nrState pe nrState cu None peste tot
for i in range(0,nrState):
    vect=[]
    for j in range(0,nrState):
        vect.append(None);
    matrix.append(vect)
# completez matricea ex: q1,1,q2 --> matrix[1-1][2-1] = 1 (matricea incepe de la 0)
for i in trans:
    matrix[int(i[0][len(i[0])-1])-1][int(i[2][len(i[2])-1])-1]=i[1]

for i in range(len(str)): # merg in sirul citit ex : 1001
    ok=0
    for j in range(0,nrState):
        if matrix[state][j]==str[i]: # caut sa vad daca din starea in care sunt exista starea in care plec
            state=j # daca exista, preiau starea in care merg ex : matrix[q0][q1]=1 atuncti plec pe linia q1
            ok=1
            break
    if ok==0: # daca sirul contine alta litera de alfabet ex : 2001 -> 2
        print("String is invalid.")
        break
if((state in fin) == True): # starea in care a ajuns dupa ce a terminat cuvantul este o stare finala
    print("String is valid.")  
elif(ok!=0) :
    print("String is invalid.")
