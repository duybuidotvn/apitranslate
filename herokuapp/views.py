from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests   
from django.views.decorators.csrf import csrf_exempt  

# Create your views here.
 
 
def index(request):
    return render(request, "home/index.html", {"users": 1})

@csrf_exempt
def search(request):
    
    fromLocation = ''
    try:
        fromLocation = request.POST['cauHoi']
    except (KeyError):
        # Redisplay the question voting form.
        param = {
            "cauHoi": '',
            "traLoi": '', 
        }
        return render(request, "home/chat.html", param)
    
    # translate
    param = {
        "cauHoi": fromLocation,
        "traLoi": ApiTranslate.translate(fromLocation)[:-5], 
    } 
 
    return render(request, "home/chat.html", param)


# def detail(request, request_id):
#     print(request_id)
#     return render(request, "home/chi-tiet-xe.html", {"id": request_id})


# def step1(request, request_id):
#     print(request_id)
#     return render(request, "home/dat-ve-buoc-1.html", {"id": request_id})

# def step2(request, request_id):
#     print(request_id)
#     return render(request, "home/dat-ve-buoc-2.html", {"id": request_id})

# def step3(request, request_id):
#     print(request_id)
#     return render(request, "home/dat-ve-buoc-3.html", {"id": request_id})


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



# deep learning begin
# from __future__ import unicode_literals, print_function, division
import torch

from core_translate.Encoder import EncoderRNN
from core_translate.AttnDecoder import AttnDecoderRNN
from core_translate.ultis import prepareData, evaluate

use_cuda = torch.cuda.is_available()

MAX_LENGTH = 50

TRANSLATION = "eng-vn"
input_lang, output_lang, pairs = prepareData(TRANSLATION.split("-")[0],
                                             TRANSLATION.split('-')[1])

teacher_forcing_ratio = 0.5
hidden_size = 256
encoder1 = EncoderRNN(input_lang.n_words, hidden_size)
attn_decoder1 = AttnDecoderRNN(hidden_size, output_lang.n_words,
                               1, dropout_p=0.1)
if use_cuda:
    encoder1 = encoder1.cuda()
    attn_decoder1 = attn_decoder1.cuda()


encoder1.load_state_dict(torch.load("core_translate/nmt_model/%s_encoder1.pth.tar"%TRANSLATION, map_location={'cuda:0': 'cpu'}))
encoder1.eval()

attn_decoder1.load_state_dict(torch.load("core_translate/nmt_model/%s_attn_decoder1.pth.tar"%TRANSLATION, map_location={'cuda:0': 'cpu'}))
attn_decoder1.eval()

class ApiTranslate:
    @staticmethod
    def translate(input_sentence=""):
        output_words, attentions = evaluate(input_lang, output_lang, encoder1, attn_decoder1, input_sentence)
        return ' '.join(output_words)

    @staticmethod
    def init():
        input_sentence = "i love you"
        print("Input Sentence: ", input_sentence)
        output_words, attentions = evaluate(input_lang, output_lang, encoder1, attn_decoder1, input_sentence)
        print("Output Sentence:", ' '.join(output_words))
# deep learning end 