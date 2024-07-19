#%%
def merge(list1,list2):
    combined = [] 
    list1_current = 0 
    list2_current = 0 
    while list2_current < len(list2) and list1_current < len(list1): 
        if list1[list1_current] <= list2[list2_current]: 
            combined.append(list1[list1_current]) 
            list1_current += 1 
        elif list1[list1_current] > list2[list2_current]:
            combined.append(list2[list2_current]) 
            list2_current += 1 
    if list1_current != len(list1) :
        while list1_current < len(list1):
            combined.append(list1[list1_current])
            list1_current += 1 
    elif list2_current != len(list2) :
        while list2_current < len(list2):
            combined.append(list2[list2_current])
            list2_current += 1 
    return combined 

def merge_sort(input_list):
    if len(input_list) == 1 or len(input_list) == 0:
        return input_list 
    mid_point_idx = len(input_list) // 2
    left_list = merge_sort(input_list[:mid_point_idx])
    right_list = merge_sort(input_list[mid_point_idx:])
    
    return merge(left_list,right_list)

#%%
list1 = [8,5,9,3,2,1]
merge_sort(list1)
