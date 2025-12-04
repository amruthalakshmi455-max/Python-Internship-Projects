
faq_responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help?",
    "price": "Our pricing information is available on the website.",
    "pricing": "Our pricing information is available on the website.",
    "refund": "Refunds take 5-7 business days to process.",
    "order status": "Please provide your order ID to check the status.",
    "support": "Sure! Tell me what issue you're facing.",
    "payment": "We accept UPI, cards and net banking.",
    "bye": "Goodbye! Have a nice day!",
}

def find_best_match(user_input):
    text = user_input.lower()

    for key in faq_responses:
        if key in text:
            return faq_responses[key]

    words = text.split()
    for word in words:
        if word in faq_responses:
            return faq_responses[word]

    return None


import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        return requests.get(url).text
    except:
        return "Could not get weather info."


def chatbot_reply(user_input):

    reply = find_best_match(user_input)
    if reply:
        return reply

    if "weather" in user_input.lower():
        city = user_input.split()[-1]
        return get_weather(city)
    return "I'm not sure about that, but I can connect you to support!"

print("🤖 AI Chatbot Ready! (Type 'bye' to exit)\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot:", faq_responses["bye"])
        break

    print("Bot:", chatbot_reply(user))
