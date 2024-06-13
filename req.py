import requests
async def send_answer(request):
    url = "https://chatgpt-api8.p.rapidapi.com/"

    payload = {
        "0": {
            "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
            "role": "system"
        },
        "1": {
            "content": request,
            "role": "user"
        }
    }
    headers = {
        "x-rapidapi-key": "a0ba13b4e0mshba551bc54539438p1345d6jsn258e72e50539",
        "x-rapidapi-host": "chatgpt-api8.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    return data['text']