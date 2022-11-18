def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    
    for answer in answers:
        if s1[0] == answer: scores[0] += 1
        if s2[0] == answer: scores[1] += 1
        if s3[0] == answer: scores[2] += 1
        
        s1.append(s1.pop(0))
        s2.append(s2.pop(0))
        s3.append(s3.pop(0))
    
    res = [i+1 for i, score in enumerate(scores) if score == max(scores)]       # 최댓값의 인덱스+1을 res에 저장
    res.sort()
    
    return res