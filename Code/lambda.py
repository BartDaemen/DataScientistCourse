#Functie 1: a*2+b (4,2) = 10

x= lambda a,b: a*2+b
print(x(4,2))

#Functie 2: a²+b² (5,3) = 34

y = lambda a,b: a**2 + b**2
print(y(5,3))

#Functie 3: (a+b)² =a²+2ab+b²  (4,3) = 49

z= lambda a,b: (a+b)**2
print(z(4,3))

#Functie 4  Als a deelbaar is door 3, a/3 anders a*2
result = lambda x : x/3 if x %3==0 else a*2
print(result(9))

#Functie 5 : Als a > b*2 dan a/2 anders a*2
f5 = lambda a,b: b*2 if a > b else a*2
print(f5(2,1))

#Functie 6 : als a + b kleiner is c dan c-(a+b) anders a+b+c
f6 = lambda a,b,c: c-(a+b) if a+b < c else a+b+c
print(f6(1,2,4))

# Euro -> dollar
ed = lambda a: a*1.10
print(ed(100))

#UK Pond -> dollar
pd = lambda a: a*1.32
print(pd(100))

#Euro-UK pond

ep = lambda a: a*0.83
print(ep(100))

#UK pond - Euro
pe = lambda a: a*1.20
print(pe(100))

x1 = lambda a,b: a*2+b
x2 = lambda a,b: a**2+b**2
x3 = lambda a,b: a**2+2*a*b+b**2
x4 =  lambda a : a/3 if a%3==0 else a*2 #doe als waar anders doe
x5 =  lambda a,b : a/2 if a>b*2 else a*2
x6 =  lambda a,b,c : c-(a+b) if a+b < c else a+b+c
print(x1(4,2))
print(x2(3,4))
print(x3(3,4))
print(x4(7))
print(x5(9,12))
print(x6(1,2,9))
