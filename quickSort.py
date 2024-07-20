#%%
def swap(list1,index1,index2):
    temp = list1[index1] 
    list1[index1] = list1[index2] 
    list1[index2] = temp 

def pivot(list1,pivot_index, end_index):
    swap_index = pivot_index 
    for i in range(pivot_index+1,end_index+1):
        if list1[pivot_index] > list1[i]:
            swap_index += 1 
            swap(list1,swap_index,i)
    
    swap(list1,pivot_index,swap_index)
    return swap_index

def quickSort(list1,index1, index2): 
    if index1 < index2:
        swap_index = pivot(list1,index1,index2)
        quickSort(list1,index1,swap_index-1) 
        quickSort(list1,swap_index+1,index2)
        return list1
    
    
    
list1 = [4,6,1,7,3,2,5,8,9]
quickSort(list1,0,len(list1)-1)
list1