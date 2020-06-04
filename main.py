import random
import json
import os
import playsound
from gtts import gTTS

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


def greeting_speech(user_statement, answer, num):
    if answer not in user_statement:
        return None
    else:
        return random.choice(data['greeting_answer'])

def tools():
    command, name, value = user_statement.split()
    if command == "add":
        data[name].append(value)
        print("added",value,"to", name)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)
    # This should add a specific item to an array
    elif command == "remove":
        data[name].remove(value)
        print("removed",value,"from", name)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)
    # This should remove a specific item from an array
    elif command == "show":
        print(data[name])
    #This should show a specific array
    elif command == "help":
        print(data['commands'])
    # This will display a list of commands that can be recieved
    # elif command == "end":
    #     break
    else:
        return None
    # This should end the cnversation and stop the program.


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    num = random.randint(1,2)

    user_statement = input("")

    for i in data['keywords']:
        response = create_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)
            speak(response)

    for i in data['greeting_answer']:
        response = greeting_speech(user_statement=user_statement, answer=i, num=num) 
        if response is not None:
            print(response)
            speak(response)
    # Handles the user saying hello

    if ("food" or "Food" or "eat" or "Eat") in user_statement:
        print(random.choice(data['food_answer']))
        speak(random.choice(data['food_answer']))
        # This if statement handles all questions with the word "food" in them
        

    for i in data['commands']:
        # Not sure why this doesn't work 
        tools()