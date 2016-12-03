import random

import factory
import factory.fuzzy

from accounts.factories import UserFactory
from . import models


class RackFactory(factory.DjangoModelFactory):
    place_id = factory.Sequence(lambda n: n)
    city = factory.Faker('city')
    country = factory.Faker('country')
    problem = factory.fuzzy.FuzzyChoice(models.RackProblems.__dict__)
    author = factory.SubFactory(UserFactory)
    vote = random.randint(-100, 100)

    class Meta:
        model = models.Rack
