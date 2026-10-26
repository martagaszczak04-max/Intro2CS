user = "Linus"
print("Hello, I am", user)
user = "George" # a new value 
print("Hello, I am" , user)
print(type(user))
name = "Marta" 
age = 22.5
height = 1.60
student_now = True
print(name, "is", age, "years old") 
print(type(name), type(age))
print(type(height), type(student_now))
city = "Poznan"
print(type(city)) 
slices_per_student = 3
students = 12
enrolled_students = students + 2
present_students = enrolled_students - 3
print(present_students) 
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
print(total_slices_needed)
print(cost_per_student)
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order * 8) % present_students
print(boxes_to_order)
print(leftover_slices)
print("Present students:" , present_students)
print("Total slices needed:" , total_slices_needed)
print("Cost per student:" , boxes_to_order)
print("Boxes to order:" , boxes_to_order)
print("Leftover slives:" , leftover_slices)

