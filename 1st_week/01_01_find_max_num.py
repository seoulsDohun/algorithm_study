def find_max_num(array):
    maxNum = array[0]
    for i in array:
        print(i)
        if maxNum < i:
            maxNum = i

    return maxNum

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 8, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 1888 ,9, 2, 7 ]))