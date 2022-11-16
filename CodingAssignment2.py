def divisible(m,n):
    if(n%m == 0): #if statement that checks whether or not the input m divides into n with no remainder
        output = [True,(n/m)] # if m divides into n a list is created in which the first index is true and the second index is m * k to get n
        return output # returns output
    else: # if m does not divide into n
        return False #returns false
    
def congruent(a,b,n): 
    difference = a-b # takes the difference between a and b in which would be used later to see if n divides into the difference with no remainder
    if(difference < 0): # if statements that checks if the difference is a negative
        difference = difference * -1 # converst the negative difference to positve by multiplying a negative 1
    if(difference%n == 0): # if statement that checks if n divides into the difference with no remainder
        output = [True,(difference/n)] # if so, a list is created with the first index being true, and the second index being k such that a = b + nk to get a
        return output # returns output
    else: # if n does not divide into the difference with no remainder
        return False # return false


#testing functions
output = divisible(5,10)
print("Divisible:")
print(output)
print("-------------------------------------------------")
print("Congruent:")
output = congruent(4,28,3)
print(output)