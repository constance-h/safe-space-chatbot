"""Initilizes a chatbot and trains with basic conversation and mental support dialogue"""

import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot("Chatbot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations", 
    "corpus"
)

# directory = "corpus"

# for file in os.listdir(directory):
#     trainer.train("corpus."+file)

"""
class ChatBot():
    def init
        training functions here
        
"""