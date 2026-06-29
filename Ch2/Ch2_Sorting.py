def insertion_sort(a): #increasing order
    for j in range (1, len(a)): #2nd element start
        current = a[j]
        i = j - 1 #move left
        while i >= 0 and a[i] > current: #move elements > current to right
            a[i + 1] = a[i] #move right
            i = i - 1 #move left
        a[i + 1] = current

def reverse_insertion_sort(a): #decreasing order
    for j in range(1, len(a)): #2nd element start
        current = a[j]
        i = j - 1 #move left
        while i >= 0 and a[i] < current: #move elements < current to right
            a[i + 1] = a[i] # move right
            i = i - 1 #move left
        a[i + 1] = current

def merge(a,p,q,r): #divide & conquer
    n1 = q - p + 1 #sub array 1
    n2 = r - q
    left = [0] * (n1 + 1) #create blank arrays
    right = [0] * (n2 + 1)

    for i in range(0, n1): #left array
        left[i] = a[p + i]
    for j in range (0, n2): #right array
        right[j] = a[q + 1 + j]

    left[n1] = float('inf')
    right[n2] = float('inf')

    i = 0 #merge arrays back
    j = 0

    for k in range (p,r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1

def merge_sort(a,p,r):
    if p < r:
        q = (p + r) // 2 #// for floor division
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

def bubble_sort(a):
    for i in range(len(a) - 1): #start @ 0
        for j in range(len(a) - 1, i, (-1)): #downto
            if a[j] < a[j - 1]: #swap current w/ previous
                a[j], a[j - 1] = a[j-1], a[j] #swap if incorrect

def main():
    a = [1,5,6,2,199,2037,111,90311,3,456]

    print("Before Sorting: ", a)
    print("After Sorting: ")

    #sorted copies to use
    insertion_sorted = a.copy()
    reverse_insertion_sorted = a.copy()
    merge_sorted = a.copy()
    bubble_sorted = a.copy()

    #call methods and sorted
    insertion_sort(insertion_sorted)
    reverse_insertion_sort(reverse_insertion_sorted)
    merge_sort(merge_sorted, 0, len(merge_sorted) - 1)
    bubble_sort(bubble_sorted)

    #print
    print("Insertion Sort: ", insertion_sorted)
    print("Reverse Insertion Sort: ", reverse_insertion_sorted)
    print("Merge Sort: ", merge_sorted)
    print("Bubble Sort: ", bubble_sorted)

if __name__ == "__main__":
    main()


