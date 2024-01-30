!pip install transformers
import numpy as np
import time
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# rest of the code...

checkpoint = 'microsoft/DialoGPT-medium'
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

class ChatBot():
    # ... (Copy the entire ChatBot class definition here)

# Instantiate the ChatBot class
bot = ChatBot()

# Start chatting
while True:
    bot.user_input()
    if bot.end_chat:
        break
    bot.bot_response()
