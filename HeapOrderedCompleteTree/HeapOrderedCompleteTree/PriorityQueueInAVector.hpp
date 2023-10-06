//
// Created by Ali A. Kooshesh on 10/30/21.
//

#ifndef HEAPORDEREDCOMPLETETREE_PRIORITYQUEUEINAVECTOR_HPP
#define HEAPORDEREDCOMPLETETREE_PRIORITYQUEUEINAVECTOR_HPP
#include <vector>

class PriorityQueueInAVector {
public:
    PriorityQueueInAVector();
    void insert(int v);
    void deleteMin();
    int findMin();
    bool empty();
    unsigned long size();

private:
    std::vector<int> heap;
};


#endif //HEAPORDEREDCOMPLETETREE_PRIORITYQUEUEINAVECTOR_HPP
