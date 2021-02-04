# A dictionary within another dictionary called as nested dictionary or nesting of dict
nestdict={1:"ruby",2:"java",3:"python",4:{10:"ten",20:"twenty"}}

for i in nestdict:
    print(i,"=",nestdict[i])
# creating empty nested dictionary
a={'course':'python','fee':50000,1:{'couse':'java','fee':20000}}
print(type(a),a)
print(a['course'])
print(a[1])
print(a[1]['couse'])
a[1]['course1']= "c/c++"
print(a[1])
print(a)
a[1]['duration']='1 month'
a['duration']='1 month'
print(a)
