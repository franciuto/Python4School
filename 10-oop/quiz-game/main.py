from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(i["text"], i["answer"]) for i in question_data]
quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_questions():
    quizBrain.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quizBrain.score}/{len(question_bank)}")
