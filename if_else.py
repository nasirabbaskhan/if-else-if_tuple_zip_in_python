# n= int(input("please enter number:")) # get user input as integer
# if n==1:
#     print(f"Today is sunday and {n}st day of week")
# elif n==2:
#     print(f"Today is Monday and {n}nd day of week")
# elif n==3:
#     print(f"Today is Tuesday and {n}rd day of week")
# elif n==4:
#     print(f"Today is Wednesday and {n}th day of week")
# elif n==5:
#     print(f"Today is Thirsday and {n}th day of week")
# elif n==6:
#     print(f"Today is Friday and {n}th day of week")
# elif n==7:
#     print(f"Today is Saturday and {n}th day of week")
# else:
#     print("Please enter betwwen 0 to 7 number")
# from typing import Union

# per:Union[int,float] = 88 or 
# per:int | float = 88.6
# grade:str | None = None

# if per>=80:
#     grade= "A+"
# elif per>=70: 
#     grade= "A"
# elif per>=60:
#     grade="B"
# elif per>=50:
#     grade="C"
# elif per>=40:
#     grade="D"
# elif per>=33:
#     grade="E"
# else:
#     grade="F"
# print(f"Your grade is {grade}")

percentage:list[float | int] = [50,70,87.7,89.5,65,86.4,32]
grades:list[str] = []
for per in percentage:
    grade:str = ""
    if (per>=0) and (per<33):
        grade= "F"
    elif (per>=33) and (per<40):
        grade= "E"
    elif (per>=40) and (per<50):
        grade= "D"
    elif (per>=50) and (per<60):
        grade= "C"
    elif (per>=60) and (per<70):
        grade= "B"
    elif (per>=70) and (per<80):
        grade= "A"
    elif (per>=80) and (per<90):
        grade= "A+"
    grades.append(grade)
print(grades)