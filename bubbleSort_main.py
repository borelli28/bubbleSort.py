

# Bubble Sort Algorithm will bubble the biggest elements to end of the array. Bubble Sort is: Quadratic O(N^2)
def bubble_sort(list):

    unsorted_until_index = len(list) - 1    # Used to keep track of up to which element the list is unsorted, to which the whole list is unsorted so it equals at the last element of the list
    sorted = False                          # Used to keep track whether the list is fully sorted or not


# While list is not sorted. Goes until the list is completely sorted
    while not sorted:

        sorted = True       # This will change to false if we make at least one swap in the list

        for i in range(unsorted_until_index):
            if list[i] > list[i + 1]:               # Compare every pair of adjacent values(one element and the next element(+1) )
                sorted = False                      # Change to false because we made a swap. So than means the list is not sorted
                list[i], list[i + 1] = list[i + 1], list[i]     # Swap the adjacent elements if they are out of order

        unsorted_until_index = unsorted_until_index - 1     # We sorted the biggest element to the right of the list. So we decrease the number of unsorted elements in the list by 1


#
list = [65, 55, 45, 35, 25, 15, 10]
bubble_sort(list)
print(list)
