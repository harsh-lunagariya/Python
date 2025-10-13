while True:
    n = int(input('Enter an odd number : '))
    if n<3:
        continue
    elif n%2==0:
        continue
    else:
        break

mid = n//2
ct=1
for i in range(n):
    if i==mid :
        temp = (n-1)//2
        patt = '---'*temp+'AUM'+'---'*temp
        print(patt)
    elif i<mid:
        temp = (n-ct)//2
        patt = '---'*temp+'.|.'*ct+'---'*temp
        print(patt)
        ct +=2
    else:
        ct -=2
        temp = (n-ct)//2
        patt = '---'*temp+'.|.'*ct+'---'*temp
        print(patt)



