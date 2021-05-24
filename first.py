num=int(input("ENTER THE NUMBER:-"))
flag= False
if num>1:
    for i in range(2, num):
        if (num % i) == 0:
            flag= True
            break
if flag==True:
    print(num,"IS NOT A PRIME NUMBER")
else:
    print(num,"IS A PRIME NUMBER")
