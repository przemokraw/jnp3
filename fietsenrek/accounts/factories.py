import factory

from .models import User


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('first_name')
    email = factory.LazyAttribute(lambda u: '{}@fietsenrek.io'.
                                  format(u.username))

    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = 'test123'
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super()._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user
