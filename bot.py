import random
import json

with open('data.json') as f:
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
    # This function doesn't work now because of the .JSON file lol
    
    # x = user_statement.split(" ")

    # answer = x[1]
    
    # array_name = x[2]

    # for i in data[array_name]
    #     del i [answer]
    # # Error in the code

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

    # print("added",answer,"to", array_name)

def remove():
    # This function also doesn't work now lol

    # x = user_statement.split(" ")

    # answer = x[1]
    
    # array_name = x[2]

    # for i in data[array_name]
    #     del i [answer]
    # # Error in the code

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
        
        # print("removed",answer,"from", array_name)

while True:

    num = random.randint(1,2)

    user_statement = input("")

    for i in data['keywords']:
        response = create_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)

    for i in data['commands']:
        # make a function here using all of the if statements below 
        

        # if ("food" or "Food") in user_statement:
        #     print(random.choice(data['food_answer']))
        # # This if statement handles all questions with the word "food" in them

        # if ("add") in user_statement:
        #     add()

        # if ("remove") in user_statement:
        #     remove()

        # if ("show") in user_statement:
        #     print(data['keywords'])

        # if ("help") in user_statement:
        #     print("poo")
        # # This will display a list of commands that can be given