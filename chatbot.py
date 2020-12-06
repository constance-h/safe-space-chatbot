"""Initilizes a chatbot and trains with basic conversation and mental support dialogue"""

import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot(
    "Spacey",
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters= [
        'chatterbot.logic.BestMatch',
        {
            'import_path' : 'chatterbot.logic.BestMatch',
            'default_response' : 'Sorry, I did not understand that. Please explain?',
            'maximum_similarity_threshold' : 0.9
        }
    ],
    database_uri = 'sqlite:///database.sqlite3'
    )

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations", 
    "corpus"
)

