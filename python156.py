# nested list comprehension
lst=[[i+j for j in range(24,50,8)]for i in range(14,22)]
# print(lst)
# set comprehension in python
set1=set()
set0={2,8,17,9,23,54,26,72}
for i in set0:
    set1.add(i+10)
    # print(i)

# print(set1)
# setcom={i+100 for i in range(50,500,80)}  #this is called set comprehension
setcom={i if (i%5==0) else (i+100) for i in range(50,500,80)}  #this is called set comprehension
print(setcom)
