j=int(input())
if(j>1):
    for k in range (3, num):
        if(j%k)==0:
            print('yes')
            break
    else:
        print('no')
