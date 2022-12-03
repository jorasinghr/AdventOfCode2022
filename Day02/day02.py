with open('Day02/input1.txt') as f:
    lines = [x for x in f.read().split('\n')]
    
#solution 1
x=1 #rock (a)
y=2 #paper (b)
z=3 #scissors (c)

loss=0
draw=3
win=6

points=0
for val in lines:
    if val[0]=='A':
        if val[2]=='X':
            points+=draw+x
        if val[2]=='Y':
            points+=win+y
        if val[2]=='Z':
            points+=loss+z
    if val[0]=='B':
        if val[2]=='X':
            points+=loss+x
        if val[2]=='Y':
            points+=draw+y
        if val[2]=='Z':
            points+=win+z
    if val[0]=='C':
        if val[2]=='X':
            points+=win+x
        if val[2]=='Y':
            points+=loss+y
        if val[2]=='Z':
            points+=draw+z
            
print(points)


#solution 2
rock=1 #A
paper=2 #B
scissors=3 #C 

loss=0
draw=3
win=6

#X win, Y draw, Z loss
points=0
for val in lines:
    if val[0]=='A':
        if val[2]=='X':
            points+=loss+scissors
        if val[2]=='Y':
            points+=draw+rock
        if val[2]=='Z':
            points+=win+paper
    if val[0]=='B':
        if val[2]=='X':
            points+=loss+rock
        if val[2]=='Y': 
            points+=draw+paper 
        if val[2]=='Z':
            points+=win+scissors
    if val[0]=='C':
        if val[2]=='X':
            points+=loss+paper
        if val[2]=='Y':
            points+=draw+scissors
        if val[2]=='Z':
            points+=win+rock
            
print(points)
