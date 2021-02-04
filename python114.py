#video 124   Recursion in python
# function call itself  is call recursion
"""def func1():
    print("PanditProgrammer.com")
    #func1()     # it is dangerous for system don't do mistake

func1()"""
'''import  sys            # this is for checking recurion liit
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())'''

#video 124   pass or call by object reference in python

"""def chfun(x):
    print("in function  after passing x id for this is ",x,id(x))
    x=20            # pass by object reference 
    print("after modifying id of x is",x,id(x))

x=22
chfun(x)
print("outside of fun" ,x)"""

# passing a list and checking id of list

"""def vlist(lst):
    lst.append(4)
    print(lst)    #after appending
    print(id(lst))        # we got same id  because list are mutable we can modify it
    lst=[10,20,30,40,50] #checking id of lst
    print(lst,id(lst))
    
lst=[1,2,3]

print(lst,id(lst))

vlist(lst)    #  here calling function
"""
# lw=['1','2']
# print(lw)
# print(type(lw))
# lw1=[1,2,3,4,5]
# print(lw1)
# print(type(lw1))