#include <iostream>
#include <fstream>
#include "PriorityQueueInAVector.hpp"

int main(int argc, char *argv[]) {

    if (argc != 2) {
        std::cout << "usage: " << argv[0] << " nameOfAnInputFile\n";
        exit(1);
    }
    std::fstream inputStream;
    inputStream.open(argv[1], std::ios::in);
    if (!inputStream.is_open()) {
        std::cout << "Unable to open " << argv[1] << ". Terminating...";
        exit(1);
    }

    PriorityQueueInAVector heapOrderedTree;
    int value;
    while( inputStream >> value ) {  // n * log n \in O(n log n)
        heapOrderedTree.insert(value); // O(log n)
    }

    while( !heapOrderedTree.empty() ) { // n * log n \in O(n log n)
        std::cout << heapOrderedTree.findMin() << std::endl; // O(1)
        heapOrderedTree.deleteMin(); // O(log n)
    }

    // std::cout << "The heap has " << heapOrderedTree.size() << " elements.\n";
    return 0;
}

