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
    #            and call find_min function recursively

    if start==end:
        return min_l
    if lst[min_l]>lst[start]:
        min_l=start
        start=start+1
        return Find_min(lst,start,end,min_l)
    else:
        return Find_min(lst,start+1,end,min_l)



def Find_minimum(lst,start,end):
    
    return Find_min(lst,start,end,start)

def main():

    lst=[int(x) for x in input("Enter a list : ").split()]
    lower=int(input('Enter lower bound : '))
    upper=int(input('Enter upper bound : '))
    print('Index of minimum element :',Find_minimum(lst,lower,upper))
    
if __name__=='__main__':
    main()
