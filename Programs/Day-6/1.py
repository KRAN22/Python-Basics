# 1. Write a code to accept data for a file until the choice of the user is 'NO'
import os

dir = os.getcwd()
print(f"dir :{dir}")

dir = "C:\Users\kd67152\PycharmProjects\ZensarProject\day-6"
os.chdir(dir)
print(os.getcwd())
print("-" * 40)

files = os.listdir()
# print(files)
lst = []
for file in files:
    if file.endswith(".py"):
        lst.append(file)

FL = open("C:\\Users\\kd67152\\PycharmProjects\\ZensarProject\\day-6\\data.txt", "w")
for file in lst:
    FL.write(file + " => " + str(os.path.getsize(file)) + "\n")
FL.close()
