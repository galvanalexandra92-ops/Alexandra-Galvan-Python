graduation_year = 2026
program = "Fintech"
grade = 95
gpa = 3.9
is_grad_student = True

print(graduation_year, type(graduation_year))
print(program, type(program))
print(grade, type(grade))
print(gpa, type(gpa))
print(is_grad_student, type(is_grad_student))

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = 2026
age = current_year - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")

credits_per_course = float(input("Enter the credits per course: "))
num_courses = float(input("Enter the number of courses: "))

total_credits = credits_per_course * num_courses

print(f"{credits_per_course} × {num_courses} = {total_credits}")

# Receipt (variables and print only, no input)
item_name = "Custom Embroidered Hat"
price = 28.00
quantity = 3

total = price * quantity

print("=" * 36)
print("RECEIPT".center(36))
print("=" * 36)
print(f"Item:      {item_name}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("-" * 36)
print(f"Total:     ${total:.2f}")
print("=" * 36)

# Profile card
profile_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Share one fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))

profile_age = current_year - profile_birth_year

print("=" * 40)
print(f"PROFILE: {profile_name}".center(40))
print("=" * 40)
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {profile_age}")
print("=" * 40)
