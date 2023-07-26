import json

with open('15_question.json', 'r') as file:
    content = file.read()
data = json.loads(content)

correct_answer = 0
incorrect_answer = 0
cnt_answer = 0

for i in data:
    cnt_answer += 1
    last_quest = False
    if i == data[-1]:
        last_quest = True
    if last_quest:
        print("That is last question")
    answer = input(f'Answer the question: \n{i["question"]}:\n')
    if answer == i["answer"]:
        if not last_quest:
            print("Right! Next question!")
        else:
            print("Right and let's move on to scoring!")
        correct_answer += 1
    else:
        print("I'm sorry but no...")
        if last_quest:
            print("Let's move on to scoring")
        incorrect_answer += 1
print(f'Total questions: {cnt_answer}')
print(f'Correct answers: {correct_answer}')
print(f'Incorrect answers: {incorrect_answer}')
print(f'Your score: {round((correct_answer / (correct_answer + incorrect_answer) * 100), 2)}%')
