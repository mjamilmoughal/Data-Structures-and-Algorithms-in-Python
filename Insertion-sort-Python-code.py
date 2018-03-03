
# coding: utf-8

# In[1]:

array=[31,41,59,26,41,58]


# In[2]:

def sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=key
            


# In[3]:

sortedArray=sort(array)


# In[6]:

for i in range(1,len(array)):
    print(array[i], ' ')


# In[ ]:



