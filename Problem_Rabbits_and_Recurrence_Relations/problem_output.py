with open('problem_input.txt') as f: 
    n_str, k_str = f.readline().split() #reads the first line of the txt file and splits it into a list of strings, then assigns each element to a variable
    n = int(n_str) #turns the string into an integer
    k = int(k_str)
#n, k = map(int, f.readline().split()) an alternative code that I want to remember

#Fn = Fn-1 + Fn-2



