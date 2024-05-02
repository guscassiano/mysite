from django.views import generic

from blog.models import Post

class PostView(generic.ListView):  # O Django já possui diversas Views e Classes já prontas, o que fazemos muitas vezes é sobreescrevê-las
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html' #toda vez que bate na home será executado o queryset e renderizará o index.html

    # def get(self, request, *args, **kwargs):  # Neste método estamos sobreescrevendo um método que já existe no Views definido na classe acima
    #     return HttpResponse('Hello World')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'