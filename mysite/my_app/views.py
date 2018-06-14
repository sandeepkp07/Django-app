from django.shortcuts import render
from django.shortcuts import render
from .forms import AddForm,reader
from .models import Adding,Reader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
#from django.conf.urls import reverse
from django.core.urlresolvers import reverse_lazy
from django.views import generic

import requests,json
from .forms import TweetForm
import json
from .forms import TweetForm,Converter,Chatroom

from requests_oauthlib import OAuth1Session

import requests
import ast

import feedparser


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




def add(request):
    if(request.method=='POST'):
    	title = "Welcome"
    	form=AddForm(request.POST)
    	#context={"title":title,"form":form}
    	if form.is_valid():
        	form.cleaned_data["userid"] = request.user.id
        	instance = form.save(commit = False)
        	instance.userid=request.user.id
        	instance.save()
        	message = "Database successfully updated!!!"
    else:
	form = AddForm()
        message = "Welcome"

    return render(request, 'my_app/Adding.html', {"form":form,"message":message})



def show(request):
	# lead = [(i.name,i.marks,i.userid) for i in Leaderboard.objects.all()]
	le=Adding.objects.all().order_by("-Marks")
	#if request.user.is_authenticated():
        print(request)
        context={"leaderboard":le,}

        return render(request,"my_app/leaderboard.html",context)








def delete(request,pk):

    print(request,"\n",pk,"\n",request.user.id)
    le1=Adding.objects.get(id=pk)
    #print(le1)
    le=le1.userid
    print(le)
    print(request.user.id)
    if int(request.user.id) == int(le):
        print("yess")
        message="Deleted"
        print(Adding.objects.filter(id=pk))
        Adding.objects.filter(id=pk).delete()
    else:
        message = "Unsuccessfull cannot delete other's data"
    le2=Adding.objects.all()
    context={"leaderboard":le2,"title":message}

    return render(request,"my_app/leaderboard.html",context)

API_KEY = "9MrHmZOusg7wAw5JwGAg8Jy3C"
API_SECRET = "lBV7mhD6dyh5pw2NNpKh1adufBzZav8fbu04D1qMfelXTFjZxa"
AUTH = OAuth1Session(API_KEY,API_SECRET)

def tweets(request):
	if request.method=='POST':
		form=TweetForm(request.POST)
		username = request.POST.get('fullname')
		tweetcount = (request.POST.get('tweetcount'))
		user_timeline= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count="+tweetcount+"&tweet_mode=extended"
		Value = AUTH.get(user_timeline)
		tweets = json.loads(Value.text)
		TOP =   "Tweets:"
		DATA = []
		for i in tweets:
			DATA.append(i["created_at"]+"\n"+i["full_text"])

	else:
		TOP = ""
		DATA=""
		form=TweetForm()
        context = {"form":form,"Tweet" : DATA,"TOP":TOP}
        return render(request,'my_app/tweets.html',context)


def converter(request):
	if request.method=='POST':
		form=Converter(request.POST)
		cfrm = request.POST.get('convert_from')
		cto = request.POST.get('convert_to')
		amt = (request.POST.get('amount'))
		print(cfrm,cto,amt)
		value=[]
		DATA=0
		t = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=%s_%s&compact=y" % (cfrm,cto))
		text = ast.literal_eval(t.text)
		f=text.values()
		value =  f[0].values()
		DATA = "THE AMOUNT IS="+str(float(amt) * value[0])


		#response=requests.get("https://api.fixer.io/latest?base="+cfrm)
		#text=ast.literal_eval(response.text)
		#rates=text['rates']
		#print(rates.keys())
		#print((rates[cto]))
		#amount =(rates[cto])*(float(amt))
		#DATA="THE AMOUNT IS="+str(amount)

	else:
		DATA="Please Select The exchange rates"
		form = Converter()
        return render(request,'my_app/converter.html',{"print":DATA,"form":form})


def rssreader(request):
	if request.method=='POST':
		form = reader(request.POST)
		urls = request.POST.get('url')
		link = feedparser.parse(urls)
		MainHead = link['feed']['title']
		DATA=[]
		Topic = []
                H = []
		for post in link.entries:
			Topic.append(post.title+"-------"+"\n"+post.published+":"+post.summary+"----------"+"#Link:"+post.link)
			
				
	else:
		Topic = ""
		MainHead = ""
		form = reader()

        return render(request,'my_app/rss.html',{"Head":MainHead,"print":Topic,"form":form})



def chatroom(request):
	if request.method=='POST':
		form = Chatroom(request.POST)
		msg=request.POST.get("message")
		url = ("https://matrix.org/_matrix/client/r0/rooms/!VloBXYacCYTNcJpCdx:matrix.org/send/m.room.message?access_token=MDAxOGxvY2F0aW9uIG1hdHJpeC5vcmcKMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDI4Y2lkIHVzZXJfaWQgPSBAc2FuZGVlcGtwOm1hdHJpeC5vcmcKMDAxNmNpZCB0eXBlID0gYWNjZXNzCjAwMjFjaWQgbm9uY2UgPSBCMHI0MWVlT184LUdYOGZPCjAwMmZzaWduYXR1cmUgVpHVfB5VV3Knyr3UwMgxzIZmQG4m_LeYSIfTt1RWEqAK")
		dat = {"msgtype":"m.text", "body":msg}
		forward = requests.post(url,data = json.dumps(dat))
		d = ast.literal_eval(forward.text)
		list = d.keys()
		if list[0] == 'event_id':
    			Data = "SUCCESS!!!"
		else:
    			Data = "Some error occured"

	else:
		form = Chatroom()
		Data = ""
		
	return render(request,'my_app/chat.html',{"print":Data,"form":form})


	




# Create your views here.
