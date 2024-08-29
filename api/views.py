from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def get_word(request):
    # 示例数据
    word = 'makbaka'
    return JsonResponse({'word': word})
