#!/usr/bin/env python
# coding: utf-8

# In[25]:


def backtrack(x,enemy_list,domain,assigned):
    if -1 not in assigned:
        return x
    v = 999
    for i in range(len(domain)):                # assign variable equal to value
        if v>len(domain[i]) and assigned[i]!=1:
            v = i
    order=[]
    #print(v)
    for i in domain[v]:                     
        mini = 1000
        for j in enemy_list[v]:        # Check for the constraints , if the same table has the enemy
            temp = len(domain[j])
            if i in domain[j]:
                temp-=1
            if temp<mini:
                mini = temp
        order.append((i,mini))
        
    order = sorted(order,key=lambda x:x[1],reverse=True)
    ordered = [i[0] for i in order]
    #print(ordered)
    for i in ordered:
        newdomain = [ [j for j in i] for i in domain]
        for j in enemy_list[v]:
            if i == x[j]:
                continue
        #print(v,i)
        x[v] = i
        assigned[v] = 1
        newdomain[v] = [z for z in newdomain[v] if z==i]         
        temp = []
        for j in range(len(newdomain)):
            if j!=v and j in enemy_list[v]:
                newdomain[j] = [z for z in newdomain[j] if z!=i]
        #print(newdomain)
        res = backtrack(x,enemy_list,newdomain,assigned)
        #print (res)
        if res!=0:
            return res
    x[v] = ""
    assigned[v] = -1
    return 0




people = int(input("Enter the number of people"))
tables = int(input("enter the number of tables"))
edges = []
line = input("enter elements of list L(people who should not sit together) till an empty newline character. ").split()
while(line):
    
     edges.append((int(line[0]),int(line[1])))
     line = input().split()
    
#edges = [(0,1),(0,4),(0,5),(1,2),(1,3),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]

x = ["" for i in range(people)] #the final answer


enemy_list = [[] for i in range(people)]   # The list contains the each ith person, who are the enemies

for i in edges:                           # The loop creates the list of list, enemieis of the ith person
    enemy_list[i[0]].append(i[1])         # i is pointing to edges list
    enemy_list[i[1]].append(i[0])

#print(enemy_list)

for i in range(people):
    j = list(set(enemy_list[i]))        # Connect the enemy list identified in the above loop, wuth the person i
    enemy_list[i] = j
assigned = [-1 for i in range(people)]    #Initialize the table assigned to each person as -1
domain = [[x for x in range(tables)] for i in range(people)]  # Initialize with all the domain for all the person

res = backtrack(x,enemy_list,domain,assigned)  # List X will hold the table assigned to each person 

if res == 0:
    print('False')
else:
    for i in range(len(res)):
        print(' {} :'.format(i),res[i])


# In[ ]:


#Output 
'''Enter the number of people8
enter the number of tables3
enter elements of list L(people who should not sit together) till an empty newline character. 0 2
0 3
0 4
1 4
1 7
2 3
2 6
3 7
3 4
4 7
5 6

 0 : 0
 1 : 1
 2 : 2
 3 : 1
 4 : 2
 5 : 1
 6 : 0
 7 : 0
'''
