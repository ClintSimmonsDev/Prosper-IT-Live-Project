from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect

def ToDoListApp(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'ToDoListApp.html', {'all_items': all_items})
        else:
            all_items = List.objects.all
            return render(request, 'ToDoListApp.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'ToDoListApp.html', {'all_items': all_items})

def today(request):
    if request.method == 'POST':
        form = ListForm_today(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List_today.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'today.html', {'all_items': all_items})
        else:
            all_items = List_today.objects.all
            return render(request, 'today.html', {'all_items': all_items})
    else:
        all_items = List_today.objects.all
        return render(request, 'today.html', {'all_items': all_items})

def this_week(request):
    if request.method == 'POST':
        form = ListForm_week(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List_thisweek.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'this_week.html', {'all_items': all_items})
        else:
            all_items = List_thisweek.objects.all
            return render(request, 'this_week.html', {'all_items': all_items})
    else:
        all_items = List_thisweek.objects.all
        return render(request, 'this_week.html', {'all_items': all_items})

def this_month(request):
    if request.method == 'POST':
        form = ListForm_month(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List_thismonth.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'this_month.html', {'all_items': all_items})
        else:
            all_items = List_thismonth.objects.all
            return render(request, 'this_month.html', {'all_items': all_items})
    else:
        all_items = List_thismonth.objects.all
        return render(request, 'this_month.html', {'all_items': all_items})

def spare_time_tasks(request):
    if request.method == 'POST':
        form = ListForm_spare(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List_spare_time.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'spare_time_tasks.html', {'all_items': all_items})
        else:
            all_items = List_spare_time.objects.all
            return render(request, 'spare_time_tasks.html', {'all_items': all_items})
    else:
        all_items = List_spare_time.objects.all
        return render(request, 'spare_time_tasks.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('ToDoListApp')

def delete_today(request, list_id):
    item = List_today.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('today')

def delete_thisweek(request, list_id):
    item = List_thisweek.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('this_week')

def delete_thismonth(request, list_id):
    item = List_thismonth.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('this_month')

def delete_spare_time(request, list_id):
    item = List_spare_time.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('spare_time_tasks')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('ToDoListApp')

def cross_off_today(request, list_id):
    item = List_today.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('today')

def cross_off_thisweek(request, list_id):
    item = List_thisweek.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('this_week')

def cross_off_thismonth(request, list_id):
    item = List_thismonth.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('this_month')

def cross_off_spare_time(request, list_id):
    item = List_spare_time.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('spare_time_tasks')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('ToDoListApp')

def uncross_today(request, list_id):
    item = List_today.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('today')

def uncross_thisweek(request, list_id):
    item = List_thisweek.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('this_week')

def uncross_thismonth(request, list_id):
    item = List_thismonth.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('this_month')
    
def uncross_spare_time(request, list_id):
    item = List_spare_time.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('spare_time_tasks')