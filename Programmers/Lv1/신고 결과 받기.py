def solution(id_list, report, k):
    answer = []
    ban_list = []
    report_count = {}
    report_hash = {}
    report = list(set(report))
    
    for i in id_list:
        report_count[i] = 0
        report_hash[i] = []
    
    for i in report:
        reporter,reportee = i.split(' ')
        report_count[reportee] += 1
        
        report_hash[reporter].append(reportee)
        
    for i in report_count:
        if report_count[i] >= k:
            ban_list.append(i)
    
    for i in report_hash:
        counter = 0
        for j in report_hash[i]:
            if j in ban_list:
                counter += 1
        answer.append(counter)
    return answer

id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2

id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id_list1,report1,k1))
print(solution(id_list2,report2,k2))