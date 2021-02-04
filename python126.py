# Accessing nested list using while loop

"""a=[21,22,23,24,25,26,[10,20,30,40,50,60],27,28,29,30]
l0=len(a)
i=0
j=0
while i<l0:
    if type(a[i]) is list:
        l1=len(a[i])
        while j<l1:
            print(i,j,"index =",a[i][j])
            j+=1
    else:
        print(i,"index =",a[i])
    i+=1
"""
nl=[[71,72,73,74,75,76,77,78,79,80],[61,62,63,64,65,66,67,68,69,70],[51,52,53,54,55,56,57,58,59]]
n=len(nl)
i=0
while i<n:
    print( i,"index =",nl[i])
    n1=len(nl[i])
    j=0
    while j<(n1):
        print(i,j,"index ",nl[i][j])
        j+=1
    i+=1
