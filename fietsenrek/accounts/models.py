import architect
from django.contrib.auth.models import AbstractUser


@architect.install('partition', type='range', subtype='integer',
                   constraint='100000', column='id')
class User(AbstractUser):
    pass
