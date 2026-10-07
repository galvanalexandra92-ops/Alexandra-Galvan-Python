graduation_year = 2026
grade = 95
gpa = 3.9
is_grad_student = True

print(graduation_year, type(graduation_year))
print(grade, type(grade))
print(gpa, type(gpa))
print(is_grad_student, type(is_grad_student))

name = input("What is your name? ")
start_year = int(input("What year did you start? "))

years_in_program = graduation_year - start_year

print(f"Hi, {name}! Your program takes approximately {years_in_program} years.")

credits_per_course = float(input("Enter the credits per course: "))
num_courses = float(input("Enter the number of courses: "))

total_credits = credits_per_course * num_courses

print(f"{credits_per_course} × {num_courses} = {total_credits}")

# Receipt (variables and print only, no input)
item_name = "Graduate Credit Hours"
price = 350.00
quantity = total_credits

total = price * quantity

print("=" * 12)
print("TUITION RECEIPT".center(36))
print("=" * 12)
print(f"Student:   {name}")
print(f"Item:      {item_name}")
print(f"Price:     ${price:,.2f} per credit")
print(f"Quantity:  {quantity:g}")
print("-" * 12)
print(f"Total:     ${total:,.2f}")
print("=" * 12)
