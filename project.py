import random
def main():
    print("Welcome to the Hogwarts House Sorting Quiz!")
    print("Answer the following 5 questions to find out which house you belong to.\n")

    questions = [
        "Question 1: What quality do you value the most?\n"
        "a) Courage\n"
        "b) Loyalty\n"
        "c) Wisdom\n"
        "d) Ambition\n",
        
        "Question 2: If you could choose a magical power, what would it be?\n"
        "a) Super strength\n"
        "b) Invisibility\n"
        "c) Mind reading\n"
        "d) Shape-shifting\n",
        
        "Question 3: What animal do you feel a connection with?\n"
        "a) Lion\n"
        "b) Badger\n"
        "c) Eagle\n"
        "d) Snake\n",
        
        "Question 4: What's your approach to making decisions?\n"
        "a) Follow your instincts\n"
        "b) Consider all options\n"
        "c) Think analytically\n"
        "d) Be strategic\n",
        
        "Question 5: What type of people do you want to be friends with?\n"
        "a) Adventurous and daring\n"
        "b) Kind and loyal\n"
        "c) Intelligent and creative\n"
        "d) Ambitious and resourceful\n",
    ]

    house_scores = {
        "Gryffindor": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
        "Slytherin": 0
    }

    for i, question in enumerate(questions, start=1):
        print(question)
        answer = input("Your choice (a/b/c/d): ").lower()
        
        if answer == 'a':
            house_scores["Gryffindor"] += 1
        elif answer == 'b':
            house_scores["Hufflepuff"] += 1
        elif answer == 'c':
            house_scores["Ravenclaw"] += 1
        elif answer == 'd':
            house_scores["Slytherin"] += 1
        else:
            print("Invalid choice. Skipping this question.")

    max_score = max(house_scores.values())
    max_houses = [house for house, score in house_scores.items() if score == max_score]
    
    if len(max_houses) > 1:
        result = random.choice(max_houses)
    else:
        result = max_houses[0]
    
    print("\nSorting complete! Based on your answers, you belong to:")
    print(result)

if __name__ == "__main__":
    main()