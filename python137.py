#nested tuple A tuple in anothe tuple is called nested tuple
a=(1,2,3,4,(12,13,14,15,16),5,6,7,8)
n=len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])>1:
#             m=len(a[i])
#             for j in range(m):
#                 print(i,j,"index",a[i][j])
#
#     else:
#         print(i,"index",a[i])

i=0
j=0
while i<n:
    if type(a[i]) is tuple:
        l=len(a[i])
        while j<l:
            print(i,j,"index",a[i][j])
            j+=1
    else:
        print(i,"index",a[i])
    i+=1