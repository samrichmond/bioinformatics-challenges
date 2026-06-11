with open('problem_input.txt') as f: 
    s = list(f.readline().strip()) #strips the first line of breaks or spaces, then turns each character into items of a list
    t = list(f.readline().strip()) 

muts = 0
for i in range(len(s)):
    if s[i] != t[i]:
        muts += 1

print(muts)

#Notes for future
#Could use zip() function to loop over items from multiple loops in parallel and retursn as an iterator of tuples
        