import random

import factory
import factory.fuzzy

from accounts.factories import UserFactory
from . import models


class RackFactory(factory.DjangoModelFactory):
    place_id = factory.Sequence(lambda n: n)
    city = factory.Faker('city')
    country = factory.Faker('country')
    problem = factory.fuzzy.FuzzyChoice(
        [models.RackProblems.there_are_no_racks,
         models.RackProblems.there_are_stupid_racks,
         models.RackProblems.there_are_too_few_racks,
        ]
    )
    author = factory.SubFactory(UserFactory)
    vote = random.randint(-100, 100)
    description = factory.Faker('text')

    class Meta:
        model = models.Rack
