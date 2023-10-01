#filename='Day10/input.txt'
filename='Day10/day10.txt'
with open(filename) as f:
    lines = [x for x in f.read().split('\n')]
    
    
signals = [x.split(' ') for x in lines]
#print(signals)

#part1
cycle_checklist=[40*x+20 for x in range(0,6)] #20,40,100,140,180,220    
cycle_checklist2= [x-1 for x in cycle_checklist]
cycle_list=[]
cycle=1
val=1
for signal in signals:
    if signal[0]=='noop':
        if cycle in cycle_checklist:
            cycle_list.append(val)
        cycle+=1
    elif signal[0]=='addx':
        if cycle in cycle_checklist2 or cycle in cycle_checklist:
            cycle_list.append(val)
            
        cycle+=2
        val+=int(signal[1])        
    else:
        print('ERROR---------------')
         
      
print(cycle_list)

score=0
for val1, val2 in zip(cycle_list, cycle_checklist):
    score+=val1*val2
print(score)


#part2
cycle_checklist=[40*x for x in range(1,7)]
line=''
cycle=0
'''
signal=[]
for val in signals:
    signal.append(0)
    if val[0]=='addx':
        signal.append(int(val[1]))
'''

pixel_pos=0
for signal in signals:
    if signal[0]=='noop':
            ''