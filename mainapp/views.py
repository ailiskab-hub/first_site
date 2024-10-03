import os
from django.shortcuts import render, redirect


curr_path = os.path.dirname(os.path.abspath(__file__))

posts = [
    {
        "Title": "Что то пока бесполезное, но то, что позволит мне стать лучше",
        "Description": "Если долго мучаться - что-нибудь получится. Пока получилось только это",
        "Author": "Элис",
        "Date": "03.10.2024",
        "Comments": "А тут должны быть комментарии"
    },
    {
        "Title": "А это уже еще что-то",
        "Description": "Это как бы второй пост в блоге ахахах",
        "Author": "Элис",
        "Date": "03.10.2024",
        "Comments": "Тут без комментариев"
    }
]


def indexpage(request):
    return(render(request, template_name='index.html', context={'articles': posts, 'page': 'index'}))

def aboutpage(request):
    return render(request, template_name='about.html', context={"page": 'about'})

def contactpage(request):
    if request.method == 'GET':
        return render(request, template_name='contact.html', context={"page":"contact"})
    else:
        print(request.POST)
        with open(os.path.join(curr_path, 'contact_results.txt'), 'a') as file:
            file.writelines(f'Name {request.POST["name"]}, Message {request.POST["message"]} \n')
        return redirect(thanks)

def thanks(request):
    return render(request, template_name='thanks.html', context={"page": 'thanks'})
