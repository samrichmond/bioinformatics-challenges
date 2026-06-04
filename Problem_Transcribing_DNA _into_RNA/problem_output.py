with open('problem_input.txt') as f:
    t = f.read().strip()

rna = ''
for base in t:
    if base == 'T':
        rna += 'U'
    else:
        rna += base

print(rna)