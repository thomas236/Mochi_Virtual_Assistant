# Import required libraries
import speech_recognition as sr
import openai
import os

# Set up the OpenAI API key
openai.api_key = "YOUR API KEY"

# Define a function to generate a response from OpenAI based on the user input
def generate_response(user_input):
    # Construct the prompt to be passed to OpenAI
    prompt = f"User: {user_input}\nMochi:"
    # Use OpenAI's Completion API to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7)
    # Return the generated response
    return response.choices[0].text.strip()

# Define a function to listen for user input and generate a response
def listen_for_hello():
    # Create an instance of the speech recognizer
    r = sr.Recognizer()
    # Use a microphone as the source for input
    with sr.Microphone() as source:
        # Print a message to the console
        print("Waiting for 'hello mochi'...")
        # Use a while loop to continuously listen for user input
        while True:
            # Listen for input from the microphone
            audio = r.listen(source)
            try:
                # Attempt to convert the user's voice input into text
                user_input = r.recognize_google(audio)
                # Print the recognized text to the console
                print (user_input)
                # Check if the user input contains the phrase "hello mochi"
                if "hello mochi" in user_input.lower():
                    # Print a message to the console
                    print("Say something...")
                    # Use the 'say' command to speak a greeting
                    os.system("say -v Samantha 'Hello, I am Mochi. How can I assist you?'")
                    # Use a while loop to continuously listen for user input
                    while True:
                        # Listen for input from the microphone
                        audio = r.listen(source)
                        # Attempt to convert the user's voice input into text
                        user_input = r.recognize_google(audio)
                        # Print the recognized text to the console
                        print (user_input)
                        # Check if the user input contains the phrase "exit"
                        if "exit" in user_input.lower():
                            # Print a message to the console
                            print("Goodbye!")
                            # Use the 'say' command to speak a goodbye message
                            os.system("say -v Samantha 'Goodbye!'")
                            # Exit the function
                            return
                        # Generate a response from OpenAI based on the user input
                        response = generate_response(user_input)
                        # Print the user input and generated response to the console
                        print(f"User: {user_input}")
                        print(f"Mochi: {response}")
                        # Use the 'say' command to speak the generated response
                        os.system(f"say -v Samantha '{response}'")
                else:
                    # Print a message to the console
                    print("Waiting for 'hello mochi'...")
            except sr.UnknownValueError:
                # Print a message to the console
                print("Sorry, I didn't understand. Please try again.")

# Call the listen_for_hello function to start the program
listen_for_hello()
