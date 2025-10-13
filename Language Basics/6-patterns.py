#     1
#    121
#   12321
#  1234321
# 123454321
def numberPt():
    n=int(input("Enter a number : "))
    ct=1
    for i in range(1, n+1):
        print(" "*(n-i),end='')
        if(i == 1):
            print(i,end='')
        else:
            # for j in range(1,i+1):
            #     print(j,end='')
            # for j in range(1,i):
            #     print(i-j,end='')
            for j in range(1,i*2):  #6789  10 10 10 10
                if(j <= i):
                    print(j,end='')
                else:
                    print(((i*2)-j),end='')
        print()
        ct+=2

numberPt()
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

# def diamond():
#     n=int(input("Enter a number : "))

#     for i in range(1,n+1):
#         print(" "*(n-i),end='')
#         if(i==1):
#             print("*",end='')
#         else:
#             print("* ",end='')
#             if(i>2):
#                 print("  "*(i-2),end='')
#             print("*",end='')
#         print()
#     n-=1
#     for i in range(1,n+1):

#         print(" "*i,end='')

#         if(n==1):
#             print("*",end='')
#         else:
#             print("* ",end='')
#             if(n>2):
#                 print("  "*(n-2),end='')
#             print("*",end='')
#         print()
#         n-=1