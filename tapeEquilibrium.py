'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solutionA(A):
    # write your code in Python 3.6
    differences = []
    
    for p in range(1, len(A), 1):
        
        firstsum = 0
        for i in range(p):
            firstsum += A[i]
        
        secondSum = 0
        for i in range( p, len(A), 1):
            secondSum += A[i]
            
        differences.append(abs(firstsum - secondSum))
    
    return min(differences)
    
def solutionB(A):
    # write your code in Python 3.6
    differences = []
    sumAtIndexs = []
    sumAtIndex = 0
    
    for i in range(len(A)):
        sumAtIndex += A[i]
        sumAtIndexs.append(sumAtIndex)
    
    #check sumAtIndexs is non-empty
    if len(sumAtIndexs) == 0: return 0
    
    for i in range(len(sumAtIndexs)):
        differences.append(abs(sumAtIndexs[i] - (sumAtIndexs[-1] - sumAtIndexs[i])))

    
    return min(differences)

        
def solution(A):
    # write your code in Python 3.6
    right_sum = sum(A)
    left_sum = 0

    #this need to be large number (no max int in Python 3.0)
    minimal = 2**100
    for i in range(1, len(A)):
        val = A[i - 1]
        left_sum += val
        right_sum -= val

        difference = abs(left_sum - right_sum)
        if( difference < minimal ):
            minimal = difference
    
    return minimal

if __name__ == '__main__':

    print('Start tests..')
    assert solution([0,2000]) == 2000
    solution([0,1,5,7,8,4,3]) 
    # assert solution([]) == 0
    # assert solution([0,1]) == 1
    # assert solution([0, 0]) == 0
    # assert solution([1,0,0,3]) == 4
    print('Ok!')