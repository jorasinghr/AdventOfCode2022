with open('Day08/input.txt') as f:
    lines = [x for x in f.read().split('\n')]
    
#print(lines)


#task1
def vision(tree_check, tree_list):
    if type(tree_list) == int:
        return tree_check>tree_list
    else:    
        for val in tree_list:
            if  not tree_check>val:
                return False  
        return True
        
n=0
for x, line in enumerate(lines[1:-1]):
    for y, chr in enumerate(line[1:-1]):
        tree=int(chr)
        if x==0:
            up=int(lines[x][y+1])
        else:
            up=[int(a) for a in [b[y+1] for b in lines[x::-1]]]
        
        if x==(len(lines)-3):
            down=int(lines[x+2][y+1])
        else:
            down=[int(a) for a in [b[y+1] for b in lines[x+2:]]]
        
        if y==0:
            left=int(lines[x+1][y])
        else:
            left=[int(a) for a in lines[x+1][y::-1]] 
            
        if y==len(lines[x+1])-1:
            right=int(lines[x+1][y+2])
        else:
            right=[int(a) for a in lines[x+1][y+2:]] 
        
        
        if vision(tree, up):
            n+=1
        elif vision(tree, down):
            n+=1
        elif vision(tree, left):
            n+=1
        elif vision(tree, right):
            n+=1
               
#print(n)
#print(2*len(lines))
#print(2*len(lines[0]))
print(n+(2*len(lines))+(2*len(lines[0]))-4)


#task2
high_score=0
def vision2(tree_check, tree_list):
    m=0
    if type(tree_list) == int:
        if tree_check>=tree_list:
            return 1
        else:
            return 0
    else:    
        for val in tree_list:
            if tree_check>val:
                m+=1
            else:
                return m+1
        return m
        
for x, line in enumerate(lines[1:-1]):
    for y, chr in enumerate(line[1:-1]):
        tree=int(chr)
        if x==0:
            up=int(lines[x][y+1])
        else:
            up=[int(a) for a in [b[y+1] for b in lines[x::-1]]]
        
        if x==(len(lines)-3):
            down=int(lines[x+2][y+1])
        else:
            down=[int(a) for a in [b[y+1] for b in lines[x+2:]]]
        
        if y==0:
            left=int(lines[x+1][y])
        else:
            left=[int(a) for a in lines[x+1][y::-1]] 
            
        if y==len(lines[x+1])-1:
            right=int(lines[x+1][y+2])
        else:
            right=[int(a) for a in lines[x+1][y+2:]] 
        
        n_up = vision2(tree, up)
        n_down = vision2(tree, down)
        n_left = vision2(tree, left)
        n_right = vision2(tree, right)
        #print(n_up, n_down, n_left, n_right)
        score = n_up*n_down*n_left*n_right
        
        
        if score>high_score:
            high_score=score


           
print(high_score) 
