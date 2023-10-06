//
// Created by Ali A. Kooshesh on 5/5/21.
//

#ifndef BINOMIALQUEUES_BINOMIALQUEUE_HPP
#define BINOMIALQUEUES_BINOMIALQUEUE_HPP

/* This class provides an implementation for Binomial Queues: https://en.wikipedia.org/wiki/Binomial_heap
 * It uses a vector to represent the heap-ordered trees that form the queue.
 * Suppose the Binomial Queue consists of k tree, including null trees. Then,
 * for 0 <= i <= k - 1, heapOrderedTrees[i] is either a null pointer or it
 * points to a tree that contains 2^i nodes. We refer to this property as
 * the Binomial Queue invariant.
 *
 * The run-time of the queue operations is as follows
 * 1. Insert: O(log n)
 * 2. findMin: O(log n)
 * 3. deleteMin: O(log n)
 * 4. empty: O(1)
 * 5. size: O(1)
 * 6. merge: O(log n)
 *
 * The ADT doesn't provide an explicit merge operation even though it implements it
 * when it performs delete min.
*/

#include "BQnode.hpp"

class BinomialQueue {
public:
    BinomialQueue();
    void insert(int v);
    int findMin();
    void deleteMin();
    bool empty();
    int size();
    void print();

private:
    std::vector<BQnode *> heapOrderedTrees;
    void printHeapOrderedTree(BQnode *tree);
    BQnode *treeWithMinValue();
    void insertTreeAtIndex(BQnode *tree, int idx);
    int numNodesInTheQueue = 0;
    int assertSizeOfTree(BQnode *tree);
    void assertSizeOfBinomialQueue();

};


#endif //BINOMIALQUEUES_BINOMIALQUEUE_HPP
