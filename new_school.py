import datetime


def counting():
    jot = []
    with open('student_report.txt', 'r') as re:
        read = re.readlines()
        classes = ['GRADUATION CLASS : Second Class Upper\n', 'GRADUATION CLASS : Second Class Lower\n',
                   'GRADUATION CLASS : Third Class\n', 'GRADUATION CLASS : PASS\n', 'GRADUATION CLASS : First Class\n']
        for items in read:
            if items in classes:
                jot.append(items)
    with open('student_grad.txt','w') as write:
        for item in jot:
            write.writelines(item)
        write.close()


def student_total():
    with open("student_grad.txt", "r") as j:
        lines = j.readlines()
        number = len(lines)
        print(f"The total number of students = {number}")


def student_stats():
    with open("student_grad.txt", "r") as jeep:
        values = jeep.readlines()
        fir = []
        sec = []
        thi = []
        fou = []
        fif = []
        for values in values:
            first = "GRADUATION CLASS : First Class\n"
            second = "GRADUATION CLASS : Second Class Upper\n"
            third = "GRADUATION CLASS : Second Class Lower\n"
            fourth = "GRADUATION CLASS : Third Class\n"
            fifth = "GRADUATION CLASS : PASS\n"
            if values == first:
                fir.append(values)
            elif values == second:
                sec.append(values)
            elif values == third:
                thi.append(values)
            elif values == fourth:
                fou.append(values)
            else:
                fif.append(values)

    with open("student_stats.txt", "w") as keep:
        keep.write(f"Students with First Class = {len(fir)}\n")
        keep.write(f"Students with Second Class Upper = {len(sec)}\n")
        keep.write(f"Students with Second Class Lower = {len(thi)}\n")
        keep.write(f"Students with Third Class = {len(fou)}\n")
        keep.write(f"Students with a PASS  = {len(fif)}")
        keep.close()

    do_tal = len(fir) + len(sec) + len(thi) + len(fou) + len(fif)
    print(f"{(len(fir)/do_tal)*100}% of students are First Class Students")
    print(f"{(len(sec) / do_tal) * 100}% of students are Second Class Upper Students")
    print(f"{(len(thi) / do_tal) * 100}% of students are Second Class Lower Students")
    print(f"{(len(fou) / do_tal) * 100}% of students are Third Class Students")
    print(f"{(len(fif) / do_tal) * 100}% of students had a normal Pass")


print("Welcome To St. Johns School ")
prompt = int(input("1. Add Student. \n 2. Check Number Of Students. \n 3. Check Student Statics \n 4.Remove Student: "))
if prompt == 1:
    name = input("name: ")
    department = input("Department name: ")
    number_courses = int(input("How Many Of Courses: "))
    limit = number_courses + 1
    gp_total = []
    hours = []
    while limit > 1:
        limit = limit - 1
        with open('courses&credits.txt', 'a+') as screed:
            course = input(f"course{limit }: ")
            score = int(input(f"{course}: "))
            credit_hours = int(input("credit hours: "))
            screed.write(f'{course}   ||    {score}     ||       {credit_hours}   \n')
            screed.write("-----------------------------------------------------------\n")
        screed.close()
        if score > 0:
            if score > 80:
                gp = 4.0 * credit_hours
            elif score > 75:
                gp = 3.85 * credit_hours
            elif score > 70:
                gp = 3.5 * credit_hours
            elif score > 65:
                gp = 3.0 * credit_hours
            elif score > 60:
                gp = 2.5 * credit_hours
            elif score > 55:
                gp = 2.0 * credit_hours
            elif score > 45:
                gp = 1.0 * credit_hours
            else:
                gp = 0.0
            gp_total.append(gp)
            hours.append(credit_hours)

    hour = 0
    for value in hours:
        hour = hour + value
    print(hour)

    total = 0
    for values in gp_total:
        total = total + values
    gpa = total/hour
    print(gpa)
    if gpa >= 3.6:
        grad_class = "First Class"
    elif gpa >= 3.0:
        grad_class = "Second Class Upper"
    elif gpa > 2.5:
        grad_class = "Second Class Lower"
    elif gpa >= 2.0:
        grad_class = "Third Class"
    elif gpa >= 1.0:
        grad_class = "PASS"

    now = datetime.datetime.now()
    with open("student_report.txt", "a+") as f:
        f.write("\n")
        f.write("-----------------------------------------------------------\n")
        f.write(f"D@TE:{now.day}/{now.month}/{now.year}\n")
        f.write(f"NAME: {name}                   DEPARTMENT: {department} \n")
        f.write(f"GPA : {gpa}                    CREDIT HOURS: {hour}\n")
        f.write(f"GRADUATION CLASS : {grad_class}\n")
        f.write("-----------------------------------------------------------\n")
        f.close()
        with open('courses&credits.txt', 'r') as xx, open('student_report.txt', 'a+') as yy:
            for lines in xx:
                yy.write(lines)
        xx.close()
        yy.close()
    with open("student_grad.txt", "a+") as ced:
        ced.write(f"{grad_class} \n")
        ced.close()
    with open('courses&credits.txt', 'w') as clean:
        clean.write('')
    clean.close()
    counting()
    student_total()
    student_stats()
elif prompt == 2:
    student_total()
elif prompt == 3:
    student_stats()
elif prompt == 4:
    student_name = input('Name of Student: ')
    number_courses = int(input('Number of courses: '))
    pops = []
    with open('student_report.txt', 'r') as pop:
        scripts = pop.readlines()
        tops = [scripts]
        before_pop = enumerate(scripts)
        for index, script in before_pop:
            if student_name in script:
                for word in scripts[index-3: index + 4 + number_courses*2]:
                    scripts.remove(word)
    with open('student_report.txt', 'w') as wr:
        wr.writelines(scripts)
        wr.close()
    counting()
    student_stats()
    student_total()

