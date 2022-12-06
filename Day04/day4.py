with open('Day04/input.txt') as f:
    lines = [x for x in f.read().split('\n')]

#part1
score=0
for val in lines:
    pair = val.split(',')
    pair1 = pair[0].split('-')
    pair2 = pair[1].split('-')
    
    if int(pair1[0])>= int(pair2[0]) and int(pair1[1])<=int(pair2[1]):
        score+=1

    elif int(pair2[0])>= int(pair1[0]) and int(pair2[1])<=int(pair1[1]):
        score+=1

print(score)

#part2
score=0
for val in lines:
    pair = val.split(',')
    pair1 = pair[0].split('-')
    pair2 = pair[1].split('-')
    
    
    if int(pair1[0])>= int(pair2[0]) and int(pair1[0])<= int(pair2[1]):
        score+=1
    elif int(pair1[1])<=int(pair2[1]) and int(pair1[1])>=int(pair2[0]):
        score+=1
    elif int(pair2[0])>= int(pair1[0]) and int(pair2[0])<=int(pair1[1]):
        score+=1
    elif int(pair2[1])<= int(pair1[1]) and int(pair2[1])>=int(pair1[0]):
        score+=1
        
print(score)
