#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Implimentation of Minimax algorithm

# Initial values of Aplha and Beta 
MAX, MIN = 1000, -1000
nodeIndex = 0
Depth = 3         # to be defined as per the problem
Children = 2    # to be defined as per the problem

# Returns optimal value for current player  (Initially called for root and maximizer) 

def minimax(depth, nodeIndex, maximizingPlayer,values): 

# Terminating condition. i.e  leaf node is reached 
    if depth == Depth:                                  # the integer to be updated based on the depth of the input tree
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = MIN
        # Recur for all the children 
        for i in range(0, Children):                      #The range to be updated based on the no. of childer  in each level
            val = minimax(depth + 1, nodeIndex * Children + i,False, values) 
            best = max(best, val)   
            print(depth+1,nodeIndex * Children + i,best,val)
        return best 

    else: 
        best = MAX
        # Recur for all the children 
        for i in range(0, Children):        #The range to be updated based on the no. of childer  in each level
            val = minimax(depth + 1, nodeIndex * Children + i,True, values) 
            best = min(best, val)  
            print(depth+1,nodeIndex * Children + i ,best,val)
        return best 

# Driver Code 
if __name__ == "__main__": 

    values = [3, 5, 6, 9, 1, 2, 0, -1] #depth 3, child 2
    #values = [3,12,8,2,4,6,14,5,2] #depth 2, child 3
    #values = [2,7,6,8] #depth 2, child 2
    print(values)
    print("The optimal value is :", minimax(0, nodeIndex, True, values)) 


# In[ ]:





# In[ ]:




