# Show Duplicates in Two Linked Lists avoiding Exponential n^2 Traverse

## Key Idea

>  ´Dict_[nxt_node.ck_data()] += 1´

That is it!

## Assumption

The implemented logic assumes that the input two linked lists are absultely independent. The client must provide two independent linked lists with heads each does reference a different memory location. And there must be no node belongs to one linked list does point to a node also being pointed to by a node from the other linked list provided. In short, all nodes of a linked list must be unique for the same linked list.

## Duplicates in Merged Two Linked Lists

To traverse and show duplicate instances in two merged linked lists, an extended definition is added to class [Node](./dups_in_merged/definition/node.py). The solution is extended with extra two instructions keeping the complexity non-exponential in module [Dups in Merged](./dups_in_merged/dups_in_merged.py)