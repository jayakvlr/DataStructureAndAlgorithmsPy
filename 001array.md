
## Array

- When code is running in CPU, the code uses RAM to store all the variables and data.
- The addresses of the RAM are in hexadecimal format.
- An int takes 4 bits and 4 mem addresses to save one integer.

### Search

- So when we access using the index, it uses the equation `address + 2∗size(integer)`.
- This is exactly one operation, so the time complexity is O(1).
- If we don't know the particular index and iterate through the array to search for the element, we have to use at most n of this equation `address + 2∗size(integer)`. That means n*(address + 2∗size(integer)), so the time complexity is O(n).

### Insertion/Deletion

- The insertion/deletion results in shifting all elements after the particular element, resulting in at most n operations.
- So the time complexity is O(n).
- `Arrayname.insert(x, i)`
- `Arrayname.remove(x)`

### Static and Dynamic Array

- Static array doesn’t allow us to increase size; dynamic does.
- Static allocates the exact memory for the array.
- Dynamic allocates a particular size initially. After that size is full, it allocates double size of the older one, copies all the elements of the old array to the new one, and inserts the new one.

## Exercise 1

Let us say your expense for every month are listed below,
- January - 2200
- February - 2350
- March - 2600
- April - 2130
- May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compared to January?
2. Find out your total expense in the first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month.
4. June month just finished, and your expense is 1980 dollars. Add this item to our monthly expense list.
5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.
