l = {1, 2, 3, 4, 5}

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] in l:
        print("Yes")
    else:
        print("No")