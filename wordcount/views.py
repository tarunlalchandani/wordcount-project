from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')# we cannot just return string but a http url
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split(' ')
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] = worddictionary[word]+1
        else:
            worddictionary[word] = 1
    Sortedwords = sorted(worddictionary.items(),key = operator.itemgetter(1),reverse=True)
    for (x,y) in Sortedwords:
        print("x: {} y: {}".format(x,y))
    return render(request,'count.html',{'count':len(wordlist),'fulltext':fulltext,'Sortedwords':Sortedwords})
def about(request):
    return render(request,'about.html')
