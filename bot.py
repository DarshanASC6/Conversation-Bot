import random
import array as arr

silent_answer = ["*shrugs*", "*silence*", "*stoic face combined with silence*", "*annyoed silence*"]

question_answer = ["What can I have to eat?", "When can I get a new book?", "When are we going back to New York?"]

statement_answer = ["Nah", "No", "One second", "Yeah, let me just finish this first", "Please stop pestering me about this", "Did Mom put you up to this?"]

food_answer = ["I'm good with anything", "Can I have desert?", "What can I have to eat?"]

answer = ""

def create_speech():
    if ((answer in user_statement) and (num > 1)):
        print(statement_answer[random.randint(0,(len(statement_answer)-1))])
    elif ((answer in user_statement) and (num == 1)):
        print(silent_answer[random.randint(0,(len(silent_answer)-1))])
    elif ((answer in user_statement) and (num == 3)):
        print(question_answer[random.randint(0,(len(question_answer)-1))])
# This is the function that generates a random answer based on the above parameters

def add_list():
    question_answer.append("orange")
    print(question_answer[(len(question_answer))-1])
    print(question_answer)

def remove_list():
    question_answer.remove("orange")
    print(question_answer[(len(question_answer))-1])
    print(question_answer)

while True:
    num = random.randint(1,3)

    user_statement = input("")

    answer = "ACT"
    create_speech()
    # This handles all statemets with the word "ACT" in them
    # Note to self: Find a way to break the function after this  

    answer = "grade"
    create_speech()
    # This handles all statemets with the word "grade" in them    

    answer = "school"
    create_speech()
    # This handles all statemets with the word "school" in them    

    if ("food" in user_statement):
        print(food_answer[random.randint(0,(len(food_answer)-1))])
    # This if statement handles all questions with the word "food" in them

    if ("add" in user_statement):
        add_list()
    # This will write to the above answers

    if ("remove" in user_statement):
        remove_list()
    # This will remove one of the above answers