import json
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

class Quiz:
    def __init__(self, question_file="questions.json"):
        self.questions = []
        self.load_questions(question_file)
        self.score = 0
        self.question_file = question_file

    def load_questions(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for entry in data:
                    question = Question(entry['prompt'], entry['options'], entry['answer'])
                    self.questions.append(question)
            print(f"{len(self.questions)} questions loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty question set.")
        except json.JSONDecodeError:
            print("Error loading questions: Invalid file format.")

    def save_questions(self):
        data = []
        for question in self.questions:
            data.append({
                'prompt': question.prompt,
                'options': question.options,
                'answer': question.answer
            })
        with open(self.question_file, 'w') as file:
            json.dump(data, file, indent=4)
        print("Questions saved successfully.")

    def add_question(self, prompt, options, answer):
        if answer not in options:
            print("Error: Answer must be one of the options.")
            return
        new_question = Question(prompt, options, answer)
        self.questions.append(new_question)
        print("New question added successfully.")
        self.save_questions()

    def start_quiz(self):
        print("Starting the quiz!\n")
        for question in self.questions:
            print(question.prompt)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}. {option}")
            try:
                user_answer = int(input("Enter the option number of your answer: ").strip())
                if user_answer < 1 or user_answer > len(question.options):
                    print("Invalid option. Skipping question.\n")
                    continue
                if question.check_answer(question.options[user_answer - 1]):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect! The correct answer was: {question.answer}\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")

        print(f"Quiz completed! Your final score is: {self.score} out of {len(self.questions)}")

    def reset_score(self):
        self.score = 0

quiz = Quiz()

while True:
    add_question = input("Would you like to add a new question? (yes/no): ").strip().lower()
    if add_question == 'yes':
        prompt = input("Enter the question prompt: ").strip()
        options = []
        for i in range(4):
            option = input(f"Enter option {i + 1}: ").strip()
            options.append(option)
        answer = input("Enter the correct answer: ").strip()
        quiz.add_question(prompt, options, answer)
    else:
        break

quiz.start_quiz()
