import random
import re
from bot_responses import bot_responses  


def get_users_name():
    users_name = input("Bot: Please enter your name to proceed ahead: ") 
    return users_name

#Function defined to randomly generate a name for the chatbot as per the users name
def get_bots_name(users_name): 
    bots_name = ["Eli", "Debrah", "Aron", "Mike", "Linda"]
    random.shuffle(bots_name)  

    if len(users_name) < 5: 
        return bots_name[1]  
    else:
        return bots_name[3]

def exit_phrases():
    return ["bye", "quit", "see you later", "i have to go now", "see you again"]

def get_responses(user_input):
    user_input = user_input.lower()
    words = user_input.split()

    for response in bot_responses: 
        for word in words:         
            if word in response["user_input"]:     
                return response["bot_response"]    
    return "I don't have information for that. Please ask me about something else." 

#Main function defined which controls the workflow for the chatbot
def chatbot():
    users_name = get_users_name()
    bots_name = get_bots_name(users_name)
    print(f"{bots_name}: Hello {users_name}! Welcome to the University of Poppleton. I'm {bots_name}, I'm here to assist you.\nDo you have any questions or anything you're curious about?")

    #Loop which keeps the response flow going on
    while True:
        user_input = input(f"{users_name}: ").lower()

        #When the exit_phrases are found in the user input. It will immediately end the converstation along with a goodbye message
        if user_input in [exit_phrase.lower() for exit_phrase in exit_phrases()]:
            print(f"{bots_name}: It was wonderful having a conversation with you. Have a good day ahead!")
            break  # Exit the conversation
        
        else:
            # Determines the appropriate response as per user's input
            response = get_responses(user_input)
            print(f"{bots_name}: {response}")

chatbot()