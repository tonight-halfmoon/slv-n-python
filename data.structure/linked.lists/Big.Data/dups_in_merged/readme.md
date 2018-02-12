# Duplicates in Merged Two Linked Lists avoiding Exponential n^2 Traverse

## Key Idea

> Attribute `__has_been_visited`

> Mark a node visited the first traverse

> Check if it has never been visited while traversing the map keys

... 
if nxtNode.ck_data() in dict_ and nxtNode.is_visited() == False:                                dict_[nxtNode.ck_data()] += 1
...

That is it!


## Future Work

> This is only a very sample prototype and not applicable for real-world project. Python is not made for recursive functions calls. And the defintion is heavily recursive. Just for fun, curiousity and learning. However, in future, it would be nice to implement the logic in a way to handle really Long and Big Data Linked Nodes.

> The Unit Testing provided in [Dups in Merged Tests](./dups_in_merged/dups_in_merged_tests.py) are not enough. Only very short linked lists provided with realy one special case - Two Linked Lists are merged at some node later and continue as one linked list. In real life, there will be more complex use cases which not yet has been thought of.
