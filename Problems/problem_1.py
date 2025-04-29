# Code to Get a joke.
prompt: str= "What do you want:  "
Joke: str = """Sophia is heading out to grocery store. A programmer tell sophia. get a litter of milk if they have eggs, get 12. The sophia return the 13 litter of milk say that yes they have eggs"""
other_response: str= "Sorry! I only answers Joke."
#function
def Joke_bot():
    #User input.
    user_input: str = input(prompt)

    #Conditional statement.
    if user_input == "joke":
        print(Joke)
    else:
        print(other_response)
Joke_bot()