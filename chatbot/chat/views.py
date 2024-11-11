from django.shortcuts import render
from .models import Chat
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from datetime import datetime

# Create your views here.



responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "what is your name?": "I'm a simple chatbot created to assist you!",
    "what can you do?": "I can answer simple questions and chat with you. Try asking me something!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "help": "Sure! You can ask me about my capabilities or just chat with me.",
    "what time is it?": "I can't check the time, but you can look at your device's clock!",
    "what is the weather like?": "I don't have real-time data, but you can check a weather app for that.",
    "tell me something interesting": "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
    "i'm sad": "I'm sorry to hear that. Sometimes talking helps. Want to share what's on your mind?",
    "i'm happy": "That's great to hear! What made your day so good?",
    "what's your favorite color?": "I don't have preferences like humans do, but I think all colors are beautiful!",
    "can you speak other languages?": "I primarily understand English, but you can try asking me in another language!",
    "who created you?": "I was created by developers to assist users in chatting and answering questions.",
    "tell me about yourself": "I'm a simple chatbot here to help you with your questions and engage in conversation!",
    "how can I improve my day?": "Sometimes a small act of kindness can improve your day! How about helping someone out?",
}

def chatbot_view(request):
    user_message = ""
    bot_response = ""

    if request.method == "POST":
        user_message = request.POST.get("message").lower()
        tokens = word_tokenize(user_message)

        if user_message in responses:
            bot_response = responses[user_message]
        else:
            for token in tokens:
                if token in responses:
                    bot_response = responses[token]
                    break
            else:
                bot_response = "I'm sorry, I don't understand that."

        # Save chat to the database
        chat = Chat(user_message=user_message, bot_response=bot_response)
        chat.save()

    # Retrieve all chats from the database
    chats = Chat.objects.all().order_by('-timestamp')

    return render(request, 'index.html', {'chats': chats})
