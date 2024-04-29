import factory

from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory): # Aqui esta sendo criado um modelo fake do nosso User
    class Meta:
        model = User

    email = factory.Faker('safe_email')        # Gerando um email fake
    username = factory.LazyAttribute(lambda x: faker.name())     # Gerando um usuariofake

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.setpassword(password)
            if create:
                user.save()
        return user

class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)   # author fake sendo criado
    status = 0

    # Quando não declaramos as demais informações, o Django deixa como nulo. Ex.: content=''

    class Meta:
        model = Post