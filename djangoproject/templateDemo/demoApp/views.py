from django.shortcuts import render
import datetime

# Create your views here.

def display(request):
    message = 'Hi, '
    date = datetime.datetime.now()
    hour= int(date.strftime('%H')) 
    if hour<12:
        message += 'Good Morning!!!'
    else:
        message += 'Good Evening!!!'
    name='Nandhini'
    date_dict = {'display_date':date,'empname':name, 'greetings':message}
    return render(request, 'demoApp/first.html', context=date_dict)

