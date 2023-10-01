from doctest import ELLIPSIS_MARKER
from math import floor
import operator

filename='day11/input.txt'
#filename='day11/day11.txt'
with open(filename) as f:
    lines = [x for x in f.read().split('\n\n')]




monkey_dict={'Monkey 0':[],'Monkey 1':[],'Monkey 2':[],'Monkey 3':[],'Monkey 4':[],'Monkey 5':[],'Monkey 6':[],'Monkey 7':[]}
monkey_checks={'Monkey 0':0,'Monkey 1':0,'Monkey 2':0,'Monkey 3':0,'Monkey 4':0,'Monkey 5':0,'Monkey 6':0,'Monkey 7':0}

#create initial item list
modulo=1
for monkey in lines:
    monkey_list=monkey.split('\n')
    monkey_nr=monkey_list[0].replace(':', '')
    monkey_list[1]=monkey_list[1].replace(',', '')

    
    
    for val in monkey_list[1].split(' ')[4:]:
        monkey_dict[monkey_nr].append(int(val))
    
    #modulo calc for task 2
    i =monkey_list[3].split(' ')[-1]
    modulo *= int(i)

print(modulo)

#task1
task=1
div=3
round_nr=20
#task2
task=2
div=modulo #or comment out worry level
round_nr=10000

rounds=0
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul}
while rounds<round_nr:
    
    for monkey in lines:
        monkey_list=monkey.split('\n')
        monkey_nr=monkey_list[0].replace(':', '')
        
        monkey_op = monkey_list[2].split(' ')
        test = monkey_list[3].split(' ')
        iftrue = monkey_list[4].split(' ')
        iffalse = monkey_list[5].split(' ')
        
        monkey_checks[monkey_nr]+=len(monkey_dict[monkey_nr])
        
        for val in monkey_dict[monkey_nr]: # for each nr in list
            worry_level=0
            if monkey_op[-1]=='old':
                worry_level = ops[monkey_op[-2]](int(val), int(val))
                #worry_level = worry_level/floor(div) if task==1 else worry_level%div
            else:
                worry_level = ops[monkey_op[-2]](int(val), int(monkey_op[-1]))
                #worry_level = worry_level/floor(div) if task==1 else worry_level%div
            
            if worry_level % int(test[-1])==0:
                monkey_dict['Monkey '+ iftrue[-1]].append(worry_level)
            else: 
                monkey_dict['Monkey '+ iffalse[-1]].append(worry_level)
        monkey_dict[monkey_nr]=[]
    rounds+=1


values= list(monkey_checks.values())
values.sort(reverse=True)
print(values[0]*values[1])
#print(monkey_dict)
