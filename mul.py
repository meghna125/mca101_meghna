
def inc(num):
    '''
    objective : To increment the number
    input parameters :
           num : num to be incremented
           
    '''
    #approach : add one in the given number
    
    return num +1



def pred(num1):
    '''
    objective : To calculate the predecessor of the number
    user input :
            num1 : number given by the user

    '''
    i=0
    #approach : call recursive function mypred within pred function to calculate the predecessor of a number 
    def mypred(num1,i):

        if num1==0:
            return num1
        if inc(i)==num1:
            return i
        else:
            i=inc(i)
        return mypred(num1,i)
    
    return mypred(num1,i)


def mult(num1,num2):
    '''
    objective : To calculate multiplication of two numbers
    input parameters :
                 num1 : first number
                 num2 : second number
    return value : multiplication of given numbers
    '''
    #approach : call function mult function recursively
    if num1==0 or num2==0:
        return 0
    if num2==0:
        return num1
    else:
        return num1+mult(num1,pred(num2))
    
