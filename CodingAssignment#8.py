#this function checks the graph and the coloring and if it is correct
def isColoring(graph,coloring):
    #store the list of keys from the graph in a list
    gkeys = list(graph.keys())
    #base boolean for correct coloring in which we would want to find one instance of wrong coloring
    correct_coloring = True
    #loop that goes through the list of keys
    for key in gkeys:
        #loop that goes through each element of the key
        for element in graph[key]:
            #if statement that checks if the current color of the element is the same as the key's color 
            if(coloring[element] == coloring[key]):
                #sets boolean to False meaning that adjacent vertices are the same color
                correct_coloring = False
    #returns boolean based on if the function found one instance of wrong coloring or if the function found no issue with the coloring
    return correct_coloring

#this function determines if a given graph is connected or not connected
def connected(graph):
#store the list of key from a given graph
    keys = list(graph.keys())
#creates an empty list called used_keys 
    used_keys = []
#while loop boolean
    loop = True
#sets the base key to the first key in the list of keys
    key = keys[0]
#appends the key to used_keys
    used_keys.append(key)
#base counter of 1 because we already are using the first key in which we will check from that key if the 
#graph is connected
    counter = 1
#while loop in which will keep going until it reaches a point where the keys appended are already in
    while(loop == True):
    #base boolean that checks if the list of elements in a key are already in used_keys
        already_in = True
    #for loop that goes through each element of the key
        for element in graph[key]:
    #checks whether or not the element is in used_keys
            if(element not in used_keys):
                #appends the key
                used_keys.append(element)
                #sets the already_in to false
                already_in = False
        #if counter is equal to length of keys then we have reached the end
        if(counter == len(keys)):
            #stops loop
            loop = False
        else:
            #if that checks if nothing is appened and we are at the last integer of the list of used_keys
            if(already_in and counter == len(used_keys)):
                #stop loop
                loop = False
            else:
                #continues loop
                key = used_keys[counter]
                counter += 1
    #checks to see if the list of keys we found are equal to the entire list of keys in the graph
    if(len(used_keys) != len(keys)):
        #returns false if the lists are not the same meaning the graph is not connected
        return False
    else:
        #returns true if the lists are the same which means that the graph is conncected
        return True

#this function determines if a given graph is a tree
def isTree(graph):
    #uses the connected function to first determine if the graph is connected and stores the result in a boolean
    isConnected = connected(graph)
    #if statement that checks the result of the connected function,
    #if the function is connected then it will check for cycles in the graph
    #if the function is not connected then it will return false
    if(isConnected):
        #stores the list of keys from the dictionary in a list
        keys = list(graph.keys())
        #empty list of used_keys, used for checking if we have been to that vertices already
        used_keys = []
        #empty list of edges, used for comparing the number of keys and edges
        edges = []
        #loop that goes through each key in the list
        for key in keys:
            #appends the key that we are using to used_keys list
            used_keys.append(key)
            #goes through each element in the key
            for element in graph[key]:
                #checks if the element is not in used keys
                if element not in used_keys:
                    #if element is not in used keys append it to edges
                    edges.append(element)
        #checks if the number of keys is greater then the number of edges
        #if edges is less than keys by 1 then there is no cycle
        if(len(used_keys) > len(edges)):
            #returns true if number of keys is greater than number of edges by 1
            return True
        #checks if the number of keys and number of edges have the same amount
        #if they are equal to each other then we have a cycle in the graph in which returns false
        if(len(used_keys) == len(edges)):
            #returns false if number of keys is equal to number of edges
            return False
    else:
        #returns false if the graph is not connected
        return False

#test functions ----------------------------------------------

graph = {
    "a": ["b"],
    "b": ["c","a"],
    "c": ["b", "d"],
    "d": ["c"]
}

coloring = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 4
}

not_tree = {
    1: [2,3],
    2: [1,3],
    3: [1,2,4],
    4: [3]
}

tree = {
    1: [2],
    2: [1,3],
    3: [2,4],
    4: [3]
}

big_tree = {
    1:[2,3],
    2:[1,4,5],
    3:[1,6,7],
    4:[2,8],
    5:[2],
    6:[3],
    7:[3,10,12],
    8:[4,9],
    9:[8,16,17],
    10:[7,11],
    11:[10],
    12:[7,13,14],
    13:[12],
    14:[12,15],
    15:[14],
    16:[9],
    17:[9,18],
    18:[17,19],
    19:[18,20],
    20:[19]
}

mid_tree = {
    1:[2],
    2:[1,3],
    3:[2,4],
    4:[3,5],
    5:[4,6],
    6:[5]

}

output = isColoring(graph,coloring)
print("isColoring: " + str(output))
output = isTree(tree)
print("Correct Tree: " + str(output))
output = isTree(not_tree)
print("Incorrect Tree: " + str(output))
output = isTree(big_tree)
print("Big Tree: " + str(output))
output = isTree(mid_tree)
print("Mid Tree: " + str(output))
