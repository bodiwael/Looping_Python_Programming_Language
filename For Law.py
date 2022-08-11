k = 0

for k in range(10):
        
    print(k)


k = 0

for k in range(5 , 21) :
    
    print(k)
    

k = 0

for k in range(2 , 21 , 2) :
    
    print(k)
    

G = [ ( X , Y) for X in range (10) for Y in range (10) ]

print(G)

G = [ ( X , Y) for X in range (10) for Y in range (10) if X > Y ]

print(G)

H = "MyNameisabdelrahmanwaelabdelrahamnarashadammar"

for l in range ( len(H) ) :
    
    print(H[l])