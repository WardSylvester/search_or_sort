# Ward Sylvester
# CSC 500
# HW Assignment #9

# importing relevant libraries
import random
import datetime


# defining functions

# function to find out if user wants to search or sort
def search_or_sort():
    flag = True
    while flag:
        ss = input("Enter '1' to search, enter '2' to sort: ")
        if ss == '1':
            flag = False
        elif ss == '2':
            flag = False
    return ss


# function that will be used to create lists to search/sort
def generate_lst():
    lst = []
    for x in range(50000):
        lst.append(random.randint(1,100))
    return lst

# sorting functions


# selection sort function, O(n^2)
def selection_sort():
    start_time = datetime.datetime.now()
    lst = generate_lst()

    for i in range(0,len(lst)-1):
        minIndex = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[i], lst[minIndex] = lst[minIndex], lst[i]
    elapsed_time = datetime.datetime.now() - start_time
    return elapsed_time


# insertion sort function, O(n^2)
def insertion_sort():
    start_time = datetime.datetime.now()
    lst = generate_lst()

    for i in range(1,len(lst)):
        curNum = lst[i]
        for j in range(i-1,-1,-1):
            if lst[j] > curNum:
                lst[j+1] = lst[j]
            else:
                lst[j+1] = curNum
                break
    elapsed_time = datetime.datetime.now() - start_time
    return elapsed_time


# merge sort function, O(n log (n))
def merge_sort(lst):
    start_time = datetime.datetime.now()
    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                lst[k] = lefthalf[i]
                i += 1
            else:
                lst[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1
    elapsed_time = datetime.datetime.now() - start_time
    return elapsed_time



# quick sort function, O(n^2) (worst case), O(n log n) (average case)
def quick_sort(quick_sort_lst):
    start_time = datetime.datetime.now()
    
    less = []
    equal = []
    greater = []

    if len(quick_sort_lst) > 1:
        pivot = quick_sort_lst[0]
        for x in quick_sort_lst:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        elapsed_time = datetime.datetime.now() - start_time
        return elapsed_time
    else:
        return quick_sort_lst

# searching functions


# sequential search function
def sequential_search(item):
    start_time = datetime.datetime.now()
    
    lst = generate_lst()

    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
            break
        else:
            pos += 1
    elapsed_time = datetime.datetime.now() - start_time
    return elapsed_time, found, (pos+1)


# binary search function
def binary_search(lst,item):
    first = 0
    last = len(lst) - 1
    found = False

    while (first <= last and not found):
        mid = (first + last) // 2
        if lst[mid] == item:
            found = True
            break
        else:
            if item < lst[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found, (mid+1)


# quicksort function that returns lst instead of elapsed time and index (for binary search function)
def quick_sort2(lst):
    less = []
    equal = []
    greater = []

    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort2(less) + equal + quick_sort2(greater)
    else:
        return lst


# function to do sorting and print out elapsed times
def sort():
    print("Selection sort elapsed time: " + str(selection_sort()))
    print("Insertion sort elapsed time: " + str(insertion_sort()))
    merge_sort_lst = generate_lst()
    print("Merge sort elapsed time: " + str(merge_sort(merge_sort_lst)))
    quick_sort_lst = generate_lst()
    print("Quick sort elapsed time: " + str(quick_sort(quick_sort_lst)))


# function to do searching and print out elapsed times
def search():
    flag = True
    while flag:
        try:
            item = int(input("Enter a number to search for: "))
            if item > 0:
                flag = False
            else:
                print("Enter a positive number.")
        except:
            print("You did not enter a number.")
    ss_elapsed_time, ss_found, ss_position = sequential_search(item)
    if ss_found == False:
        print("Sequential search elapsed time: " + str(ss_elapsed_time) + "...Number is not in list.")
    else:
        print("Sequential search elapsed time: " + str(ss_elapsed_time) + "...Number is in list at position " + str(ss_position))
    bs_start_time = datetime.datetime.now()
    binary_search_lst = generate_lst()
    sorted_list = quick_sort2(binary_search_lst)
    bs_found,bs_position = binary_search(sorted_list,item)
    bs_elapsed_time = datetime.datetime.now() - bs_start_time
    if bs_found == False:
        print("Binary search elapsed time: " + str(bs_elapsed_time) + "...Number is not in list.")
    else:
        print("Binary search elapsed time: " + str(bs_elapsed_time) + "...Number is in list at position " + str(bs_position))


def main():
    ss = search_or_sort()
    if ss == '1':
        search()
    if ss == '2':
        sort()


main()






        

     

