def path(n): 
    dict = { #creates an empty dictionary in which the vertices and arcs will be appended later
    }
    for x in range(n): #loops through each integer up to n-1 (i.e, 0,1,2,3,4,...,n-1)
        if(x != (n-1)): #checks to see if counter, x, is not equal to the last index which is n-1
            vert = {x:[x+1]} #creates a dictionary, vert, in which x is the vertex(key) and x+1 are the arcs
            dict.update(vert) #takes the original dictionary above and updates it by appending it to dict
    return dict #returns the final dictionary

def bitGraph(L):
    dict = { #creates an empty dictionary in which the key and corresponding arcs will be appended later
    }
    for i in range(len(L)): #loops through the length of the list L in which i is a counter that starts at 0
        arc = [] #list in which would contain the arcs for the key and resets when the loop takes increments
        for j in range(len(L)): #loops through the length of the list in which j is a counter that starts a 0. 
            if(L[i] == L[j]): # checks to see if the elements in L[i] are equal to L[j]
                if(i != j):   # checks to see if the counters are not equal
                    arc.append(j) #if the counters are not equal it will take the index of L[j] in which is equal to L[i] and append it to the arc list
        vert = {i:arc} #creates a dictionary in which i is the key and arc is the list of arcs that have the same element as L[i] but not including L[i]
        dict.update(vert) #updates the original dictionary and appends the vert to it
    return dict #returns the final dictionary

def firstBeatsSecond(A,B):
    dict = { #creates an empty dictionary in which the key and corresponding arcs are appened to later
    }
    for x in range(len(A)): #loops through the length of the list A in terms of x being the index of it
        vert = {A[x]:B} # creates a dictionary in wich A[x] is the key and B is the list of arcs
        dict.update(vert) # updates the dictionary by appending the vert
    return dict #returns the final dictionary


#test cases
print("-----path-----")
dictionary = path(4)
print("input: 4" )
print(dictionary)
print("-----bitGraph-----")
dictionary = bitGraph([1,0,0,1,0,1,1])
print("input: [1,0,0,1,0,1,1]" )
print(dictionary)
print("-----firstBeatsSecond-----")
A = [1,2,3]
B = ["a","b","c","d"]
dictonary = firstBeatsSecond(A,B)
print("input: lists")
print(" A = [1,2,3]")
print(" B = [a,b,c,d]")
print(dictonary)