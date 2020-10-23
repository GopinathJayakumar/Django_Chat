from django.shortcuts import render

from .models import Chat


# Create your views here.

def chat_details_view(request, id=1):
    obj = Chat.objects.get(id=id)
    print(obj)
    context = {"object" : obj}
    return render(request, "details_view.html", context)


def chat_list_view(request):
    queryset = Chat.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {"object_list": queryset}
    return render(request, "list_view.html", context)
