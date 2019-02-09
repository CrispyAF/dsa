#Global Public key components

p = 7                   #prime no 1
q = 3                   #prime no 2 (prime divisor of p)
h = 2                   #random integer where 1<h<p-1
g=((h**((p-1)/q))%p)    #where 1<h<p-1 and (h(p-1)/q mod p) >1 
print('g=',g)

#Private key

x = 5                   #Private key where 0<x<q

y=((g**(x))%p)          #computing public key
print('y=',y)

Hm=3                    #Hash function

k=2                     #Random key K where 0<k<q

#Signature Generation

r=(((g**(k))%p)%q)      #Signature Generation
print('r=',r)

def modInverse(k, q):   #Inverse Mod Function
    k = k % q; 
    for a in range(1, q): 
        if ((k*a)%q==1): 
            return a 
    return 1


print(modInverse(k, q))
b=(modInverse(k, q))
print('b=',b)
s=((b*((Hm+x*r)%q))%q)  #Signature Pair
print('S=', s)


#Verification of Key

w=(modInverse(s, q))    #Signature Verification
print('w=',w)
u1=((Hm*w)%q)           #Signature Verification Parameter
print('u1=',u1)
u2=((r*w)%q)            #Signature Verification Parameter
print('u2=',u2)
               
    #Spliting the terms for easy calculation of "V"
    
a1=((g**(u1))%p)        #for easy calculation of "V"
a2=((y**(u2))%p)        #for easy calculation of "V"
print('a1=',a1)
print('a2=',a2)

v=((a1*a2)%q)           #Calculation of Reciever's Sign
print('v=',v)
#print(v)
if v == r:
    print("The Signature is verified")
else:
    print("The Signature is not verified")

