def Find_min(lst,start,end,min_l):
    '''
    objective : return index of the minimum element in the given sublist
    input parameters :
                lst-> list of elements
                start->starting index of the sublist
                end->last index of the sublist
                min_l->minimum index of the element
     return value : index of minimum element
     '''
    #approach : compare list[min_l] with list[start_l],if greater swap the indexes
    #           and call find_min function recursively

    if start==end+1:
        return min_l
    if lst[min_l]>lst[start]:
        min_l=start
        start=start+1
        return Find_min(lst,start,end,min_l)
    else:
        return Find_min(lst,start+1,end,min_l)



def Find_minimum(lst,start,end):
    
    return Find_min(lst,start,end,start)



def selsort(lst,i=0):
    if len(lst)==i:
        return lst
    else:
        min_i=Find_minimum(lst,i,len(lst)-1)
        temp=lst[i]
        lst[i]=lst[min_i]
        lst[min_i]=temp
        return selsort(lst,i+1)



lst=[5,7,3,8,9,2,1,0]
print('Sorted list : ',selsort(lst))

