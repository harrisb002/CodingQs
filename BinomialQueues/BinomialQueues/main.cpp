#include <iostream>
#include <fstream>
#include "BinomialQueue.hpp"
#include "SmallIntMixedOperations.hpp"
#include "BinomialQueueTester.hpp"

int main(int argc, char *argv[]) {

    // This program creates and tests a Binomial Queue.
    // It requires an input file. Can test with it though.

    if (argc != 2) {
        std::cout << "usage: " << argv[0] << " nameOfAnInputFile\n";
        exit(1);
    }
    std::ifstream inputStream;
    inputStream.open(argv[1], std::ios::in);
    if (!inputStream.is_open()) {
        std::cout << "Unable top open " << argv[1] << ". Terminating...";
        exit(1);
    }

    BinomialQueue priorityQueue;
    int numTestsToRun = 1000;
    testBinomialQueue(priorityQueue, numTestsToRun);
    return 0;
/*
    int inputValue;
//    BinomialQueue priorityQueue;
    while( inputStream >> inputValue ) {
//        std::cout << "inserting " << inputValue << std::endl;
        priorityQueue.insert(inputValue);
        std::cout << priorityQueue.findMin() << std::endl;
    }

    std::cout <<"The queue contains the following values\n";
    priorityQueue.print();

    std::cout <<"Printing the values in non-decreasing order.\n";
    while( ! priorityQueue.empty() ) {
        std::cout << priorityQueue.findMin() << std::endl;
        priorityQueue.deleteMin();
    }

    return 0;
*/
}
