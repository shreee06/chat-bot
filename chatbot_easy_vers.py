# -*- coding: utf-8 -*-
"""chatbot easy --vers

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JnyXFrQXYwJv9qEi3HTqn507ekDkfMuH
"""

!pip install chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('My Chatbot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train("chatterbot.corpus.english")

# Start a conversation with the chatbot
while True:
    user_input = input("You: ")

    # Get a response from the chatbot
    bot_response = chatbot.get_response(user_input)

    print("ChatBot:", bot_response)