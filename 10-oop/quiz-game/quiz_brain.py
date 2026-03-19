class QuizBrain:

    def __init__(self, q_list):
        self.number = 0
        self.list = q_list
        self.score = 0

    def next_question(self):
        r = input(f"Q.{self.number + 1}: {self.list[self.number].text} (True/False): ").capitalize()
        self.check_answer(self.list[self.number].answer, r)
        print(f"Your current score is: {self.score}/{self.number + 1}")
        self.number += 1

    def still_has_questions(self):
        return self.number < len(self.list)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}")
