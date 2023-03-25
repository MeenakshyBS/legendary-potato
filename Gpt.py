import openai
import random

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Generate a random fun fact using the OpenAI API
fact = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Generate a random fun fact",
    max_tokens=100
)["choices"][0]["text"].strip()

# Generate a random answer for the trivia question
answer = random.choice(["True", "False"])

# Print the fun fact and ask the user to guess if it's true or false
print(f"Here's a fun fact for you: {fact}")
print("Is this fact true or false?")

# Collect and check the answer from the user
crowd_answer = input("Your answer (True/False): ")
if crowd_answer == answer:
    print("Correct!")
else:
    print(f"Incorrect. The answer is {answer}.")
