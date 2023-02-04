def conflictinfo(meetings):
    n = len(meetings)
    conflicts = 0
    conflict_time = 0
    for i in range(n):
        for j in range(i+1, n):
            meeting1 = meetings[i].split(",")
            meeting2 = meetings[j].split(",")
            start1 = int(meeting1[0])
            start2 = int(meeting2[0])
            duration1 = int(meeting1[1])
            duration2 = int(meeting2[1])
            
            
            if (start1 < 0 or start1 > 2400 or start2 < 0 or start2 > 2400 or
                duration1 < 0 or duration1 > 90 or duration2 < 0 or duration2 > 90):
                return "error"
            
            
            end1 = start1 + duration1
            end2 = start2 + duration2
            if end1 > start2 and start1 < end2:
                conflicts += 1
                conflict_time += min(end1, end2) - max(start1, start2)
                
    if conflicts > 0:
        return "conflict," + str(conflicts) + "," + str(conflict_time)
    else:
        return "good"


print(conflictinfo)(1,15)