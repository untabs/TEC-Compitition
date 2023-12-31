MINIMUM = 32
  
def find_minrun(n): 
  
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sort(a, left, right):
    a = a[left:right]
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1

    # our list of pigeonholes
    holes = [0] * size

    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1

    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
    return a
              
def merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        array = insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size
    return array

array = [-1,5,0,-3,11,9,-2,7,0] 
  
print("Array:") 
print(array) 
  
array = tim_sort(array) 
  
print("Sorted Array:") 
print(array)