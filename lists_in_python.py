import copy
from collections import Counter

#The Basics
"""1. One of the 4 data strucuters provided by Python(as of version 3.7)
   2. Used to store homegeneous or heterogeneous data i.e a single list can hold various data types.
   3. If you come from a C or C++ background which have Arrays, Python Lists are similar to them but much more powerful.
"""

#Examples

#Basic List examples
my_first_list = [1, 2, 3, 4, 5, 1]
my_second_list = ['JSON','XML','YAML']
my_third_list = ['JAVA',1.2,'Orcale', "a+b", 7]

print(f"My First List is {my_first_list}\n")
print(f"My Second List is {my_second_list}\n")
print(f"My Third List is {my_third_list}\n")

#Methods available for Lists
"""
1) copy() used to copy one list to another
2) count() used to count the occurence of a particular element in the list. The Counter() function available
   in the collections module is a faster way if you want to count the entire list
3) insert() takes in 2 arguments a) the index at which the insert needs to happen and b) the element to be inserted
   Please make a note that if the index entered is greater than the length of the list the element 
   will always be appended to the last
4) pop() as many would already know is used to display the last inserted element. Pop is a common
   stack operation
5) reverse() and sort() are pretty self explanatory, the only point to note is that both these happen in place
   i.e. the original list is sorted or reversed. Also worth noting that sort() doesn't work for heterogeneous lists
6) append() function adds a new elemet to the end of the list
7) clear() just makes the list blank in place.
"""

#Inserting, appending and pop from a list examples
my_first_list.insert(88,55)
my_first_list.insert(3,33)
my_first_list.append(99)
print(f"My first list after inserting element is {my_first_list}\n")
print(f"Result of pop is {my_first_list.pop()}\n")
print(f"My first list after pop element is {my_first_list}\n")
print(f"The number of times 1 appears in my_first_list is {my_first_list.count(1)}\n")

#Sort and reverse a list
my_sorted_first_list = my_first_list.sort()

print(f"New list after sorting is {my_sorted_first_list}")

print(f"Original list after sorting is {my_first_list}")

#my_sorted_third_list = my_third_list.sort()


#Counting elements in a list
print("Entire counted list is--> ",Counter(my_first_list))

print("Number of times 1 occurs in the list is--> ",my_first_list.count(1))


#Slicing and Indexing Lists
"""Indexing is selecting one of the member from a list. Indexes in Python just like in any other programming language 
start with 0.Reverse indexing is also possible"""

list_index  = ['Scott','Marcus','Jesse','David','Juan']

print("Element at index 2 is ", list_index[2])

print("Element at index -2 is", list_index[-2])

"""Slicing is where you want to select more than one element from a list and follows the general rule
   list[start:end:step]
   where start = starting index
         end   = end index not inclusive of the end i.e. last element will be index[end-1]
         step  = positional skip in between start and end
"""

list_slice = [1, 4, 10, 55, 2, 32, 56, 86, 29, 90]

print(list_slice[0::3])

print(list_slice[0::4])

print(list_slice[-7:-4])

print(list_slice[::-2])

list_slice.extend((100, 101))

print(list_slice)



#List Comprehension
"""This is a way which allows us to create new lists where in the new list 
is a result of some operation be it simple or a complex"""

#Consider you want a list of squares for all the numbers from 1 to 10

list_squares_upto10 = [x**2 for x in range(11)]

print(list_squares_upto10)

"""Consider another example of preparing a list which is a combination of two lists.
The syntax and readability of such inline codes does go down but they are
still a very powerful tool for smaller operations.
"""
combined_list = [(x, y) for x in [1, 2, 4] for y in [2, 4, 5] if x != y]

print(combined_list)

list_of_negative = [-2, -10, -7, -15]

list_of_abs = [abs(x) for x in list_of_negative]

print(list_of_abs)

print(my_first_list)

#y = list(zip(*[iter(my_first_list)]*3))
print(y)


"""
In addition to the methods specific to Lists, the below Python methods are also
applicable
1. max(list)
2. min(list)
3.sorted(list)
"""
