import sys
import os

swiss = ()

with open(sys.argv[1], 'r') as inf1:
    for line in inf1:
        line = line.rstrip()
        if line.startswith('AC'):
            line_split = line.split(' ')
            acNum = line_split[3:]
            for i in range(0,len(acNum)):
                if i == len(acNum)-1:
                    swiss = swiss + (acNum[i].rstrip('\n')[:-1], )
                else:
                    swiss = swiss + (acNum[i][:-1], )

with open(sys.argv[2], 'r') as inf2:
    for line in inf2:
        line = line.rstrip()
        line_split = line.split('\t')
        if line_split[0] in swiss:
            print(line)
