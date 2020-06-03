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

# Does not work
def modify():
    command, name, value = user_statement.split()
    if command == "add":
        data[name].append(value)
        print("added",value,"to", name)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)
    elif command == "remove":
        data[name].pop(value)
        print("removed",value,"from", name)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)

def show():
    array_name = user_statement.split(" ")
    print(array_name[1])

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

    if ("food" or "Food" or "eat" or "Eat") in user_statement:
        print(random.choice(data['food_answer']))
        speak(random.choice(data['food_answer']))
        # This if statement handles all questions with the word "food" in them
        
        # Error here
        if "end" in user_statement:
            break
        # This should end the ocnversation and stop the program.

    for i in data['commands']:
        # make a function here using all of the if statements below 
        modify()

        if ("show") in user_statement:
            show()
            #This should show a specific array

        if ("help") in user_statement:
            print(data['commands'])
        # This will display a list of commands that can be recieved