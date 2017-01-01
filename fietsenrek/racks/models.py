from django.db import models
from django.contrib.auth.models import User


class RackProblems:
    there_are_no_racks = 1
    there_are_too_few_racks = 2
    there_are_stupid_racks = 3
    CHOICES = (
        (there_are_no_racks, 'There are no racks'),
        (there_are_too_few_racks, 'There are too few racks'),
        (there_are_stupid_racks, 'The racks are not safe'),
    )


class Rack(models.Model):
    place_id = models.CharField(max_length=128)  # Google Maps place_id
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    problem = models.CharField(choices=RackProblems.CHOICES, max_length=16)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='racks')
    author = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    solved = models.BooleanField(default=False)
    solution_photo = models.ImageField(blank=True, upload_to='racks_solutions')

    def __str__(self):
        return '{} in {}'.format(self.place_id, self.city)

    def up_vote(self):
        self.vote += 1
        self.save()
        return self

    def down_vote(self):
        self.vote -= 1
        self.save()
        return self

    def solve(self):
        self.solved = True
        self.save()
        return self
