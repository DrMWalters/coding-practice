#include <iostream>
#include <vector>

/*
PROBLEM
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

    class Solution { public int[] solution(int[] A, int K); }

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given
    A = [0, 0, 0]
    K = 1

the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4

the function should return [1, 2, 3, 4]

Assume that:

        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].
*/


std::vector<int> solution(std::vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    
    //newk - if K is larger than the size of the vector then K%A.size() is the only 
    //  number of rotations that we need to do
    if(A.size() == 0){return A;}
    int newK = ((unsigned)K > A.size()) ? K%A.size() : K;
    std::vector<int> B;
    
    //B - elements of A that need to start at the beginning of new vector
    for(auto it = A.end() - newK; it != A.end(); ++it){B.push_back(*it);}

    //B - other elements can just go on the end
    for(auto it = A.begin(); it != A.end() - newK; ++it){B.push_back(*it);}
    
    return B;
}

int main()
{
    std::vector<int> A{1,2,3,4,5,6,7,8,9};
    int K = 0;

    std::cout << "Original vector: [1,2,3,4,5,6,7,8,9]" << std::endl;
    std::cout << "Input number of rotations: ";
    std::cin >> K;

    std::cout << "The output vector is now: ";
    std::vector<int> B = solution(A,K);

    std::cout << "[";
    for(auto it = B.begin(); it != B.end(); ++it){
        std::cout << *it;
        if(it != B.end() - 1){std::cout << ",";}
    }
    std::cout << "]";

    std::cin.clear();
    std::cin.ignore();
    std::cin.get();

    return 0;
}