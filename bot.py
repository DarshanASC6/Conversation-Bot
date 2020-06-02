import random
import json

with open("data.json") as f:
    data = json.load(f)
# Pulls data from a .JSON file

def create_speech(user_statement, answer, num):

    if answer not in user_statement:
        return None

    if num == 1:
        return random.choice(data['silent_answer'])
    else:
        return random.choice(data['statement_answer'])

def add():
    x = user_statement.split(" ")

    answer = x[1]
    
    array_name = x[2]
    
    array_name.append(answer)
    # Error in the code
    
    print("added",answer,"to", array_name)

while True:

    num = random.randint(1,2)

    user_statement = input("")

    for i in data['keywords']:
        response = create_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)

    if ("food" or "Food") in user_statement:
        print(random.choice(data['food_answer']))
    # This if statement handles all questions with the word "food" in them

    if ("add") in user_statement:
        add()
    # This will write to the above answers

    if ("remove") in user_statement:
        question_answer.pop()
    # This will remove one of the above answers

    if ("show") in user_statement:
        print(data['keywords'])

    if ("help") in user_statement:
        print("poo")
    # This will display a list of commands that can be given