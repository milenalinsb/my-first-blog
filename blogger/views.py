from django.shortcuts import render

def post_list(request):
    return render(request, 'blogger/post_list.html', {})