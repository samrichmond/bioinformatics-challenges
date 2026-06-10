d = {}
b = ''
with open('problem_input.txt') as f: 
    for line in f:
        text = line.strip()
        if text.startswith('>'):
            n = text[1:]
            d[n] = b
        if text.startswith(('A', 'G', 'C','T')): #could just be and else statement since there's only 2 types of lines
            d[n] = d[n] + text #b += text
for key, value in d.items():
    count_G, count_C = value.count('G'), value.count('C')
    length = len(value)
    d[key] = ((count_G + count_C) / length ) * 100

#suggested code - revisit this
#gc_percentages = {} 
#for key, sequence in d.items():
    #gc_count = sequence.count('G') + sequence.count('C')
    #percentage = (gc_count / len(sequence)) * 100
    #gc_percentages[key] = percentage

max_key = max(d, key=d.get) #max iterates over dict d, key=d.get says for each key, usue d.get(key) to get the value to compare, and max finds the key whose value is the largest
print(max_key)
print(d[max_key]) 


#notes/brainstorming
#with open('problem_input.txt') as f: 
 #   s = f.read().replace('\n','')
#l = s.split('>')

    #format correctly
    #split between >
    #could make into a dictionary. with key:value being rosalind_xxxx : AGTC
    #for each key, get length of value and number of gc, calculate percentage, need to associate percentage with the key, make new dict?
    #then print the key and value of highest dict value?
    #read each line, if it begins iwth a > (dont htink i can do this)
    #can't determine by line becaues sometimes there's 2 lines of dna. 
    #split by >
    # d = {} 
    # d['key'] = 1 => d = {'key':1}
    #del d['key']
    #otehr way to keep association with name and percentage, is create a list of the highest percentages first, and at the same time create a list with the names orderer...
# >name /n abababab /n gcgcgc /n >name
#what if i combine the entirity of the txt file as one string, then split it by >
#if line starts with > 
# first, change add this string as key in dict , set a variable x to this key, then add it to dict as key
#if next line starts with A,G,T or C, add it as the value to the key x in dict