from nada_dsl import *
import random

def nada_main():
    party1 = Party(name="Party1")

    # Define an array of jokes
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why was the math book sad? Because it had too many problems!"
    ]

    # Choose a random joke from the array
    selected_joke = random.choice(jokes)

    # Return the selected joke as the output
    return [Output(selected_joke, "joke_output", party1)]
