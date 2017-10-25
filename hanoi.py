
def hanoi(n,source,spare,target):
    '''
    objective : To build tower of hanoi using n number of disks and 3 poles 
    input parameters :
                 n -> no of disks
                 source : starting position of disk
                 spare : auxillary position of the disk
                 target : end position of the disk
    '''
    #approach : call hanoi function recursively to move disk from one pole to another
    assert n>0
    if n==1:
        print('Move disk from ',source,' to ',target)
    else:
        hanoi(n-1,source,target,spare)
        print('Move disk from ',source,' to ',target)
        hanoi(n-1,spare,source,target)
