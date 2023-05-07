# chat
Python script to access openai GPT via cli. Includes conversation history in prompts.

This is a simple Python script that implements the basic necessities for GPT prompts.
I've included many comments to help new users understand how the parameters work.
This code is also easy to expand upon if desired, and I may choose to do so in the future.

All one needs to do to get up and running with GPT is to obtain an API key from OpenAI
and include it in one of the two provided methods.

After each loop, past prompts and GPT responses are added to the next prompt which enables
GPT to keep "memory" (not really, but for basic purposes) of the conversation. Note that
this also uses tokens, so you may need to increase the token limit for longer conversations.
History also resets upon exiting the program, so you may wish to add functionality to log
your conversations to a file.
