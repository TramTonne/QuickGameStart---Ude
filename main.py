from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
#creating question bank including a bunch of Question() (aka Question object)
question_bank=[]
for item in question_data:
    question_text=item["text"]
    question_answer=item["answer"]
    new_q= Question(question_text,question_answer)
    question_bank.append(new_q)
#print the 1st question answer using list(question_bank), attribute(answer) and class(Question)
# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.questions_number}")