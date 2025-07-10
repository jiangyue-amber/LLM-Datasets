# Software Name: Music_Scale_Trainer
# Category: Music
# Description: MST (Music Scale Trainer) is a software application designed to help musicians and music enthusiasts practice and improve their knowledge of musical scales. It provides interactive exercises where users can identify and play different scales on their instrument of choice. The software offers a variety of difficulty levels, real-time feedback on accuracy, and educational resources with explanations and audio examples of each scale. Users can track their progress and aim to master all major and minor scales.

import random

class ScaleTrainer:
    def __init__(self):
        self.major_scales = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'F', 'Bb', 'Eb', 'Ab', 'Db']
        self.minor_scales = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'D', 'G', 'C', 'F', 'Bb']
        self.current_scale = None
        self.score = 0
        self.total_questions = 0

    def choose_scale(self, scale_type='major'):
        if scale_type == 'major':
            self.current_scale = random.choice(self.major_scales)
        elif scale_type == 'minor':
            self.current_scale = random.choice(self.minor_scales)
        else:
            raise ValueError("Invalid scale type. Choose 'major' or 'minor'.")

    def ask_question(self):
        scale_type = random.choice(['major', 'minor'])
        self.choose_scale(scale_type)
        print(f"Identify the {scale_type} scale: {self.current_scale}")
        self.total_questions += 1
        return self.current_scale, scale_type

    def check_answer(self, user_answer, correct_scale, scale_type):
        if user_answer.lower() == correct_scale.lower():
            print("Correct!")
            self.score += 1
            return True
        else:
            print(f"Incorrect. The correct answer was {correct_scale} {scale_type}.")
            return False

    def display_score(self):
        if self.total_questions > 0:
            accuracy = (self.score / self.total_questions) * 100
            print(f"Your score: {self.score}/{self.total_questions} ({accuracy:.2f}%)")
        else:
            print("No questions asked yet.")

    def run_exercise(self, num_questions=5):
        print("Welcome to the Music Scale Trainer!")
        for _ in range(num_questions):
            correct_scale, scale_type = self.ask_question()
            user_answer = input("Your answer: ")
            self.check_answer(user_answer, correct_scale, scale_type)
        self.display_score()
        print("Exercise complete.")

if __name__ == '__main__':
    trainer = ScaleTrainer()
    trainer.run_exercise()