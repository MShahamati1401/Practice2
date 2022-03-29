# barnameh daryaft tedad na moshakhas daneshjoo va tedad na moshakhase darse va print moadel , kamtarin nomre va bishtarin nomre
# Program's Entrance
# daryaft vorodi az karbar
i = 0
list = []#jahate zakhire etelaate daneshjoo dar dictionary va zakhire har dictionary dar list
list_temp = []# jahate zakhire kam va bishtarin nomre an darse
average = 0
flag_number = True
flag_student = True
dic_course = {} # jahate bodvi dorose vared shode va sabte moadel an darse
while flag_student:
    students_number = input("Please Inter Students Number and for exit typed "'"exit"'": ")
    if students_number == "exit":
        print("End Program")
        flag_student = False
        break
    globals()[f"dic{i}"] = {}# Jahate tolid moteghayer dictionary dynamic ta betonam dar list zakhire konam
    globals()[f"dic{i}"]["students_number"] = students_number
    name_stu = input("Please Inter student name: ")
    family_stu = input("Please Inter student family: ")
    globals()[f"dic{i}"]["name"] = name_stu
    globals()[f"dic{i}"]["family"] = family_stu
    while flag_number:
        course_name = input("Please Inter Course Name and type exit to leave for next Student : ")
        if course_name == "exit":
            flag_number = False
            print("etmam vorode nomre darse haye daneshjoo")
            break
        dic_course[course_name] = ""
        course_number = input("Please Inter Course Number: ")
        globals()[f"dic{i}"][course_name] = course_number
    list.append(globals()[f"dic{i}"])
    print(list)
    print(dic_course)
    flag_number = True
##############################################################################
coun = 0
list_temp = []
average = 0
for i in dic_course:# be ezaye tamam drose daneshjoo haye vared shode
    for j in list:# tamam daneshjoo ha ra peymayesh mikonad
        if j.get(i) is not None:
            coun += 1
            average += float(j[i])
            list_temp.append(j[i])
    list_temp.sort()
    kam_nomre = list_temp[0]
    bish_nomre = list_temp[-1]
    dic_course[i] = round((average / coun), 2)
    for h in list:
        if i in h.keys():
            if h[i] == kam_nomre:
                print(f"kamtarin Nomre Course {i} = {kam_nomre}", end=" ** ")
                print("Shomare Daneshjoo : ", h["students_number"], " ", h["name"], " ", h["family"])

            if h[i] == bish_nomre:
                print(f"Bishtarin Nomre Course {i} = {bish_nomre}", end=" ** ")
                print("Shomare Daneshjoo : ", h["students_number"], " ", h["name"], " ", h["family"])
    print(f"Average Course {i} = {dic_course[i]}")
    average = 0
    coun = 0
    print(f"List Nomarat Kasb Shode dar in cousre = {list_temp}")
    print("***********************")
    list_temp.clear()

