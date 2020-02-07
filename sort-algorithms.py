def insertion_sort(numbers): # O(n^2)
    for i in range(1, len(numbers)): # looping over all the numbers starting at index of 1
        current_number = numbers[i] # save each number into a temporary variable 
        j = i 
        while j > 0 and current_number < numbers[j - 1]: # loop intil we reach the end of array or the number we are comparing is not smaller then its neighbor
            numbers[j] = numbers[j-1] # move the left number over to the right 1 spot
            j -= 1
        numbers[j] = current_number # save the temporary number in its correct spot
    return numbers


def dividing_function(data):
    left = []
    pivot = data[0]
    right = []

    for val in data[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)

    return left, pivot, right

def quick_sort(number):
    # base case 
    if len(number) <= 1:
        return number

    left, pivot, right = dividing_function(number)

    # sort
    return quick_sort(left) + [pivot] + quick_sort(right)



    # Merge Sort

    


