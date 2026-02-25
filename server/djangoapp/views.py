from django.http import JsonResponse
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})
