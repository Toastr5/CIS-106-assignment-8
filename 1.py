
number_of_items = int(input("Enter the number of items you want in the list: "))

#question 1
list_1 = []
for item in range(number_of_items):
  item = input("Enter item: ")
  list_1.append(item)
'''
#question 2
list_1.insert(0,99)
print(list_1)

#question 3
list_1.remove(99)
list_1.insert(0,100)
print(list_1)
'''
#question 4
list_2 = ["500", "600", "700", "800", "900"]
print(list_2)
list_1.extend(list_2)
print(list_1)

#question 5
list_1.remove("800")
print(list_1)

#question 6
list_1.remove(list_1[3])
print(list_1)



#question 7
grade_list = ["A" , "B" , "C" , "A" , "B" , "C" ]

#question 8
print(grade_list.count("A"))

#question 9
print(grade_list.index("B"))

#question 10
if "F" in grade_list:
  print(grade_list.index("F"))
else:
  print("F is not in the list")

#question 11
list_2.clear()
print(list_2)

#question 12
print(list_2) #before running this, comment out questions 4,5 and 6

#question 13
players1 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players1)

#question 14
players1.sort()
print(players1)

#question 15
players2 = players1.copy()
print(f"Player list one {players1}")
print(f"Play list two {players2}")

#question 16
players2.reverse()
print(f"Player list one {players1}")
print(f"Play list two {players2}")