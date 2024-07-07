def perform_operation(num1, num2, operation):
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'subtract':
        print(num1 - num2)
    elif operation == 'multiply':
        print(num1 * num2)
    elif operation == 'divide':
        division = num1 / num2
        if num2 == 0:
            return 'Zero division Error'
        else:
            print(division)

