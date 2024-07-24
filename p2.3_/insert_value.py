import random
from django.db import transaction
from app1.models import student, course

# Create student instances

student(usn="1BI21CS001", name="Arun", sem=6).save()
student(usn="1BI21CS002", name="ram", sem=6).save()
student(usn="1BI21CS003", name="srinivas", sem=6).save()
student(usn="1BI21CS004", name="pravin", sem=6).save()
student(usn="1BI21CS005", name="shyam", sem=6).save()
student(usn="1BI21CS007", name="fahim", sem=6).save()
student(usn="1BI21CS007", name="prakash", sem=6).save()
student(usn="1BI21CS008", name="zahid", sem=6).save()
student(usn="1BI21CS009", name="john", sem=6).save()
student(usn="1BI21CS010", name="ben", sem=6).save()
student(usn="1BI21CS011", name="james", sem=6).save()
student(usn="1BI21CS012", name="joseph", sem=6).save()
student(usn="1BI21CS013", name="jose", sem=6).save()
student(usn="1BI21CS014", name="virat", sem=6).save()
student(usn="1BI21CS015", name="johncena", sem=6).save()
student(usn="1BI21CS016", name="roman", sem=6).save()
student(usn="1BI21CS017", name="rock", sem=6).save()
student(usn="1BI21CS018", name="stonecold", sem=6).save()




course(courseCode='21CS61', courseName='SE', courseCredits=3).save()
course(courseCode='21CS62', courseName='FSD', courseCredits=3).save()
course(courseCode='21CS63', courseName='CGV', courseCredits=3).save()
course(courseCode='21CS64', courseName='DBMS', courseCredits=3).save()
course(courseCode='21CSL62', courseName='FSD Lab', courseCredits=2).save()