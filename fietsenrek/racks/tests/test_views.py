from django.urls import reverse_lazy
from djet import restframework
from rest_framework import status

from accounts.factories import UserFactory
from racks.factories import RackFactory
from racks.models import Rack, RackProblems
from racks import views


class RackCreateViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackCreateView

    def test_rack_should_be_submitted_successfully__when_user_anonymous(self):
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

    def test_rack_should_be_submitted_successfully__when_user_authenticated(self):
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

    def test_rack_should_not_be_saved__when_incomplete_data(self):
        data = {}
        request = self.factory.post(data=data)

        response = self.view(request)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert Rack.objects.count() == 0


class RackListViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackListView

    def test_all_racks_should_be_returned__on_get(self):
        RackFactory.create_batch(10)
        request = self.factory.get()

        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10


class RackTopListTestCase(restframework.APIViewTestCase):
    view_class = views.RackTopListView

    def test_10_top_racks_should_be_returned__on_get(self):
        RackFactory.create_batch(10)
        top_rack = RackFactory(vote=100000)
        low_rack = RackFactory(vote=-100000)
        request = self.factory.get()

        response = self.view(request)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10
        assert any(r['id'] == top_rack.id for r in response.data)
        assert not any(r['id'] == low_rack.id for r in response.data)


class RackUpVoteViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackUpVoteView

    def test_rack_should_be_upvoted__when_rack_exists(self):
        initial_vote = 42
        rack = RackFactory(vote=initial_vote)

        request = self.factory.patch(path=reverse_lazy('racks:upvote',
                                                       kwargs={'pk': rack.pk}))

        response = self.view(request, pk=rack.pk)
        rack.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert rack.vote == initial_vote + 1

    def test_404_should_be_returned__when_rack_doesnt_exist(self):
        request = self.factory.patch(path=reverse_lazy('racks:upvote',
                                                       kwargs={'pk': 42}))

        response = self.view(request, pk=42)

        assert response.status_code == status.HTTP_404_NOT_FOUND


class RackDownVoteViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackDownVoteView

    def test_rack_should_be_downvoted__when_rack_exists(self):
        initial_vote = 42
        rack = RackFactory(vote=initial_vote)
        request = self.factory.patch(path=reverse_lazy('racks:upvote',
                                                       kwargs={'pk': rack.pk}))

        response = self.view(request, pk=rack.pk)
        rack.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert rack.vote == initial_vote - 1

    def test_404_should_be_returned__when_rack_doesnt_exist(self):
        request = self.factory.patch(path=reverse_lazy('racks:upvote',
                                                       kwargs={'pk': 42}))

        response = self.view(request, pk=42)

        assert response.status_code == status.HTTP_404_NOT_FOUND


class RackSolveViewTestCase(restframework.APIViewTestCase):
    view_class = views.RackSolveView

    def test_rack_should_be_marked_solved__on_post(self):
        rack = RackFactory()
        request = self.factory.patch(path=reverse_lazy('racks:solve',
                                                       kwargs={'pk': rack.pk}))

        response = self.view(request, pk=rack.pk)
        rack.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert rack.solved

    def test_404_should_be_returned__when_rack_doesnt_exist(self):
        request = self.factory.patch(path=reverse_lazy('racks:solve',
                                                       kwargs={'pk': 42}))

        response = self.view(request, pk=42)

        assert response.status_code == status.HTTP_404_NOT_FOUND
