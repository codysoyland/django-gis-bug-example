from django.test import TestCase
from bughouse.models import Bug
from django.db.models import Count
import datetime

class DateQuerysetTest(TestCase):
    fixtures = ['initial_data.json']

    def test_date_queryset(self):

        # plain (works)
        self.assertEqual(
            len(Bug.objects.dates('created', 'year')),
            1
        )

        # annotated (fails)
        self.assertEqual(
            len(Bug.objects.annotate(num_patches=Count('patches')).dates('created', 'year')),
            1
        )
