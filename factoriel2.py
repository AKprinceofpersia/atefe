print("be barname factorieli bodan yek addad khosh amadid:)")
z=int(input("addad khod ra vared konid: "))
def isFactorial(n) :
    i = 1
    while(True) :
         
        if (n % i == 0) :
            n //= i
             
        else :
            break
             
        i += 1
 
    if (n == 1) :
        return True
     
    else :
        return False
 


ans = isFactorial(z) 
if (ans == 1) :
    print("addad shoma factoriel ast")
else :
    print("addad shoma factoreil nist")