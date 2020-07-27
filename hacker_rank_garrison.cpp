#include <iostream>
#include <vector>



int main()
{
    std::vector<int> A{1,2,3,4,5,6,7,8,9};
    int K = 0;

    std::cout << "Original vector: [1,2,3,4,5,6,7,8,9]" << std::endl;
    std::cout << "Input number of rotations: ";
    std::cin >> K;

    std::cin.clear();
    std::cin.ignore();
    std::cin.get();

    return 0;
}