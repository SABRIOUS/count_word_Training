from django.shortcuts import render

from django.http import HttpResponse

def aboutFun(request):
    return render(request,'about.html')


def homepage(request):
    return render(request,'home.html')


def countfun(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcitionary = dict()
    for i in wordlist:
        if i not in wordcitionary:
            wordcitionary[i] = 1
        else:
            wordcitionary[i] += 1
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'wordcitionary':wordcitionary})
