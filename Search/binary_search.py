def main():

    l = [0,1,2,3,4,5,6,7,8,9]
    print binary_search(l, 12, 0, 9)

def binary_search(data, target, low, high):

    if low > high:
        return -1 
    else:
        mid = (high+low)/2

        if target == data[mid]:
            return mid
        elif target > data[mid]:
            return binary_search(data, target, mid+1, high)
        else:
            return binary_search(data, target, low, mid-1)

if __name__ == "__main__":
    main()
