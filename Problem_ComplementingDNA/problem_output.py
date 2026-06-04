with open('problem_input.txt') as f:
    s = f.read().strip()

#1. reverse string
#2. match each letter of s to it's complement

rev = s[::-1] #reverse string
rc = '' #new string to be returned later
for i in rev: #complementing DNA
    if i == 'A':
        rc = rc + 'T'
    if i == 'T':
        rc = rc + 'A'
    if i == 'G':
        rc = rc + 'C'
    if i == 'C':
        rc = rc + 'G'
print(rc)

#remember: string.replace('A', 't'), then later upper case everything