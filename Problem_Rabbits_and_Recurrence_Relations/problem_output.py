with open('problem_input.txt') as f: 
    n_str, k_str = f.readline().split() #reads the first line of the txt file and splits it into a list of strings, then assigns each element to a variable
    n = int(n_str) #turns the string into an integer
    k = int(k_str)
#n, k = map(int, f.readline().split()) an alternative code that I want to remember

#Fn = Fn-1 + Fn-2
#n = months
#k = pairs of offspring
#1 pair to start, each newborn pair takes 1 month to reach reproduction age and then 1 month to grow the babies, 
# so in each pair's 3rd month, they have k pairs of offspring
#F1 = 1, F2 = 1
#Fn = Fn-1 + k(Fn-2)

def rabbitpairs(n):
    if n == 1 or n == 2: # base case!
        return 1
    return rabbitpairs(n-1) + k * rabbitpairs(n-2) #recursion

print(rabbitpairs(n))