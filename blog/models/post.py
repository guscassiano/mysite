from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):  #Model herda diversas funções para o models
    title = models.CharField(max_length=200, unique=True) # Criamos a coluna usuário com um campo do tipo charfield com no máximo 200 caracteres e to tipo unico, que não haverá repetição
    slug = models.SlugField(max_length=200, unique=True) # Slug é a identificação do post "URL", o campo Slugfield aceita texto e caracteres especiais
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # User já é um modelo para cadastro de usuários fornecido pelo Django, estamos só reutilizando
    updated_on = models.DateTimeField(auto_now=True) # retorna o horario da atualização
    content = models.TextField() # é um campo que aceita trextos maiores
    created_on = models.DateTimeField(auto_now_add=True) # retorna o horario da criação
    status = models.IntegerField(choices=STATUS, default=0) # status pode ser "publish(Publicar)" ou "Draft(Rascunho)", o choices seria um array de objetos, neste caso: [(0, 'Draft'), (1, 'Publish')]

    class Meta: # Metaclasse que especifica metadados no modelo, como a ordenação padrão neste caso
        ordering = ['-created_on']  # a forma de ordenação dos dados, será pelo ordem que foram criados

    def __str__(self): # Método para retornar uma representação em string do objeto
        return self.title  # retorna os titulos dos posts para representar o objeto