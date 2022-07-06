import contextlib


def TotalScore(args):
    totalScore = 0
    for scores in args: totalScore += scores
    return totalScore
def Average(args): return TotalScore(args) / len(args)
def rank1(studentDict):
    Korean, Math, Science, information, total = {}, {}, {}, {}, {}
    for name, scores in studentDict.items():
        Korean[name] = scores["국어"]
        Math[name] = scores["수학"]
        Science[name] = scores["과학"]
        information[name] = scores["정보"]
        total[name] = scores["평균"]
    Korean = dict(sorted(Korean.items(), key=lambda x : x[1], reverse=True))
    Math = dict(sorted(Math.items(), key=lambda x : x[1], reverse=True))
    Science = dict(sorted(Science.items(), key=lambda x : x[1], reverse=True))
    information = dict(sorted(information.items(), key=lambda x : x[1], reverse=True))
    total = dict(sorted(total.items(), key=lambda x : x[1], reverse=True))
    return Korean, Math, Science, information, total
def rank2(Dict1):
    Dict2 = {}
    for key, value in Dict1.items(): 
        Dict2[key] = list(Dict1.values()).index(value)+1
    return Dict2
def subjectDictChoose(subject):
    if subject == "국어": return kor
    elif subject == "수학": return math
    elif subject == "과학": return sci
    elif subject == "정보": return info

studentDict = {}

while True:
    select = input('='*100+"\n입력/출력/끝내기 중 하나를 입력하세요 : ")
    print('='*100+'\n')
    if select == "끝내기": break
    elif select == "입력":   
        name = input('='*100+"\n학생의 이름을 입력하세요 : ")
        if name in list(studentDict.keys()): 
            print("동명이인이면 ㅇㅇ1, ㅇㅇ2 로 구분해주세요.\n"+'='*100, end="\n\n")
            continue
        a = list(map(lambda n:int(n), input("학생의 점수를 입력하세요. (국어, 과학, 수학, 정보 순, 띄어쓰기로 구분) : ").split(" ")))
        a.append(Average(a))
        studentDict[name] = {}
        for key, value in zip(["국어", "과학", "수학", "정보", "평균"], a): studentDict[name][key] = value
        print('='*100+'\n')
    elif select == "출력":
        kor, math, sci, info, total=rank1(studentDict)
        while True:
            select = input('='*100+f"\n다음중 하나를 입력하세요.\n{'='*100}\n| 학생 인적 사항 | 교과별 등수 | 총점 등수 | 끝내기 | : ")
            if select == "끝내기": break
            elif select == "학생 인적 사항":
                name = input(f"현재 입력된 학생들: {', '.join(list(studentDict.keys()))}\n학생의 이름을 입력해주세요 : ")
                if name not in studentDict.keys():
                    print(f"{'='*100}\nERROR : There isn't the student whose name is '{name}'\n{'='*100}")
                    continue
                else:
                    des = f"""
                    이름 : {name}
                    {'='*50}
                    국어 | 점수 : {studentDict[name]['국어']} | 등수 : {rank2(kor)[name]}
                    과학 | 점수 : {studentDict[name]['과학']} | 등수 : {rank2(sci)[name]}
                    수학 | 점수 : {studentDict[name]['수학']} | 등수 : {rank2(math)[name]}
                    정보 | 점수 : {studentDict[name]['정보']} | 등수 : {rank2(info)[name]}
                    평균 | 점수 : {studentDict[name]['평균']} | 등수 : {rank2(total)[name]}
                    총점 | 점수 : {studentDict[name]['평균']*4} | 등수 : {rank2(total)[name]}
                    {'='*50}
                    """
                    print(des)
            elif select == "교과별 등수": 
                sn = input("과목을 입력해주세요 : ")
                subject = subjectDictChoose(sn)
                if not subject: 
                    print("존재하는 교과목을 입력해주세요.")
                    continue
                des = f"""
                과목 : {sn}
                {'='*50}"""
                for name, score in subject.items():
                    des+=f"""
                {list(subject.values()).index(score)+1}등 | {name:^30} {score}점"""
                print(des)
            elif select == "총점 등수":
                des = f"""
                {'='*50}"""
                for name, score in total.items():
                    des+=f"""
                {list(total.values()).index(score)+1}등 | {name:^30} | {score}점"""
                print(des)
            else: continue
    else: continue