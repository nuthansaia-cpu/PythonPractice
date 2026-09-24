import uuid
id=uuid.uuid1()
print(id)

id2=uuid.uuid4()
print(id2)

id3=uuid.uuid3(uuid.NAMESPACE_OID,'laptop')
print(id3)

id4=uuid.uuid5(uuid.NAMESPACE_OID,'laptop')
print(id4)


items=[['Laptop',1200],['Mouse',20],['Keyboard',30],['Tablet',200]]
item_data={}
for item in items:
	id = uuid.uuid5(uuid.NAMESPACE_OID,item[0])
	key=id.hex[:6]
	item_data[key]=item
print("Item Data:")
for k, v in item_data.items():
	print(f"{k}:{v}")

