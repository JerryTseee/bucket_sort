def insertion_sort(bucket):
    #to sort the entries in bucket with insertion sort
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j>=0 and bucket[j] > key:
            bucket[j+1] = bucket[j]
            j -= 1
        bucket[j+1] = key

def bucket_sort(arr):
    n = len(arr)#get the length of the array
    buckets = [ [] for _ in range(n) ]#initialize the bucket

    #put array elements in different buckets
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    #sort every bucket using insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    #concatenate all buckets into arr[]
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1#increment the index

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("sorted array: ")
print(arr)