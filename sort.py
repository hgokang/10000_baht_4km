class Sort:

    def sort(arr, revese=False):
        
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if revese:
                    if arr[j] < arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                else:
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr


lis = [10.2,10,20.5,15.6]

x = Sort.sort(lis, revese=True)
print(x)


