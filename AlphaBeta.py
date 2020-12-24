#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Implementation of Alpha-Beta Pruning 

# Initial values of Aplha and Beta 
MAX, MIN = 1000, -1000
Depth = 3         # to be defined as per the problem
Children = 2    # to be defined as per the problem


# Returns optimal value for current player #(Initially called for root and maximizer) 

def minimax(depth, nodeIndex, maximizingPlayer,values, alpha, beta): 

# Terminating condition. i.e  leaf node is reached 
    if depth == Depth: 
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = MIN

        # Recur for left and right children 
        for i in range(0, Children): 
            val = minimax(depth + 1, nodeIndex * Children + i,False, values, alpha, beta) 
            best = max(best, val)  
          # Alpha Beta Pruning 
            if best < beta : 
                alpha = max(alpha, best) 
            
        return best 

    else: 
        best = MAX

        # Recur for left and  right children 
        for i in range(0, Children): 
            val = minimax(depth + 1, nodeIndex * Children + i,True, values, alpha, beta) 
            best = min(best, val) 
            # Alpha Beta Pruning 
            if best  > alpha: 
                 beta = min(beta, best)  
        return best 

# Driver Code 
if __name__ == "__main__": 

    values = [3, 5, 6, 9, 1, 2, 0, -1]  #depth 3, child 2
    #values = [3,12,8,2,4,6,14,5,2] #depth 2, child 3
    
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX)) 

 


# In[ ]:




