Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> room_numbers = {
...     'CSC101': '3004',
...     'CSC102': '4501',
...     'CSC103': '6755',
...     'NET110': '1244',
...     'COM241': '1411'
... }
>>> instructors = {
...     'CSC101': 'Haynes',
...     'CSC102': 'Alvarado',
...     'CSC103': 'Rich',
...     'NET110': 'Burke',
...     'COM241': 'Lee'
... }
>>> meeting_times = {
...     'CSC101': '8:00 a.m.',
...     'CSC102': '9:00 a.m.',
...     'CSC103': '10:00 a.m.',
...     'NET110': '11:00 a.m.',
...     'COM241': '1:00 p.m.'
... }
>>> course_number = input("Enter a course number: ")
Enter a course number: CSC101
>>> 
>>> if course_number in room_numbers:
...     print(f"Room Number: {room_numbers[course_number]}")
...     print(f"Instructor: {instructors[course_number]}")
...     print(f"Meeting Time: {meeting_times[course_number]}")
... else:
...     print("Course not found.")
... 
...     
Room Number: 3004
Instructor: Haynes
Meeting Time: 8:00 a.m.
>>> 
