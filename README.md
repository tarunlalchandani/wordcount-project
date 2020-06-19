# wordcount-project
counts words in reverse Order
1. Whatever you type after the website url like localhost:8000/admin so it will check in
the project url patterns whether anything is matching with it.
for example if i put
urlpatterns[
  path('iloveGovinda/',admin.site.urls),
]
so now localhost:8000/iloveGovinda will go to admin and not the admin one

2. to make a new path 
 - you have to make views.py and import it in the url patterns and then define a function corresponding to the template page in views.py
 - then you just write from . import views
 - path('url/(This / is imp)',views.<function>,name = 'home')
 
3. def home(request): Here the request is contaning information what url they are searching
and cookies and what web browser they are using.
In the function we decide what we are going to send back to the user
So we have to enclose it by importing the following line for HTTP Response
from django.http import HttpResponse

def home(request):
  return HttpResponse(<stringName>)
  or 
  return HttpResponse(some html code)

4.The first thing to return a html template is to tell django where to look onto the templates
5. the Templates dirs in the settings contain a list of folders where it should be looking
6. For rendering templates as we would not like to paste all the code in the HttpResponse we can
use from django.shortcuts import render
render(request,<Name of the HTML file in the template dirs>)
7. We can also pass other imformations to the html templates like
render(request,'home.html',{'hithere':'This is tarun'}

8. In form we can put a text area by using 
<textarea cols="40" rows="10" name="fulltext"></textarea>
<input type="submit" value="Count!"/>
You can customize the page by using {{hithere}} in the home.html

9. We also have to tell the form where you should go action="Count" so it will go to the count
thats what is use of the name you specify in the url patterns
10. But the prime way to do it is action="{% url '<NameInUrlPatterns>' %}"
In this method even if we change the url in the url patterns like we change refrencing countthewords
still it will work
11. When we submit after entering text to the textbox with a name then we can see that the 
new url goes with a query ?fullname = <what you entered>

12. So as it is going in the count.html so we can get what the person entered by 
fulltext = request.GET['fulltext']

13. fulltext.split() this will break according to the spaces
14. We can not send a dictionary inside the dictionary we are sending but we have to send then 
as a list which can be made as <dictionaryName>.items() and then for accessing we have to use a for 
loop then only we can access otherwise a error will come

15. We can put a loop in the html file(although possible directly) as
{% for word, count in worddictionary %}

{{ word }}
{%endfor%}

16. to sort a dictionary
import operator
sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=true)                                          )
Go and look at count 
and for the order
