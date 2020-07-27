'''


An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].


'''
'''
POSSIBLE BETTER ANSWER BELOW....
int find_missing_element(vector<int> &v) {    // Here +1 needs to find size of full sequence with 
    // the missing element
    auto v_size = v.size() + 1;
    // Find sum of all elements of the sequence
    auto sumOfAllElements = (v_size * (1 + v_size)) / 2;
    auto missing_element = sumOfAllElements - 
                           std::accumulate(v.begin(), v.end(), 0);
    return missing_element;
}
'''

def solution(A):
    # write your code in Python 3.6
    A.sort()
    print(len(A))
    for i in range(len(A)):
        if i == len(A) - 1 and A[i] == len(A): return len(A) + 1
        if A[i] != i + 1:
            return i + 1
            
    return 1

if __name__ == '__main__':

    print('Start tests..')
    assert solution([2,3,1,5]) == 4
    # assert solution([]) == 0
    # assert solution([0,1]) == 1
    # assert solution([0, 0]) == 0
    # assert solution([1,0,0,3]) == 4
    print('Ok!')

