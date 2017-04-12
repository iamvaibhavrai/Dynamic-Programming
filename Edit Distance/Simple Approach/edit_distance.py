def main():
    str1 = list(input())
    str2 = list(input())
    initialLenStr1 = len(str1)
    lenStr2 = len(str2)
    counter = 0
    for i in str2:
        if i not in str1:
            counter += 1
        # str2.remove(i)
        else:
            str1.remove(i)
    finalLenStr1 = len(str1)
    print(lenStr2 - initialLenStr1 + finalLenStr1)


if __name__ == '__main__':
    main()
