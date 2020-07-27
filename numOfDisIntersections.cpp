#include <iostream>
#include <cmath>
#include <vector>
#include <tuple>
#include <list>
#include <algorithm>
#include <unordered_map>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

typedef unsigned long int unsgned_int;

int solution(std::vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)
    
    std::unordered_map<unsgned_int, std::vector<int> > umap;
    unsgned_int pairs = 0;
    unsgned_int maxPairs = 10000000;
    bool debug = false;
    
    for(unsgned_int i = 0; i < A.size(); ++i){
        if(debug){std::cout << "Centre = (" << i << ",0) Radius = " << A[i] << std::endl;}
        
        std::vector<int> v;
        v.clear();
        umap[i] = v;
        //intersects to the left

        if(debug){std::cout << "LEFT" << std::endl;}
        for(unsgned_int j = 0; j != i; ++j){
            
            if( abs(i - j) < abs(A[i] + A[j]) ){
                //if umap[j] does not contain i then add otherwise continue
                auto it = find( umap[j].begin(), umap[j].end(), i);
                if( it == umap[j].end()){
                    if(debug){std::cout << "\t For i = " << i << " and j = " << j << std::endl;}
                    if(debug){std::cout << "\t Adding centre (" << j << ",0) with rad = " << A[j] << std::endl;}
                        umap[i].push_back(j);
                }
            }
        }
        
        
        if(debug){std::cout << "RIGHT" << std::endl;}
        //centres to the right
        unsgned_int maxNum =  (i + A[i] >= A.size()) ? A.size():(i + A[i] + 1);
        for(unsgned_int j = i; j != maxNum; ++j){
            if(j == i){continue;}
            if(debug){std::cout << "\t For i = " << i << " and j = " << j << std::endl;}
            if(debug){std::cout << "\t Adding centre (" << j << ",0)" << std::endl;}
            umap[i].push_back(j);
        }
        
        pairs += umap[i].size();
        if(debug){std::cout << "Circle = (" << i << ",0) with rad" << A[i] << " PAIRS = " << (int)umap[i].size() << std::endl;}
        if(pairs > maxPairs){return -1;}
        
        if(debug){std::cout << "#####" << std::endl;}
    }
    

    
    return pairs;
}

int solutionv2(std::vector<int> &A) {
    // write your code in C++14 (g++ 6.2.0)

    std::list< std::tuple<int,bool> > circle_endpoints;
    

    
    return 0;
}

int main()
{

    std::vector<int> A;

    std::cin.clear();
    std::cin.ignore();
    std::cin.get();

    return 0;
}