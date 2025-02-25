def cbt_exam():
    questions = {
        "1. Is dog a mammal?": "A",
        "2. What is the opposite of come?": "A",
        "3. What is the past tense of eat?": "A",
        "4. How many vowels are there in the word Earth?": "A",
        "5. Color yellow is an example of primary colors, yes or no?": "A"
    }
    
    options = [
        ["A) Yes", "B) No", "C) I don't know", "D) None"],
        ["A) Go", "B) Gone", "C) I don't know", "D) None"],
        ["A) Ate", "B) Eaten", "C) I don't know", "D) None"],
        ["A) 2", "B) 6", "C) I don't know", "D) None"],
        ["A) Yes", "B) No", "C) I don't know", "D) None"]
    ]

    score = 0

    for i, (question, correct_answer) in enumerate(questions.items()):
        print(question)
        for option in options[i]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == correct_answer:
            score += 1
    print(f"You scored {score}/{len(questions)}.")

cbt_exam()