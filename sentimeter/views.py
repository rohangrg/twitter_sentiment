from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
import final
import sentimeter


def index(request):
    user_input = userinput()
    return render(request, "index.html", {'input_hastag': user_input})

def analyse(request, choice):
    user_input = userinput(request.GET or None)
    if int(choice) == 4 or (request.GET and user_input.is_valid()) :
    	try:
        	input_hastag = user_input.cleaned_data['q']
        except:
        	input_hastag = ''

        #to be changed
        data = final.getSentimentGraph(choice, input_hastag)

        return render(request, "result.html", {'data': data})
    return render(request, "index.html", {'input_hastag': user_input})