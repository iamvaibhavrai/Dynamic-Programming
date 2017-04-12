def editDistance(str1,str2,lenStr1,lenStr2):
    result = [[0 for i in range(lenStr2+1)] for j in range(lenStr1+1)]
    for i in range(lenStr1+1):
        for j in range(lenStr2+1):
            if i == 0:
                result[i][j] = i
            elif j == 0:
                result[i][j] = j
            elif str1[i-1] == str2[j-1]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = 1 + min(result[i-1][j],result[i][j-1],result[i-1][j-1])
    return result[i][j]

def main():
    str1 = list(input())
    str2 = list(input())

    edit_distance = editDistance(str1,str2,len(str1),len(str2))
    print(edit_distance)


if __name__ == '__main__':
    main()
