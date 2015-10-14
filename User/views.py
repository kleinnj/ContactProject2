from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import generic
import unicodedata

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from .models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
       
        username = request.POST.get("username", "")
        username = unicodedata.normalize('NFKD', username).encode('ascii','ignore')
        try:
            u = User.objects.get(pk =)first(pk = username)
        except User.DoesNotExist:
           return HttpResponse("none")
        return HttpResponse("yes")
    
#         password = request.POST.get("password","")
# 
#        
#         test = is_user_password_right(username, password)
#         if test:
#             HttpResponse("We did it!")
#         else:
#             state = "Please try again"
#             return render(request, 'user/login.html' ,{'state':state, 'username': username})
            
#         try:
#             user = User.objects.get(pk=username)
#         except User.DoesNotExist:
#             state = "please try again"
#             return render(request, 'user/login.html' ,{'state':state, 'username': username})
#         if user.password == password:
#             return HttpResponse("it worked?")
#         else:
#             state = "Please try again"
#             return render(request, 'user/login.html' ,{'state':state, 'username': username})
#                                     
               
              
                
                
           

    return render_to_response('user/login.html',{'state':state, 'username': username})

def is_user_password_right(username, password):
    
    try:
        u = User.objects.get(pk=username)
        print "heeeeelp"
    except User.DoesNotExist:
        return False
    if u.password == password:
        return True
    else: 
        return False