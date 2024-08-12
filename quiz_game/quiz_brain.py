class QuizBrain:
    def __init__(self, qbank):
        self.question_number = 0
        self.question_list = qbank
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        while answer.lower() != "true" and answer.lower() != "false":
            answer = input("Please enter 'True' or 'False' :  ")
        self.question_number += 1
        self.check_answer(answer, self.question_list[self.question_number].answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nYou got it right!")
            self.score += 1
        else:
            print("\nThat's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n\n")

