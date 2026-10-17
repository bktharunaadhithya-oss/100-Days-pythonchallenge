# ==========================================
# DAY 3: Operators & Conditional Logic
# ==========================================

print("--- Welcome to Day 3 Project: The Smart Decision Maker ---")

# Part 1: Arithmetic & Comparison Operators
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nAddition: {num1} + {num2} = {num1 + num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Exponentiation (Power): {num1} ** {num2} = {num1 ** num2}")

# Using a modulus operator to check for even/odd numbers
if num1 % 2 == 0:
    print(f"-> {num1} is an EVEN number.")
else:
    print(f"-> {num1} is an ODD number.")

# Part 2: Advanced Conditionals (If-Elif-Else)
print("\n--- Next Challenge: Grade Classifier ---")
score = float(input("Enter your exam score (0 to 100): "))

# Decision-making logic based on ranges
if score >= 90:
    grade = "A"
    message = "Excellent work! You are rocking Python!"
elif score >= 80:
    grade = "B"
    message = "Great job! Keep pushing harder."
elif score >= 70:
    grade = "C"
    message = "Good effort, but there is room to grow."
elif score >= 60:
    grade = "D"
    message = "You passed, but you need more practice."
else:
    grade = "F"
    message = "Don't give up! Review the previous days' lessons."

# Output the decision
print(f"\nYour Grade: {grade}")
print(f"Feedback: {message}")
