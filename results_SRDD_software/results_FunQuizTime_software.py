# Software Name: FunQuizTime
# Category: Family_Kids
# Description: FunQuizTime is a software application that offers a wide range of fun and educational quizzes for children. It includes various topics such as math, science, history, language arts, and general knowledge. The quizzes are designed to be interactive and engaging, with colorful visuals and animated characters. Children can select their preferred subject and difficulty level, and the app provides instant feedback on their answers. FunQuizTime aims to make learning enjoyable and challenging while helping children improve their knowledge and critical thinking skills.

```python
import random

class Quiz:
    def __init__(self, subject, difficulty):
        self.subject = subject
        self.difficulty = difficulty
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        # This is a placeholder for loading questions from a file or database.
        # In a real application, you would load questions based on subject and difficulty.
        if self.subject == "math":
            if self.difficulty == "easy":
                return [
                    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
                    {"question": "What is 5 - 3?", "options": ["1", "2", "3", "4"], "answer": "2"},
                    {"question": "What is 1 + 1?", "options": ["1", "2", "3", "4"], "answer": "2"}
                ]
            elif self.difficulty == "hard":
                return [
                    {"question": "What is 12 x 12?", "options": ["140", "144", "150", "154"], "answer": "144"},
                    {"question": "What is 144 / 12?", "options": ["10", "11", "12", "13"], "answer": "12"},
                    {"question": "What is the square root of 81?", "options": ["7", "8", "9", "10"], "answer": "9"}
                ]
            else:
                return []

        elif self.subject == "science":
             if self.difficulty == "easy":
                return [
                    {"question": "What color is the sky?", "options": ["Red", "Blue", "Green", "Yellow"], "answer": "Blue"},
                    {"question": "What do bees make?", "options": ["Wax", "Honey", "Syrup", "Jam"], "answer": "Honey"},
                    {"question": "What is water made of?", "options": ["H2O", "CO2", "O2", "N2"], "answer": "H2O"}
                ]

             elif self.difficulty == "hard":
                return [
                    {"question": "What is the chemical symbol for iron?", "options": ["Ir", "Fe", "Au", "Ag"], "answer": "Fe"},
                    {"question": "What is the largest planet in our solar system?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Jupiter"},
                    {"question": "What is the process of plants making their own food called?", "options": ["Respiration", "Photosynthesis", "Digestion", "Transpiration"], "answer": "Photosynthesis"}
                ]
             else:
                return []

        else:
            return []

    def present_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"]):
            print(f"{i+1}. {option}")

        while True:
            try:
                user_answer = int(input("Enter your answer (1-" + str(len(question_data["options"])) + "): "))
                if 1 <= user_answer <= len(question_data["options"]):
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and " + str(len(question_data["options"])))
            except ValueError:
                print("Invalid input. Please enter a number.")

        if question_data["options"][user_answer - 1] == question_data["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer was:", question_data["answer"])

    def run_quiz(self):
        if not self.questions:
            print("No questions available for this subject and difficulty.")
            return

        random.shuffle(self.questions)

        for question_data in self.questions:
            self.present_question(question_data)

        print(f"Quiz complete! Your score: {self.score}/{len(self.questions)}")


def main():
    print("Welcome to FunQuizTime!")

    while True:
        print("\nChoose a subject:")
        print("1. Math")
        print("2. Science")
        print("3. Exit")

        try:
            subject_choice = int(input("Enter your choice (1-3): "))
            if subject_choice == 3:
                break

            if subject_choice == 1:
                subject = "math"
            elif subject_choice == 2:
                subject = "science"
            else:
                print("Invalid choice. Please try again.")
                continue

            print("\nChoose a difficulty:")
            print("1. Easy")
            print("2. Hard")

            difficulty_choice = int(input("Enter your choice (1-2): "))

            if difficulty_choice == 1:
                difficulty = "easy"
            elif difficulty_choice == 2:
                difficulty = "hard"
            else:
                print("Invalid choice. Please try again.")
                continue
            quiz = Quiz(subject, difficulty)
            quiz.run_quiz()

        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Thanks for playing FunQuizTime!")


if __name__ == "__main__":
    main()
```