def validate_input(num1, num2, operation):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Numbers must be numeric!")
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Operation must be +, -, *, or /")
