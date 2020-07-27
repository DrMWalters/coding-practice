'''


A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.


'''
def solutionA(X, Y, D):
    frogPos = X
    numOfJumps = 0
    while frogPos <= Y:
        numOfJumps += 1
        frogPos += D
        
    return numOfJumps
    
def ceilDiv( a, b ):
    return -(-a//b)


def solution(X, Y, D):
    # write your code in Python 3.6
    
    if X >= Y: return 0

        
    return ceilDiv( Y - X,D )

if __name__ == '__main__':

    print('Start tests..')
    assert solution(10 , 85, 30) == 3
    # assert solution([]) == 0
    # assert solution([0,1]) == 1
    # assert solution([0, 0]) == 0
    # assert solution([1,0,0,3]) == 4
    print('Ok!')