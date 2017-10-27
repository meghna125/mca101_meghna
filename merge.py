import pdb

pdb.set_trace()
def merge(l1,l2):
    
    '''
    objective : To merge two sorted lists recursively
    input parameters :
              l1 -> list1 of sorted elements
              l2 -> list2 of sorted elements
    return value : return merged list l3
    
    '''
    l3=[]
    if l1==[] and l2==[]:
        return l3
    elif l1!=[] and l2==[]:
        return l3+l1
    elif l1==[] and l2!=[]:
        return l3+l2
    elif l1[0]<l2[0]:
        l3.append(l1[0])
        return l3+merge(l1[1:],l2)
    elif l1[0]>l2[0]:
        l3.append(l2[0])
        return l3+merge(l1,l2[1:])
    




def main():
    '''
    '''

    l1=[int(x) for x in input("Enter numbers in a list : ").split()]
    l2=[int(x) for x in input("Enter numbers in a list : ").split()]
    l1.sort()
    l2.sort()
    print('List 1 : ',l1)
    print('list 2 : ',l2)
    print("Merged list : ",merge(l1,l2))
    

if __name__=="__main__":
    main()
