import random

def generate_math_question(a, b):

    num1 = random.randint(a, b)
    num2 = random.randint(a, b)

    operation = random.choice(['+', '-', '*', '/'])

    result = f'{num1} {operation} {num2}'
    return result

def check_answer(question, answer):
    try:
       answer = float(answer)
       return answer == eval(question)
    except ValueError:
        return False

def math_quiz(num_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(num_questions):
        question = generate_math_question(1, 300)
        answer = input(f'{question} = ')
        if check_answer(question, answer):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {num_questions} вопросов.")

    if correct_answers >= num_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= num_questions * 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")

math_quiz(7)

