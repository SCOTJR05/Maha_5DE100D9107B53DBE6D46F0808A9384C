class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
  student("Hariprasath", "U316", 7.8),
  student("Maha", "U326", 9.6),
  student("Rajadurai", "U340", 8.0),
  student("Dinesh", "U311", 8.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                    
student.roll_number,
                                                     student.cgpa))
  