from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
                        'december' : None
                        }
def index(request):
    months = list(challenges_of_month.keys())
    return render(request, 'mchallenges/index.html', {
        'months' : months

    })


def int_month(request, month):
    month -=1
    months = list(challenges_of_month.keys())
    if month >= 0 and month <= len(months)-1:
        return HttpResponseRedirect(reverse("month_challenge", args=[months[month]]))
    else:
        return HttpResponseRedirect(reverse("month_challenge", args=[f'{month+1}_is_wrong_month']))


def month(request, month):
    months = list(challenges_of_month.keys())
    month = month.lower()
     
    if month in months:
        challenge_text = challenges_of_month[month]
        return render(request, 'mchallenges/challenge.html', {
            'challenge' : challenge_text,
            'month' : month

        })
    else:
        return HttpResponseNotFound()
    