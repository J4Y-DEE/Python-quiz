quiz = [
    ("What percentage of people are left handed?", ["10 percent", "10", "10%"]),
    ("How many paintings did vincent van Gogh sell in his lifetime?", "1"),
    ("What human organ can fully regenerate itself?", "Liver"),
    ("What is the largest organ in the human body?", "Skin"),
    ("What is the largest bone in the human body?", "Femur")
]
def run_quiz(Questions):

    score = 0
    for question, answer in Questions:
        user_answer = input(question)

        # Convert both user_answer to lowercase and remove leading/trailing spaces for comparison
        user_answer_processed = user_answer.strip().lower()

        is_correct = False
        if isinstance(answer, list):
            for possible_answer in answer:
                if user_answer_processed == possible_answer.strip().lower():
                    is_correct = True
                    break
        else:
            if user_answer_processed == answer.strip().lower():
                is_correct = True

        if is_correct:
            print("Correct!")
            score += 1
        else:
            # Display correct answer(s) appropriately
            if isinstance(answer, list):
                print("Incorrect. The correct answers are:", ", ".join(answer))
            else:
                print("Incorrect. The correct answer is:", answer)

    print("Quiz complete! You scored", score, "out of", len(Questions))

run_quiz(quiz)

