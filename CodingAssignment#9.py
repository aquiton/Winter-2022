#This function takes in a connected graph and returns a spanning tree in the form of a dictionary
def spanningTree(graph):
    #list of keys from the connected grpah
    keys = list(graph.keys())
    #empty dictionary that will hold the edges and vertices of the spanning tree
    spanning_tree = {
    }
    #base boolean for while loop
    loop = True
    #base case dictionary for the starting vertex of the spanning tree
    vert = {keys[0]: [graph[keys[0]][0]]}
    #update the spanning_tree dictionary with the base case vertex
    spanning_tree.update(vert)
    #list of keys that we have already used
    used_keys = []
    #append the basecase vertex
    used_keys.append(keys[0])
    #counter for the for loop in which will be updating the keys
    key_counter = 0
    #while loop that starts at the base case vertex
    #examines the adjacent edges and vertices
    #chooses one of the vertices in which is not in the used_keys list
    #and creates and small dictionary(vert) and then appends it to the spanning_tree dictionary
    #then checks if the loop has to stop
    #if not update the loop for the next vertices
    while (loop == True):
        #goes through each element of the previous key's element
        for element in graph[spanning_tree[used_keys[key_counter]][0]]:
            #checks if the element is not in used)keys
            if(element not in used_keys):
                #sets the element as connector; edge
                connector = [element,used_keys[key_counter]]
                break   
        #creates sub dictionary in which uses the 
        vert = {spanning_tree[used_keys[key_counter]][0] : connector}
        #updates the spanning_tree dictionary with the sub dictionary
        spanning_tree.update(vert)
        #appends the just used key to the used_keys list
        used_keys.append(spanning_tree[used_keys[key_counter]][0])
        #if statement that checks when to stop the loop
        #if the length of the list of keys in the given dictionary - 1 is equal to the length of the used_keys then stop the while loop
        if(len(keys) - 1 == len(used_keys)):
            #set loop to false
            loop = False
        #contiunes the loop
        else:
            #increments the key_counter by 1
            key_counter += 1
    #when the while loop is done it will return the spanning_tree
    return spanning_tree

#test cases -----

connected_graph = {
    1 :[2,4,5,6],
    2 :[1,3,4],
    3 :[2,4],
    4 :[1,2,3,5],
    5 :[1,4,6],
    6 :[1,5]
}

graph_two = {
    1 :[2,4],
    2 :[1,3],
    3 :[2,4],
    4 :[3,5],
    5 :[4]
}

output = spanningTree(connected_graph)
print(output)
output = spanningTree(graph_two)
print(output)
