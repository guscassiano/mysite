from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):  # O Django já possui diversas Views e Classes já prontas, o que fazemos muitas vezes é sobreescrevê-las
    def get(self, request, *args, **kwargs):  # Neste método estamos sobreescrevendo um método que já existe no Views definido na classe acima
        return HttpResponse('Hello World')