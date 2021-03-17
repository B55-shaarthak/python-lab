k=int(input('enter the number'))
for i in range (2,int(k/2)):
    if k%i==0:
        print('not prime')
        break
    else:
        print('prime no')
