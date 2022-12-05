with open('C:/repos/AdventOfCode2022/Day05/input.txt') as f:
    lines = [x for x in f.read().split('\n')]
    
    
#print(lines[8])

a = [x.replace(' ', '0').replace(']', '0').replace('[', '0') for x in lines[:8]]


list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]
list_7=[]
list_8=[]
list_9=[]
list_tot=[list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]
list_tot2=[list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]

for val in reversed(a):
    for id, chr in enumerate(val):
        if not chr.isnumeric():
            if id==1:
                list_1.append(chr)
            elif id==5:
                list_2.append(chr)
            elif id==9:
                list_3.append(chr)
            elif id==13:
                list_4.append(chr)
            elif id==17:
                list_5.append(chr)
            elif id==21:
                list_6.append(chr)
            elif id==25:
                list_7.append(chr)
            elif id==29:
                list_8.append(chr)
            elif id==33:
                list_9.append(chr)

#task1
#print(list_1, '\n', list_2, '\n', list_3, '\n', list_4, '\n', list_5, '\n', list_6, '\n', list_7, '\n', list_8,'\n', list_9)
for val in lines[10:]:
    #print(val)
    if len(val)==18:
        #list_pop = list_tot[int(val[12])-1]
        #list_add = list_tot[int(val[17])-1]
        if len(list_tot[int(val[12])-1][-int(val[5]):])==1:
            list_tot[int(val[17])-1].extend(list_tot[int(val[12])-1][-int(val[5]):])
        else:
            list_tot[int(val[17])-1].extend(list(reversed(list_tot[int(val[12])-1][-int(val[5]):])))
        list_tot[int(val[12])-1]=list_tot[int(val[12])-1][:-int(val[5])]
        
        #print(list_tot[0])
    elif len(val)==19:
        #print(val[5:7])
        if len(list_tot[int(val[13])-1][-int(val[5:7]):])==1:
            list_tot[int(val[18])-1].extend(list_tot[int(val[13])-1][-int(val[5:7]):])
        else:
            list_tot[int(val[18])-1].extend(list(reversed(list_tot[int(val[13])-1][-int(val[5:7]):])))
        list_tot[int(val[13])-1]=list_tot[int(val[13])-1][:-int(val[5:7])]
    else:
        print(val)
      
#print(list_tot)
for val in list_tot:
    if len(val) != 0:
        print(val[-1]) 

print('-----------') 
 
      
#task2     
#comment out task 1 first  
for val in lines[10:]:
    #print(val)
    if len(val)==18:
        #list_pop = list_tot[int(val[12])-1]
        #list_add = list_tot[int(val[17])-1]

        list_tot2[int(val[17])-1].extend(list_tot2[int(val[12])-1][-int(val[5]):])

        list_tot2[int(val[12])-1]=list_tot2[int(val[12])-1][:-int(val[5])]
        
        #print(list_tot[0])
    elif len(val)==19:
        list_tot2[int(val[18])-1].extend(list_tot2[int(val[13])-1][-int(val[5:7]):])
        list_tot2[int(val[13])-1]=list_tot2[int(val[13])-1][:-int(val[5:7])]
    else:
        print(val)
        
#print(list_tot)
for val in list_tot2:
    if len(val) != 0:
        print(val[-1])