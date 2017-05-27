a = input()
s = 0
if a == 1:  
    print a, 'prime'

else : 

    for i in range (2, a ):

        if a%i == 0:
            print a,'not prime'
            s = 'true'
            break

    if s == 0 : print a,'prime'
