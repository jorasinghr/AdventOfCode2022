with open('Day01/input1.txt') as f:
    lines = [x for x in f.read().split('\n')]
    
#solution 1
y=0 #highest number
z=0 #compared number
for x in lines:
    if x == '':
        if y<z:
            y=z
        z=0
    else:
        z+=int(x)

print(y)
        
#solution 2
sum_list=[]
z=0 #compared number
for x in lines:
    if x == '':
        sum_list.append(z)
        z=0
    else:
        z+=int(x)
sum_list.append(z)
sum_list.sort(reverse=True)     
print(sum_list[0]+sum_list[1]+sum_list[2])

   