# Higher Order Function
# filter function-The filter function is used to filter out the elements of an iterable (sequence) depending on a function that texts each element in the sequence to be true or not.
a=[80,73,93,85,62,29,58,63,93]

# def firstd(n):
#     if n>=60:
#         return True

  #using lambda function

result=filter(lambda x:x>=60,a)

print(result)
print(type(result))

for i in result:
    print(i)

l1=list(result)
print(type(l1))
