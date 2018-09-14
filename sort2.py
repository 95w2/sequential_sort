import easygui

msg = "Please enter CS HL students in random order"
title = "Multiple enter box"
names = ["1", "2", "3", "4", "5"]
students = easygui.multenterbox(msg, title, names)

wall = 0
copy = 0
copyIndex = 0
sortd = 0

print(students)
while sortd = 0:
	sortd = 1
	copy = students[wall]
	copyIndex = wall
	#in the case that array[wall] is already in correct position
	for i in range(wall+1, len(students)):
		if copy > students[i]:
			copy = students[i]
			copyIndex = i

			if students[i-1] > students[i]:
				sortd = 0
				#if sortd is never set to 0, rest of array is sorted
	students[copyIndex] = students[wall]
	students[wall] = copy
	#swap these		
	wall += 1
	#I am overexplaining things
	print(students)