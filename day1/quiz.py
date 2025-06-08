question_answer = [
    {'question': 'What is capital of Nepal?', 'answer': 'Kathmandu', 'points': 0},
    {'question': 'What is age of Manish?', 'answer': 23, 'points': 0}
]
user_points = 0

for each in question_answer:
    print(each['question'])
    answer = input()
    if type(each['answer']) == str:
        if each['answer'].lower() == answer.lower():
            each['points'] += 10
            user_points += 10
    elif type(each['answer']) in [int, float]:
        if str(each['answer']) == answer:
            each['points'] += 10
            user_points += 10

print(f"You have got points: {user_points}")