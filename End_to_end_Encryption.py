import random
alp=["#",'a','b','1',"~",'c','2','d','e','3',"&",'4','f',"`",'g',"%",'h','5','i','7','j','6','k',"^",'l','8','m','9','n','o','p','0','q','r','s','*','t','u','v','w',"$","x",",","y","!","z","@","-",'A',"(",'B',")",'C',"_",'D',"]","+",'E',"=",'F',"[",'G',"}","{",'H',"|","\\",'I',":",'J',";",'K',"\'",'\"',"L","?",'M',"/",'N',"<",'O','P','Q','R','S',".",'T',">",'U','V','W',"X","Y","Z"] # 94 element(0-93)

def encrypt():
    inp = input("Enter string for encryption: ")
    key = int(input("Enter security key between 1 and 45: "))
    if key < 1 or key > 45:
        raise ValueError("Key out range!!!")

    for i,x in enumerate(inp):
        if x in alp:
            index=(int(alp.index(x))+key)%94
            ListS = list(inp)
            ListS[i]=alp[index]
            # ListS.pop(3)
            inp = "".join(ListS)
        else:
            pass
        i=i+1

    inp1=str(alp[random.randrange(0,94)])+str(alp[random.randrange(0,94)])+str(alp[random.randrange(0,94)])+inp+inp[0]+str(alp[random.randrange(0,94)])+str(alp[random.randrange(0,94)])+str(alp[random.randrange(0,94)])
    inp1=inp1[ : :-1]
    print(inp1)


def decrypt():
    out = input("Enter string for decryption: ")
    key = int(input("Enter security key between 1 and 45: "))
    if key < 1 or key > 45:
        raise ValueError("Key out range!!!")
    out = out[::-1]
    ListS = list(out)
    ListS.pop()
    ListS.pop()
    ListS.pop()
    ListS.pop()
    ListS.pop(2)
    ListS.pop(1)
    ListS.pop(0)
    out = "".join(ListS)


    for i,x in enumerate(out):
        if x in alp:
            index = int(alp.index(x))
            if key <= index:
                real = (index - key)%94
                ListS = list(out)
                ListS[i] = alp[real]
                out = "".join(ListS)
            elif key > index:
                real = (index - key + 94)%94
                ListS = list(out)
                ListS[i] = alp[real]
                out = "".join(ListS)

        i = i + 1
    print(out)

a=int(input('Enter "1 for encryption" and "2 for decryption": '))
if a==1 or a==2:
    if a == 1:
        encrypt()
    else:
        decrypt()
else:
    raise ValueError("Invalid input!!")

