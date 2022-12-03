with open('Day03/input.txt') as f:
    lines = [x for x in f.read().split('\n')]

sum=0
for line in lines:
    comp1 = list(set(line[:int(len(line)/2)]))
    comp2 = list(set(line[int(len(line)/2):]))
    #print(comp1, ' --- ', comp2)
    
    for val1 in comp1:
        if val1 in comp2:
            if ord(val1)<ord('a'):
                sum+=(ord(val1)-ord('A')+27)
            else:
                sum+=(ord(val1)-ord('a')+1)

    #for val2 in comp2:
    #    if val2 in comp1:
    #        dublicates.append(val2)
    
print(sum)

sum2=0
for idx, line in enumerate(lines[::3]):
    sack1 = set(line)
    sack2 = set(lines[(3*idx)+1])
    sack3 = set(lines[(3*idx)+2])
    #print(sack1,'\n', sack2,'\n', sack3, '\n')
    for val in sack1:
        if val in sack2 and val in sack3:
            if ord(val)<ord('a'):
                sum2+=(ord(val)-ord('A')+27)
            else:
                sum2+=(ord(val)-ord('a')+1)
                
print(sum2)