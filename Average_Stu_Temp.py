
list=[{"name": "mohammad", "family": "shahamati", "fizic": 16, "riazi": 17, "python": 20},
      {"name": "ahmad", "family": "mohammadi", "fizic": 10, "riazi": 11, "python": 8},
      {"name": "morteza", "family": "rajabi", "hesaban": 10, "olom": 11, "python": 8},
      {"name": "Parham", "family": "shahamati", "hesaban": 20, "olom": 20, "python": 20, "riazi": 20, "english": 20}
      ]
dic_course = {
      "fizic": " ", "riazi": " ", "python": " ", "hesaban": " ", "olom": " ", "english": " "
      }
coun = 0
list_temp = []
average = 0
for i in dic_course:
      for j in list:
            if j.get(i) != None:
                  coun +=1
                  average += j[i]
                  list_temp.append(j[i])
      list_temp.sort()
      kam_nomre = list_temp[0]
      bish_nomre = list_temp[-1]
      dic_course[i] = round((average / coun), 2)  # print(h["name"])
      for h in list:
            if i in h.keys():
                  if h[i] == kam_nomre:
                      print(f"kamtarin Nomre Course {i} = {kam_nomre}", end=" ")
                      print(h["name"], " ", h["family"])

                  if h[i] == bish_nomre:
                        print(f"Bishtarin Nomre Course {i} = {bish_nomre}", end=" ")
                        print(h["name"], " ", h["family"])
      print(f"Average Course {i} = {dic_course[i]}")
      average = 0
      coun = 0
      print(f"List Nomarat Kasb Shode = {list_temp}")
      print("***********************")
      list_temp.clear()
