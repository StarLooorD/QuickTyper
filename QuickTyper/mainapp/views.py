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


def sentence_analyzer(text, input_text, words, start_time, end_time):
    counter = 0
    for i in range(len(text)):
        try:
            print(text[i], input_text[i])
            if text[i] == input_text[i]:
                counter += 1
        except:
            break
    accuracy = counter / len(text) * 100
    total_time = round(end_time)
    wpm = words * 60 / total_time
    return total_time, accuracy, wpm


def get_level(accuracy, wpm):
    count = wpm * accuracy
    if count > 50:
        level = 'Octopus'
    elif 40 < count < 50:
        level = 'Monkey'
    elif 30 < count < 40:
        level = 'Pigeon'
    elif 20 < count < 30:
        level = 'Bear'
    elif 0 < count < 20:
        level = 'Sloth'
    else:
        level = 'unknown'
    return level


def welcome_page(request):
    return render(request, 'mainapp/welcome_page.html')


def test_page(request):
    # words = len(text.split(' '))
    if request.method == 'GET':
        form = TextForm()
        level = get_level(0, 0)
        text = get_sentence()
        global my_obj
        new_obj = Tester(text=text, start_time=time.time())
        my_obj = new_obj
        context = {'text': text, 'form': form, 'level': level, 'time': '-', 'acc': '-', 'wpm': '-'}
        return render(request, 'mainapp/test_page.html', context)
    if request.method == 'POST':
        end_time = time.time()
        form = TextForm(request.POST)
        if form.is_valid():
            # input_text = form.cleaned_data['text']
            # total_time, accuracy, wpm = sentence_analyzer(text, input_text, words, start_time=0, end_time=2)
            # level = get_level(accuracy, wpm)
            my_obj.input_text = form.cleaned_data['text']
            my_obj.end_time = end_time
            my_obj.set_total_time()
            my_obj.set_accuracy_and_wpm()
            my_obj.set_level()
            context = {'text': my_obj.text, 'form': form, 'time': my_obj.total_time, 'acc': my_obj.accuracy,
                       'wpm': my_obj.wpm, 'level': my_obj.level}
            return render(request, 'mainapp/test_page.html', context)
