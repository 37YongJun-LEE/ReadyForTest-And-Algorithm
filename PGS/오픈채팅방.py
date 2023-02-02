def solution(record):
    answer = []
    chatUser = dict()
    inout_dic = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for log in record:
        try:
            inout, uid, nick = log.split()
            chatUser[uid] = nick
        except:
            continue

    for log in record:
        try:
            if len(log.split()) == 3:
                inout, uid, nick = log.split()
                answer += [chatUser[uid] + inout_dic[inout]]
            elif len(log.split()) == 2:
                inout, uid = log.split()
                answer += [chatUser[uid] + inout_dic[inout]]
        except:
            continue

    return answer