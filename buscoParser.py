
import sys
import re
completeBuscos = {}
foundGene = False
with open(sys.argv[1], 'r') as inf:
    org_name = sys.argv[1].split('.')[0][11:]
    for line in inf:
        line = line.rstrip()
        if re.search('EPrGT[0-9]{14}', line):
            split_line = line.split('\t')
            if split_line[1] == 'Complete':
                busco_id = split_line[0]
                gene_id = '>' + split_line[2] + ' ' + org_name
                completeBuscos[busco_id] = []
                completeBuscos[busco_id].append(gene_id)
with open(sys.argv[2], 'r') as inf2:
    for line in inf2:
        line = line.rstrip()
        if line.startswith('>'):
            line_split = line.split('\t')
            gene_id = line_split[0]
            if foundGene == True:
                foundGene = False
                buscoFile.close()
            for key in completeBuscos:
                if gene_id == completeBuscos[key][0].split(' ')[0]:
                    foundGene = True
                    buscoFile = open(key, 'w')
                    print(line, file=buscoFile)
        elif foundGene == True:
            print(line, file=buscoFile)
