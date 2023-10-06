//
// Created by Ali A. Kooshesh on 10/30/21.
//

#include "PriorityQueueInAVector.hpp"

PriorityQueueInAVector::PriorityQueueInAVector() {
    heap.push_back(0);
}

void PriorityQueueInAVector::insert(int v) {
    heap.push_back(v);

    int childIdx = heap.size() - 1, parentIdx = childIdx / 2;
    while( parentIdx > 0 && heap.at(parentIdx) > heap.at(childIdx)) {
        std::swap(heap.at(parentIdx), heap.at(childIdx));
        childIdx = parentIdx;
        parentIdx = childIdx / 2;
    }
}

int PriorityQueueInAVector::findMin() {
    // Precondition -- there is at least one element in the heap.
    return heap.at(1); // could crash the program.
}

unsigned long PriorityQueueInAVector::size() {
    return heap.size() - 1;
}

void PriorityQueueInAVector::deleteMin() {
    // Precondition -- heap is not empty.

    heap.at(1) = heap.at( heap.size() - 1 );
    heap.pop_back();
    int parentIdx = 1, childIdx = 2 * parentIdx;
    while( childIdx < heap.size() ) {
        if( childIdx + 1 < heap.size() && heap.at(childIdx+1) < heap.at(childIdx) )
            childIdx++;
        if( heap.at(parentIdx) < heap.at(childIdx))
            break;
        std::swap(heap.at(childIdx), heap.at(parentIdx));
        parentIdx = childIdx;
        childIdx *= 2;
    }

}

bool PriorityQueueInAVector::empty() {
    return size() == 0;
}