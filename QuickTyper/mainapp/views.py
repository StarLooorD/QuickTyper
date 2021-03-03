from django.shortcuts import render, redirect
from django.http import request
from .forms import TextForm
from .tester import Tester
import random
import time


def redirect_welcome(request):
    return redirect('welcome_page')


def get_sentence():
    with open('sentences.txt', 'r') as file:
        sentences = file.read().split('\n')
        rand_sentence = random.choice(sentences)
        return rand_sentence


def welcome_page(request):
    return render(request, 'mainapp/welcome_page.html')


def test_page(request):

    if request.method == 'GET':
        form = TextForm()
        text = get_sentence()
        global my_obj
        my_obj = Tester(text=text, start_time=time.time())
        context = {'text': text,
                   'form': form,
                   'level': 'unknown',
                   'time': '-',
                   'acc': '-',
                   'wpm': '-'}
        return render(request, 'mainapp/test_page.html', context)

    if request.method == 'POST':
        end_time = time.time()
        form = TextForm(request.POST)
        if form.is_valid():
            my_obj.input_text = form.cleaned_data['text']
            my_obj.end_time = end_time
            my_obj.set_total_time()
            my_obj.set_accuracy_and_wpm()
            my_obj.set_level()
            context = {'text': my_obj.text,
                       'form': form,
                       'time': my_obj.total_time,
                       'acc': my_obj.accuracy,
                       'wpm': my_obj.wpm,
                       'level': my_obj.level}
            return render(request, 'mainapp/test_page.html', context)
