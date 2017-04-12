def getFibonacciNumber(check,num):
    if num < 2:
        check[num] = num
    if check[num] is None:
        check[num] = getFibonacciNumber(check,num-1) + getFibonacciNumber(check,num-2)
    return check[num]

def main():
    num = int(input())
    check = [None]*100
    print(getFibonacciNumber(check,num))

if __name__ == '__main__':
    main()
