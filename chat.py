import openai
import os

''' The safest way to store your API key is to set it as an environment variable
You can also store it as a string, but be careful not to commit it to GitHub!
To use it as a string, uncomment the line below'''

# openai.api_key = 'your-key-here'

'''To add your key as an environment variable on Windows, run the following in Command Prompt:
 setx OPENAI_API_KEY your-key-here
 make sure to use setx instead of set because setx makes the variable persistant
 whereas set is only for the current console instance'''

openai.api_key = os.environ.get('OPENAI_API_KEY')
messages = [ {"role": "system", "content": "Developing a web application"} ]
# There's no ending condition for the while loop, so it'll run until you quit.

while True:
    # You don't really need to mess with message settings can read about it here:
    # https://beta.openai.com/docs/api-reference/chat
    # Because the prompt is APPENDED to messages, it will include a history of every message you've sent
    # until you exit the program.

    prompt = input("Enter prompt: ")
    if prompt:
        messages.append(
            {"role": "user", "content": prompt}
        )

    # Generate a response
    # I included the engine settings here so they are easier to tweak per-prompt
    # It is recommended to change either temperature or top_p, but not both
    # top_p is based on nucleus sampling and idk wtf that is :)
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 1024,
        # stop is not normally necessary unless you have a condition in which you want it to stop automatically
        # such as in the case of SQL queries or something
        # stop = None,
        temperature = 0.5,
        # top_p = 1,
    )
    # The response you get from the API contains a lot more information than just the content
    # so here it's just grabbing the content, but you can change the parameters to see it all
    # or uncomment the next line and comment out the following one.
    # response = completion
    response = completion.choices[0].message.content
    print(f"ChatGPT: {response}")
   
    '''By default, the API is not able to reference past prompts unlike the web playground
    there is a method to do this by storing the response in a variable and passing it back to the input.
    Keep in mind this uses tokens as well, so you may want to exit the program in between different topics'''

    messages.append({"role": "assistant", "content": response})

