from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
challenges_of_month = {'january' : "Run 5km every day",
                        'february' : 'Take cold shower every day',
                        'march' : 'Do not eat after 6pm', 
                        'april' : "Run 5km every day",
                        'may' : 'Take cold shower every day',
                        'june' : 'Do not eat after 6pm', 
                        'july' : "Run 5km every day",
                        'august' : 'Take cold shower every day',
                        'september' : 'Do not eat after 6pm', 
                        'october' : "Run 5km every day",
                        'november' : 'Take cold shower every day',
                        'december' : 'Do not eat after 6pm'
                        }
def index(request):
    return HttpResponse('works')


def int_month(request, month):
    month -=1
    months = list(challenges_of_month.keys())
    if month >= 0 and month <= len(months)-1:
        return HttpResponseRedirect(reverse("month_challenge", args=[months[month]]))
    else:
        return HttpResponseRedirect(reverse("month_challenge", args=[f'{month}_is_wrong_month']))


def month(request, month):
    months = list(challenges_of_month.keys())
    if month.lower() in months:
        challenge_text = month + challenges_of_month[month.lower()]
    else:
        challenge_text = 'Page not found'
    return HttpResponse(challenge_text)