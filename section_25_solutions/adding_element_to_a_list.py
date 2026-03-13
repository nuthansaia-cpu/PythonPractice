# --- Append ---
l1 = [1, 2, 3, 4, 5]
l1.append(6)  
print(l1)  

l1 = []
l1.append(10)
l1.append('python')
l1.append([1, 2])  
print(l1) 

# --- Slicing for Append ---
l1[len(l1):len(l1)] = [20]  
print(l1) 

# --- Extend ---
l2 = [1, 2, 3, 4]
l2.extend([5, 6, 7])  
print(l2)  

l3 = [1, 2]
l3.extend('python')  
print(l3)  

l4 = [1, 2, 3, 4]
l4.extend(range(5, 8))  
print(l4)  

# --- Insert ---
l5 = [1, 2, 3, 4]
l5.insert(0, 50) 
print(l5)  

l5.insert(2, 'python')  
print(l5)  

l5.insert(70, 'end') 
print(l5)  

# --- Slice Assignment for Insertion ---
l6 = [1, 2, 3, 4]
l6[2:2] = [55]  
print(l6)  

# --- Copy ---
l7 = [1, 2, 3, 4]
l8 = l7.copy()  
l8[0] = 100
print(l7)  
print(l8)  