# 자카드 유사도 검색시 A B 모두 공집합일 경우 자카드 유사도 == 1
# 영문자만 유효, 특수문자 공백은 모두 버립
# 원소 대소문자 차이 무시 => A == a
# 들어온 문자열 2개씩 묶기

# 다중원소 집합 만들기 함수
def multidiagram(list_1):
    multi_list = []
    for idx in range(1, len(list_1)):
        if list_1[idx - 1:idx + 1].isalpha() == True:
            ab = list_1[idx - 1:idx + 1].lower()
            multi_list.append(ab)
    # print("----------------------")
    return multi_list


def solution(str1, str2):
    multistr1 = multidiagram(str1)
    multistr2 = multidiagram(str2)
    print(multistr1, multistr2)
    print("------------------------------")

    """
    if len(multistr1) == 0 or len(multistr2) == 0:
      return 65536
  """

    # 합집합


    multistr1_1 = multistr1.copy()
    multistr2_1 = multistr1.copy()
    for i in multistr2:
        if i not in multistr1_1:
            multistr2_1.append(i)
        else:
            multistr1_1.remove(i)
    print(multistr2_1)
    # 합집합 multistr2_1

    print("-------------------------------------")
    # 교집합
    multistr1_2 = multistr1.copy()
    multistr2_2 = multistr2.copy()
    common = []
    for j in multistr2_2:
        if j in multistr1_2:
            multistr1_2.remove(j)
            common.append(j)
    print(common)
    # 교집합 common

    try:
        return int((len(common) / len(multistr2_1)) * 65536)
    except:
        return 65536