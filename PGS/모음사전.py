
cnt = -1
answer = 0
def dfs(mother, word, speak, depth):
    global cnt
    global answer
    cnt += 1
    if speak == word:
        #print(speak, cnt)
        answer = cnt
        return
    if depth == 5:
        return

    dfs(mother, word, speak + mother[0], depth+1)
    dfs(mother, word, speak + mother[1], depth+1)
    dfs(mother, word, speak + mother[2], depth+1)
    dfs(mother, word, speak + mother[3], depth+1)
    dfs(mother, word, speak + mother[4], depth+1)

    return


def solution(word):
    # 여기서 word 는 target이나 다름없다.
    # aeiou 문자 리스트 만들기
    mother = ['A', 'E', 'I', 'O', 'U']

    # 길이는 최대 5글자인것을 명심 dfs로 조합을 순회한다. uuuuu까지 출력하는 함수만들기
    # dfs(mother, target == word, idx)
    # dfs(mother, word, idx)

    # for i in range(4):
    dfs(mother, word, '', 0)

    return answer