from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for dictionary in question_data:
    question = dictionary["question"]
    answer = dictionary["correct_answer"]
    question = Question(question, answer)
    question_bank.append(question)
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
   
print("You've completed the quiz. Thanks for playing!")
print(f"Your high score was {quiz.score}/{quiz.question_number}")