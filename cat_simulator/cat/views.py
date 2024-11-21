from django.shortcuts import render, redirect
from .models import Cat

def welcome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cat = Cat.objects.create(name=name)
        return redirect('cat_stats')
    return render(request, 'cat/welcome.html')
def cat_stats(request):
    cat = Cat.objects.last()
    return render(request, 'cat/cat_stats.html', {'cat': cat})
def cat_action(request):
    cat = Cat.objects.last()
    action = request.POST.get('action')

    if action == 'play':
        if not cat.is_sleeping:
            cat.happiness += 15
            cat.satiety -= 10
        else:
            cat.happiness -= 5
    elif action == 'feed':
        if not cat.is_sleeping:
            cat.satiety += 15
            cat.happiness += 5
            if cat.satiety > 100:
                cat.happiness -= 30
    elif action == 'sleep':
        cat.is_sleeping = not cat.is_sleeping

    cat.save()
    return redirect('cat_stats')
