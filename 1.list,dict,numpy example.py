import numpy as np

Value_List=[9,10,19,11,1,0];
print(Value_List)


type(Value_List)



Value_List.sort()
print(Value_List)



del Value_List[4];
print(Value_List)



print(len(Value_List))


Value_List.append(10);
print(Value_List)


Value_List.index(9)




Value_List.insert(5,4)
print(Value_List)



Value_List.remove(10)
print(Value_List)



Value_List.pop()
print(Value_List)


Value_List.pop(1)
print(Value_List)




Value_Dict={'name':'John','e-mail':'google@gmail.com','phone':'01234762825','birth':'0916','live':'China','from':'Japan'}



print(Value_Dict)

print(Value_Dict.items())
print(Value_Dict.keys())
print(Value_Dict.values())

for idx in Value_Dict.keys():
    print(idx, ": ",Value_Dict[idx]);
    
    
Value_Dict.clear()
print(Value_Dict)
    


print(Value_Dict.get('name'))


print('e-mail' in Value_Dict)
print('family' in Value_Dict)


a=np.zeros((3,4))
b=np.ones((2,3,4), dtype=float)
c=np.arange(90,200,10)


print(a)
print(b)
print(c)


ran_arr=np.random.random((2,3))
print(ran_arr)
print(len(ran_arr))
print(ran_arr.ndim)
print(ran_arr.size)

print(ran_arr.shape)
ran_arr=ran_arr.reshape(1,-1)
print(ran_arr.shape)

ran_arr2=np.random.random((3,6))
print(ran_arr2)
print(ran_arr2[1,:-1])

concat_arr=np.concatenate((ran_arr,ran_arr2),axis=0)
print(concat_arr)

hsplit_arr=np.hsplit(concat_arr,2)
print(hsplit_arr[0])
print(hsplit_arr[1])
print(hsplit_arr[0].shape,hsplit_arr[1].shape)

vsplit_arr=np.vsplit(concat_arr,2)
print(vsplit_arr[0])
print(vsplit_arr[1])
print(vsplit_arr[0].shape,vsplit_arr[1].shape)