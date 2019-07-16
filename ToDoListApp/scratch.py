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
