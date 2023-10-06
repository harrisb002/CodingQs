//
// Created by Ali A. Kooshesh on 5/5/21.
//

#include <cassert>
#include "BQnode.hpp"

BQnode::BQnode(int v) {
    nodeValue = v;
}

int BQnode::value() {
    return nodeValue;
}

int BQnode::value() const {
    return nodeValue;
}

void BQnode::addChild(BQnode *child) {
    // pre-condition: child is not a null pointer.
    // This node doesn't impose any structural or value property as that
    // is the responsibility of the user of the class.
    assert(child != nullptr);
    _children.push_back(child);
}

const std::vector<BQnode *> &BQnode::children() const {
    return _children;
}

const std::vector<BQnode *> &BQnode::children() {
    return _children;
}
