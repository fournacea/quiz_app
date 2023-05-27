from question_model import Question
from data import question_data


question_bank = []

for question in question_data:
    trivia_question = question["text"]
    trivia_answer = question["answer"]
    new_question = Question(trivia_question, trivia_answer)
    question_bank.append(new_question)


# new_q = Question("Plants 'exhale' oxygen", "True")

# print(new_q)
# print(new_q.text)
# print(new_q.answer)
# print(len(question_bank))
# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)
# print(question_bank.answer["0"])

for question in question_bank:
    print(question.text)

for question in question_bank:
    print(question.answer)
