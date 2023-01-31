import os
import openai

def openai_bot():
    while (1):
        inputMsg = input("Human: ")
        response = call_to_open_ai(inputMsg)
        print_openai_response(response)

def call_to_open_ai(request):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=request,
        temperature=0.8,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        stop= "Stop"
    )

def print_openai_response(response):
    for choice in response.choices:    
        print("AI: " + choice.text)
        print()

openai_bot()