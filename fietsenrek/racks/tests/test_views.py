from django.urls import reverse_lazy
from djet import restframework
from rest_framework import status

from accounts.factories import UserFactory
from racks.factories import RackFactory
from racks.models import Rack, RackProblems
from racks import views


class RackCreateViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackCreateView

    def test_anynomous_user_should_submit_a_rack_successfully(self):
        place_id = 42
        city = 'Warsaw'
        country = 'Poland'
        problem = RackProblems.there_are_stupid_racks
        data = {
            'place_id': place_id,
            'city': city,
            'country': country,
            'problem': problem,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert Rack.objects.count() == 1

    def test_authenticated_user_should_submit_a_rack_successfully(self):
        place_id = 42
        city = 'Warsaw'
        country = 'Poland'
        problem = RackProblems.there_are_stupid_racks
        author = UserFactory()
        data = {
            'place_id': place_id,
            'city': city,
            'country': country,
            'problem': problem,
            'author': author.pk,
        }
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert Rack.objects.count() == 1
        assert Rack.objects.first().author == author

    def test_rack_should_not_be_saved_with_incomplete_data(self):
        data = {}
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Rack.objects.count() == 0


class RackListViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackListView

    def test_view_should_return_all_racks_on_get(self):
        RackFactory.create_batch(10)
        request = self.factory.get()

        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10


class RackTopListTestCase(restframework.APIViewTestCase):
    view_class = views.RackTopListView

    def test_view_should_return_all_racks_on_get(self):
        RackFactory.create_batch(10)
        top_rack = RackFactory(vote=100000)
        low_rack = RackFactory(vote=-100000)
        request = self.factory.get()

        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10
        assert any(r['id'] == top_rack.id for r in response.data)
        assert not any(r['id'] == low_rack.id for r in response.data)


class RackVoteViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackVoteView

    def test_rack_should_be_upvoted_with_correct_data_and_1_vote(self):
        initial_vote = 42
        rack = RackFactory(vote=initial_vote)
        data = {
            'rack_id': rack.id,
            'vote': 1,
        }
        request = self.factory.patch(data=data,
                                     path=reverse_lazy('racks:vote'))

        response = self.view(request)
        rack.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert rack.vote == initial_vote + 1
