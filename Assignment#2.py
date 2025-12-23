n=int(input("Enter the number of Student"))
if n<=0:
    exit()
marklist=[int(input(f"Enter the mark of Student:{i+1}")) for i in range(n)]
def computeavg(marklist):
    return sum(marklist)/len(marklist)
def higestmark(marklist):
    return max(marklist)
def grades(marklist):
    grade=[]
    for mark in marklist:
     if mark>=90:
        ch='A'
     elif mark>=75:
        ch='B'
     elif mark>=60:
        ch='C'
     else:
        ch='F'
     grade.append(ch)
    return grade
gradelist=[m for m in grades(marklist)]
print(f"Average:{computeavg(marklist)}")
print(f"Higest Mark:{higestmark(marklist)}")
for i,m in enumerate(gradelist,start=1):
    print(f"Student#{i}:Grade{m}")

attendence_data=[(101, ['P', 'A', 'P', 'P', 'P']),
            (102, ['P', 'P', 'P', 'P', 'P']),
            (103, ['P', 'A', 'A', 'A', 'A']),
            (104, ['P', 'A', 'A', 'A', 'P']),
            (105, ['P', 'P', 'P', 'A', 'P']),
]
def attendence_percentage(attendence_data):
  return [(m[0],m[1].count('P')/len(m[1])*100)for m in attendence_data]

def low_attendance_students(attendance_data, threshold):
    m=attendence_percentage(attendence_data)
    std=[]
    for idx,per in enumerate(m):
        percent=m[idx][1]
        if percent<threshold:
            stdlist=attendance_data[idx][0]
            std.append(stdlist)
    return std
print(low_attendance_students(attendence_data,75))

def daily_absences(attendance_data):
    return [(i[0],i[1].count('A')) for i in attendance_data]
att=attendence_percentage(attendence_data)
for id,m in att:
    print(f"Student id:{id}----->Percentage={m:.2f}%")
print(low_attendance_students(attendence_data,75))
l=daily_absences(attendence_data)
for stdid,totalabs in l:
    print(f"Student id:{stdid}\nTotal Absent={totalabs}")
