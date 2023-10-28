import openai
from django.shortcuts import render
from django.http import JsonResponse

openai_api_key = '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'
openai.api_key = openai_api_key


def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')


def ask_openai(message):
    conversation = [
        {"role": "system", "content": "You are a intelligent."},
        {"role": "user", "content": message}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer
