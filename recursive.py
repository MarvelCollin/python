def printing():
    name = input("input nama anda > ")

    if name == "kenisha":
        print(name)
    else:
        printing()

def fibonacci(n, a = 0, b = 1):
    if n > 0:
        print(a, end=" ")
        fibonacci(n - 1, b, a + b)

def findMinMax(arr, i, end, min = 10000, max = 0): # 3,5,1,30,35
    if i < end:
        if arr[i] < min:
            min = arr[i]

        if arr[i] > max:
            max = arr[i]

        i += 1
        return findMinMax(arr, i, end, min, max)
    else: # selesai
        return min, max


def main():
    # printing()
    arr = [3,1,8,9,10,29,30,35]
    #      0 1 2 3 4 5 6 7
    # size = len(arr)
    # arrSorted = sorted(arr)
    # arr.sort()
    # print(arr)
    # for i in r                                                                                                        ange(0, size):
    #     if i == 0:
    #         print(arr[i])
    #     elif i == size - 1:
    #         print(arr[i])
    #     else:
    #         continue


    # for i in range(0, size):
    #     if arr[i] < min:
    #         min = arr[i]
    #
    #     if arr[i] > max:
    #         max = arr[i]

    # print(min, max)
    # min = 1000000
    # max = 0

    # min, max = findMinMax(arr, 0, size - 1)
    # print(min, max)
main()
