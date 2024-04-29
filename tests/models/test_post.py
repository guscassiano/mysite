import pytest

from blog.factories import PostFactory

@pytest.fixture  # Contruido
def post_published():
    return PostFactory(title='pytest with factory') # Cria um post fake com o titulo de 'pytest with factory' e retorna o post no que a função é chamada

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory' # Compara se o title que foi criado no PostFactory é o mesmo, se sim, o teste passa