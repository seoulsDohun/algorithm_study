def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    string = string.replace(' ', '')

    for char in string :
        print('test', ord(char) - ord('a'))
        alphabet_occurrence_array[ord(char) - ord('a')] += 1

    return alphabet_occurrence_array


print("정답 = [3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0] \n풀이 =", find_alphabet_occurrence_array("Hello my name is sparta"))
print("정답 = [2, 1, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0] \n풀이 =", find_alphabet_occurrence_array("Sparta coding club"))
print("정답 = [2, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 3, 3, 0, 0, 0, 0, 0, 0] \n풀이 =", find_alphabet_occurrence_array("best of best sparta"))


def find_max_occurred_alphabet(string):
    # 알파벳 별로 나온 개수를 카운트한 배열
    alphabet_array_result =  find_alphabet_occurrence_array(string)

    # 가장 많이 나온 알파벳의 개수
    max_count = max(alphabet_array_result)

    # 배열에서 가장 큰 개수인 배열을 추출
    max_alphabet_index = alphabet_array_result.index(max_count)

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))