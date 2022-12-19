
# List

Data=[11,21,51,101,3.14]

print("Data type is",type(Data)) # list
print("Length of list is",len(Data)) # 4
print("Actual data is:",Data)      # 11,21,51,101

print("Data from 0th index:",Data[0]) # 11
print("Data from 3rd index:",Data[3]) # 101

Data[0]=12
print("new data is:",Data[0])

Data.append(111)
print(Data)

Data.insert(2,51)
print(Data)

print("Data[0]:",Data[0])
print("Data[1]:",Data[1])
print("Data[-1]:",Data[-1])
print("Data[-2]:",Data[-2])

print("Data[1:3]",Data[1:3])
print("Data[0:4]",Data[0:4])