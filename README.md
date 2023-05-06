# Mochi_Virtual_Assistant
 OpenAI's text-davinci-002 based voice assistant
This program demonstrates how to use OpenAI's text-davinci-002 model to generate responses based on user input, and how to use synthesized speech to read out the responses to the user. The program provides an interactive way for users to engage with a virtual assistant named Mochi.

There are two functions in this code, one for generating a response from OpenAI based on user input, and another for listening for user input and responding using synthesized speech. The program uses a microphone to listen for the phrase "hello mochi" and then generates a response to any subsequent user input using OpenAI's text-davinci-002 model. The program uses the 'say' command in the terminal to read out the responses.

The program first sets up the OpenAI API by providing the API key. The function generate_response takes in user input and uses OpenAI's Completion API to generate a response. The function uses the text-davinci-002 engine to generate the response, and sets various parameters such as the maximum number of tokens and the temperature of the response. The function returns the generated response.

The function listen_for_hello uses the speech_recognition library to listen for user input using a microphone. It first waits for the phrase "hello mochi" to be spoken. When the phrase is detected, it responds using synthesized speech and waits for subsequent user input. It uses a while loop to continue listening for user input until the user says "exit". For each user input, the function generates a response using the generate_response function and reads out the response using the 'say' command in the terminal.

The program handles cases where the user input cannot be recognized using the try-except block. The program also handles cases where the user input includes the phrase "exit", in which case it terminates the program.
