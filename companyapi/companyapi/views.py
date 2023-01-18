from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    list = [
        'VIJAY',
        'DAHIYA',
        'ANKIT'
    ]
    return JsonResponse(list, safe= False)