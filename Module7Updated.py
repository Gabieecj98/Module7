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
>>> while True:
...     course_number = input("Enter a course number (or 'q' to quit): ")
...     if course_number.lower() == 'q':
...         break
...     if course_number in room_numbers:
...         print(f"Room Number: {room_numbers[course_number]}")
...         print(f"Instructor: {instructors[course_number]}")
...         print(f"Meeting Time: {meeting_times[course_number]}")
...     else:
...         print("Course not found. Please enter a valid course number.")
... 
...         
Enter a course number (or 'q' to quit): NET110
Room Number: 1244
Instructor: Burke
Meeting Time: 11:00 a.m.
Enter a course number (or 'q' to quit): CSC103
Room Number: 6755
Instructor: Rich
Meeting Time: 10:00 a.m.
Enter a course number (or 'q' to quit): COM241
Room Number: 1411
Instructor: Lee
Meeting Time: 1:00 p.m.
Enter a course number (or 'q' to quit): CSC101
Room Number: 3004
Instructor: Haynes
Meeting Time: 8:00 a.m.
Enter a course number (or 'q' to quit): CSC102
Room Number: 4501
Instructor: Alvarado
Meeting Time: 9:00 a.m.
Enter a course number (or 'q' to quit): q
