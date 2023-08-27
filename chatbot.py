import openai

# Ustawienie klucza API OpenAI
openai.api_key = "TU_TWÓJ_KLUCZ_API"

# Funkcja do wysyłania zapytań do API OpenAI
def send_message(message):
    # Przygotowanie danych wejściowych w formacie GPT-3
    input_data = {
        "prompt": f"User: {message}\nChatBot:",
        "max_tokens": 50,
        "temperature": 0.6,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
    
    # Wywołanie API OpenAI
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_data["prompt"],
        max_tokens=input_data["max_tokens"],
        temperature=input_data["temperature"],
        top_p=input_data["top_p"],
        frequency_penalty=input_data["frequency_penalty"],
        presence_penalty=input_data["presence_penalty"]
    )
    
    # Odczytanie odpowiedzi od ChatBota
    chatbot_response = response.choices[0].text.strip().split("ChatBot:")[1]
    
    return chatbot_response

# Główna pętla programu
while True:
    user_input = input("User: ")
    chatbot_output = send_message(user_input)
    print("ChatBot:", chatbot_output)

    # Zakończenie programu, jeśli użytkownik wpisze "quit" lub "exit"
    if user_input.lower() in ["quit", "exit"]:
        break