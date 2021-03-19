# I have Created This File  - Stark

#
from django.http import HttpResponse
# for using templates in django we use this in our projects
from django.shortcuts import render


def index(request):
    # st  = {'name':'Tushar','occu':'Stark'}
    return render(request, 'index.html')


def Analyze(request):

    # it returns the text which user enter in a field box and throws to console if not give the text then it print default
    # djtext = request.GET.get('text', 'default')
    djtext = request.POST.get('text', 'default')
    # Check which checkbox is on
    removepunc = request.POST.get('removepunc', 'OFF')
    # removepunc = request.GET.get('removepunc', 'OFF')
    fullcaps = request.POST.get('fullcaps', 'OFF')
    # fullcaps = request.GET.get('fullcaps', 'OFF')
    NewLineRemover = request.POST.get('NewLineRemover', 'OFF')
    # NewLineRemover = request.GET.get('NewLineRemover', 'OFF')
    Space = request.POST.get('Space', 'OFF')
    # Space = request.GET.get('Space', 'OFF')
    Counter = request.POST.get('Counter', 'OFF')
    # Counter = request.GET.get('Counter', 'OFF')
# we use POST instead of GET because we want our url clean and safe from malicious users so use POST because there may be danger of csrf issues so that we use this 
    if(removepunc == "on" and fullcaps == 'on' and NewLineRemover == "on"):
        lists = '''(/[-[\]()*+{:?}.,\^$|#\]/,"\><$&");'''
        ana = ""
        for char in djtext:
            if char not in lists:
                if char != "\n" and char!='\r':

                
                    ana = ana+char.upper()
        params = {'purpose': "Removed Punctuations", 'analyzed_text': ana}
        djtext = ana
        # return render(request, 'analyze.html', params)

    if (removepunc == "on"):

        lists = '''(/[-[\]()*+{:?}.,\^$|#\]/,"\><$&");'''
        ana = ""
        for char in djtext:
            if char not in lists:
                ana = ana+char
        # analyzed = ana
        params = {'purpose': "Removed Punctuations", 'analyzed_text': ana}
    # Analyze The text
        djtext = ana
        # return render(request, 'analyze.html', params)

    if(fullcaps == 'on'):
        ana = ""
        for char in djtext:
            ana = ana+char.upper()
        params = {'purpose': "Uppercase Letters are", 'analyzed_text': ana}
        djtext = ana
        # return render(request, 'analyze.html', params)

    if(NewLineRemover == "on"):

        ana = ""
        for char in djtext:
            if char != "\n"and char!='\r': # \r is a carriage return which return unknown values
                ana = ana+char

        params = {'purpose': "NewLineRemover Charactors", 'analyzed_text': ana}
        djtext = ana

        # return render(request, 'analyze.html', params)

    if(Space == "on"):
        ana = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):

                ana = ana + char
        params = {'purpose': "SpaceRemover", 'analyzed_text': ana}
        djtext = ana

        # return render(request, 'analyze.html', params)
    if(Counter == "on"):
        count = 0
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                count = count+1
        params = {'purpose': "Counter", 'analyzed_text': count}
        # djtext = ana

    if(Counter!='on'and Space!='on'and NewLineRemover!='on'and fullcaps!='on'and removepunc!='on'):
        return HttpResponse("Please Select The Options")

    return render(request, 'analyze.html', params)