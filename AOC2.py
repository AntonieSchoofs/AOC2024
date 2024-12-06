reports = open("C:\\Users\\Antonie\\Documents\\AOC 2023\\input.txt").readlines()



ans = 0

reports_all = []


for i in range(len(reports)):
    reports[i] = reports[i].strip("\n").split(" ")
    reports_i = []
    reports_i.append(reports[i])
    for j in range(len(reports[i])):
        reports_i.append(reports[i][:j] + reports[i][j+1:])
    reports_all.append(reports_i)

#print(reports_all)

for reports in reports_all:
    reports_safety = 0
    for report in reports:
        report_safety = True
    
        if int(report[0]) > int(report[1]):
            increasing = False
        else:
            increasing = True
    
        for i in range(len(report) - 1):
            if increasing:
                dif = int(report[i+1]) - int(report[i])
            else:
                dif = int(report[i]) - int(report[i+1])
        
            if dif > 3 or dif < 1:
                report_safety = False
                #print(report)

    
        if report_safety:
            reports_safety += 1
    
    #print(reports_safety)

    if reports_safety > 0:
        ans += 1

print(ans)
