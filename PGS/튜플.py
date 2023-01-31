def solution(s):
    answer = []

    s = s.strip("{}")

    s = s.split("},{")

    new = []
    for i in s:
        new.append(i.split(","))

    new.sort(key=len)
    # print(new)

    for x in new:
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))

    return answer



#############################################
# 첫 시도 솔루션...
"""
def solution(s):
    answer = []
    find_int = ''
    answer2 = []
    answer3 =[]
    
    for s_word in s:
        if s_word != "{" and s_word != "}":
            find_int += s_word
            #print(find_int)
            
        if s_word == "}":
            find_int = find_int.strip(',')
           # print(find_int)
            
            if len(find_int) == 0:
                continue
            answer += [find_int]
            find_int = ''
            
    answer = sorted(answer, key=len)
   # print(answer)    
    
    for x in answer: 
        answer2 += [[int(y) for y in x.split(',')]]
    
    for y in answer2:
        for z in y:
            if z not in answer3:
                answer3.append(z)
            
        
    
    
    return answer3
"""