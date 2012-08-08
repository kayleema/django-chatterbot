# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Bot
from django.template import RequestContext

def ask(request):
    bot = Bot.objects.get(id=request.GET['b'])
    response = bot.ask(request.GET['q'])
    return HttpResponse(response)

def home(request):
    return render_to_response('chat/home.html',
                              context_instance=RequestContext(request))

def feed(request):
    bot = Bot.objects.get(id=request.POST['b'])
    file = request.FILES['f']
    if not ".txt" in file.name:
    	return HttpResponse("failure:  must upload a .txt file!")
    if file.size > 100000:
    	return HttpResponse("failure:  max filesize is 100K!")
    bot.ask(file.read())
    return HttpResponse("success :)")

def newbot(request):
    bot = Bot(name=request.GET['n'])
    bot.save()
    return HttpResponse("successfully created bot named '{1}' with id: {0}".format(bot.id, bot.name))

def interact(request):
    bot = Bot.objects.get(id=request.GET['b'])
    return render_to_response('chat/interact.html',{'bot' : bot},
                              context_instance=RequestContext(request))
