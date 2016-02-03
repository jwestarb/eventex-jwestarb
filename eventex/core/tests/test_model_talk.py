from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = 'Título da palestra',
            start = '10:00',
            description = 'Descrição da palestra.'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many speakers and vice-versa"""
        self.talk.speakers.create(
            name = 'Julio Cesar Westarb Jr.',
            slug = 'julio-cesar',
            website = 'http://hbn.link/julio-site'
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_description_can_be_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_can_be_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_can_be_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_can_be_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEquals('Título da palestra', str(self.talk))