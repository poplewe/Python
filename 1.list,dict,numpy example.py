

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