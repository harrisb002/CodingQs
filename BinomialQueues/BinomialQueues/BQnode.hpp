//
// Created by Ali A. Kooshesh on 5/5/21.
//

#ifndef BINOMIALQUEUES_BQNODE_HPP
#define BINOMIALQUEUES_BQNODE_HPP

#include<vector>

/*
 * A Binomial Queue node hold a value (an int in our implementation) and
 * uses a vector to keep track of its children. It is a passive class in
 * that it doesn't impose any value or structural property on its children.
 */

class BQnode {
public:
    BQnode(int v);

    int value();
    int value() const;
    void print();

    void addChild(BQnode *child);
    const std::vector<BQnode *> &children();
    const std::vector<BQnode *> &children() const;

private:
    int nodeValue;
    std::vector<BQnode *> _children;
};


#endif //BINOMIALQUEUES_BQNODE_HPP
