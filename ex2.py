def pattern(n,i=0,mid=-1,ct=1):
    if i==n:
        return
    mid = n//2
    if i==mid:
        temp = (n-1)//2
        patt = '---'*temp+'AUM'+'---'*temp
    elif i< mid:
        temp = (n-ct)//2
        patt = '---'*temp+'.|.'*ct+'---'*temp
        ct+=2
    else:
        ct-=2
        temp = (n-ct)//2
        patt = '---'*temp+'.|.'*ct+'---'*temp
    print(patt)
    pattern(n,i+1,mid,ct)

pattern(11)