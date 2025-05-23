# -*- coding: utf-8 -*-
"""code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e5FF-V7ffLrFi4ArXSab0xOpBWWUcqCL
"""

def add_student(students_dict, student_id, name, courses):
    students_dict[student_id] = {
        'name': name,
        'courses': courses,
        'grades': {}
    }
    print(f"دانشجو {name} با موفقیت اضافه شد!")

def add_grade(students_dict, student_id, course, grade):
    if student_id in students_dict:
        if 0 <= grade <= 20:  # شرط برای نمره
            students_dict[student_id]['grades'][course] = grade
            print(f"نمره {grade} برای درس {course} ثبت شد.")
        else:
            print("نمره باید بین 0 تا 20 باشد!")
    else:
        print("دانشجو یافت نشد!")

def calculate_average(students_dict, student_id):
    if student_id in students_dict:
        grades = students_dict[student_id]['grades'].values()
        if not grades:
            print("این دانشجو هنوز نمره‌ای ندارد.")
            return None
        average = sum(grades) / len(grades)
        return average
    else:
        print("دانشجو یافت نشد!")
        return None

def find_top_student(students_dict):
    top_student = None
    highest_avg = -1

    for student_id, info in students_dict.items():
        avg = calculate_average(students_dict, student_id)
        if avg is not None and avg > highest_avg and info['grades']:
            highest_avg = avg
            top_student = info['name']

    return top_student, highest_avg

def filter_passed_courses(students_dict, student_id, passing_grade=10):
    if student_id in students_dict:
        passed_courses = [
            course for course, grade in students_dict[student_id]['grades'].items()
            if grade >= passing_grade
        ]
        return passed_courses
    else:
        return []

# --- ایجاد دیکشنری دانشجویان و تست توابع ---
students = {}

# اضافه کردن دانشجویان
add_student(students, 1001, "علی", ["ریاضی", "فیزیک", "شیمی"])
add_student(students, 1002, "مریم", ["ادبیات", "تاریخ", "زیست"])

# اضافه کردن نمرات
add_grade(students, 1001, "ریاضی", 18)
add_grade(students, 1001, "فیزیک", 15)
add_grade(students, 1002, "ادبیات", 20)
add_grade(students, 1002, "تاریخ", 12)

# محاسبه معدل
ali_avg = calculate_average(students, 1001)
print(f"معدل علی: {ali_avg:.2f}")

# یافتن دانشجوی برتر
top_student, top_avg = find_top_student(students)
print(f"دانشجوی برتر: {top_student} با معدل {top_avg:.2f}")

# دروس قبولی مریم
maryam_passed = filter_passed_courses(students, 1002)
print(f"دروس قبولی مریم: {maryam_passed}")