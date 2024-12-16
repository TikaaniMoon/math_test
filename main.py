import random

def generate_math_question(a, b):

    num1 = random.randint(a, b)
    num2 = random.randint(a, b)

    operator = random.choice(['+', '-', '*', '/'])

    result = f'{num1} {operator} {num2}'
    return result

print(generate_math_question(1, 300))

def check_answer(question, answer):
    try:
       answer = float(answer)
       return answer == eval(question)
    except ValueError:
        return False