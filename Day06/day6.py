with open('C:/repos/AdventOfCode2022/Day06/input.txt') as f:
    stream = f.read().split('\n')[0]
    
#task1
for idx, val in enumerate(stream):
    if len(set([val, stream[idx+1], stream[idx+2], stream[idx+3]])) ==4:
        print(idx+4)
        break
    
#task2
for idx, val in enumerate(stream):
    list_compare = [stream[idx+id] for id in range(14)]
    if len(set(list_compare)) ==14:
        print(idx+14)
        break