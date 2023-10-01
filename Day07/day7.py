with open('Day07/day7.txt') as f:
    lines = [x for x in f.read().split('\n')]

commands = [[idx,val[2:]] for idx,val in enumerate(lines) if val[0]=='$']
print(commands)
dixt={'/':{'dir a':413, 'dir b':342, 'dir c': {'3':324}}}

'''
class NonBinTree:
    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))
'''       
print(dixt['/'].keys())
a = dixt['/']
a['dir d'] =123
if 'dir a' in dixt['/'].keys():
    print('a')
    print(dixt)
#mytree = NonBinTree(0)        



#current_dir='/'
hist_dir=[]
list_debth=[]



main_dict={'/':0}
first=True
first_list=[]
for id,com in commands:
    if first and com[:2]=='ls':
        for i in range(id+1, 10000):
            if i==len(lines):
                break
            elif lines[i][2:4]=='cd':
                break
            else: #not lines[i][:3]=='dir':
                first_list.append(lines[i])
                
        temp_dict=main_dict['/']
        for val in first_list:
            if val[:3]=='dir':
                print(val[3:])
                temp_dict[val[3:]] = 0
            else:
                a = val.split(' ')
                temp_dict[a[1]]= a[0]
        
        c_dict=main_dict['/']
        first=False
        current_dir='/'
    
    if com[:2] =='cd' and id>1:
        if com == 'cd ..':
            hist_dir = hist_dir[:-1]
            c_dict=main_dict['/']
            for val in hist_dir:
                c_dict=c_dict[val]
        else:
            current_dir=com[3:]
            c_dict = c_dict[current_dir]
            hist_dir.append(com[3:])
        
    elif com[:2] =='ls':
        temp_list=[]
        for i in range(id+1, 10000):
            if i==len(lines):
                break
            elif lines[i][2:4]=='cd':
                break
            
            else:# not lines[i][:3]=='dir':
                temp_list.append(lines[i])
                
        #print(temp_list, current_dir)
        temp_dict = c_dict[current_dir]
        for val in temp_list:
            if val[:3]=='dir':
                temp_dict[val] = 0
            else:
                a = val.split(' ')
                temp_dict[a[1]]= a[0]

    else:
        print('ERROR something escaped')
            

print(main_dict)        

    
    
    
'''
for line in lines:
    if line[0]=='$':
        if line[2:4]=='cd':
            
            print(line[2:4])
        elif line[2:4]=='ls':

            print(line[2:4])
        else: 
            print('ERROR')
'''