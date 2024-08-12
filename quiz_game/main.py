from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for ques in question_data:
    q = Question(ques["text"], ques["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

score = 0
number_of_questions = len(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congrats on completing the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
