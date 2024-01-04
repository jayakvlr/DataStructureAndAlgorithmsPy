## Linked List
![linked list](images\linkedlist01.png)
- Instead of allocating a particular number of contiguous memory locations, a linked list saves the elements in different locations. It not only stores the value but also the memory address of the next element.
- The downside is that it takes almost double the space since we need to save the addresses too.
- However, the insertion and deletion of elements at the beginning of the linked list will have a time complexity (TC) of O(1) since it only involves replacing the address of the element in the first position.
- The insertion at the end or in the middle will have a time complexity of O(n) since we can't access through an index but have to traverse through the list.
- Accessing the value of an element has a time complexity of O(n).

![Double linked list](images\doublell.png)
![comparison](images\listvsll.png)