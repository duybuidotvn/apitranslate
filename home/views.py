from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests

# Create your views here.


def index(request):
    return render(request, "home/index.html", {"users": 1})


def search(request):
    fromLocation = request.POST['fromLocation']
    destLocation = request.POST['destLocation']
    startDate = request.POST['startDate']
    numberSeat = request.POST['numberSeat']
    param = {
        "fromLocation": fromLocation,
        "destLocation": destLocation,
        "startDate": startDate,
        "numberSeat": numberSeat
    }

    print(fromLocation)
    print(destLocation)
    print(startDate)
    print(numberSeat)
    return render(request, "home/tim-xe.html", param)


def detail(request, request_id):
    print(request_id)
    return render(request, "home/chi-tiet-xe.html", {"id": request_id})


def step1(request, request_id):
    print(request_id)
    return render(request, "home/dat-ve-buoc-1.html", {"id": request_id})

def step2(request, request_id):
    print(request_id)
    return render(request, "home/dat-ve-buoc-2.html", {"id": request_id})

def step3(request, request_id):
    print(request_id)
    return render(request, "home/dat-ve-buoc-3.html", {"id": request_id})


# def index(request):
#     users = User.objects.order_by('username')[:3]
#     output = '<br>'.join(['Hello %s <a href="phuong">%s</a>' %
#                           (u.username, u.address) for u in users])
#     return HttpResponse('Hello Lê Hồng Phương <a href="phuong">adf</a>')


# def phuong(request):
#     users = User.objects.all()
#     template = loader.get_template('home/index.html')
#     context = {
#         'users': users,
#     }

#     return HttpResponse(template.render(context, request))
#     # return HttpResponse('Phuong method <a href="/home/">adf</a>')


# def hien(request):
#     users = User.objects.all()
#     context = {
#         'users': users,
#     }
#     username = request.POST['username']
#     password = request.POST['password']
#     print(username)
#     # return render(request, 'home/index.html', context)
#     # return HttpResponse("username %s password %s" %(username,password))
#     # return HttpResponse("username %s password %s" %(username,password))
#     return HttpResponseRedirect(reverse("home:index"))


# def hack(request):
#     # URL = "https://www.vetaulyson.com/?component=tim-kiem&act=search&type=oneway&khoihanh=sa-ky&diemden=ly-son&date_kh=28-04-2019&soluong_start=2&date_ve=&soluong_return=0&btnBooking=T%C3%8CM+V%C3%89+NGAY"
#     # URL = "https://www.vetaulyson.com/"
#     # location given here
#     # location = "delhi technological university"

#     # defining a params dict for the parameters to be sent to the API
#     # PARAMS = {'address': location}

#     # sending get request and saving the response as response object
#     # for x in range(2):
#     # requests.post(url=URL, params={})
#     for x in range(5000):
#         requests.get('https://www.vetaulyson.com/')

#     # extracting data in json format
#     # data = r.json()

#     # print("phuong" + req.url)

#     return render(request, "home/hack.html", {})


# def detail(request, request_id):
#     return HttpResponse('detail %s' % request_id)


# def result(request, request_id):
#     response = "result %s"
#     return HttpResponse(response % request_id)


# def vote(request, request_id, request_id1):
#     return HttpResponse("vote %s + %s = %s" % (request_id, request_id1, (request_id+request_id1)))


# def testRaise(request):
#     u = get_object_or_404(User, pk=12312)
#     return render(request, "home/index.html", {"users": u})


# class testGenericView(generic.DetailView):
#     model = User
#     template_name = 'home/detail.html'
