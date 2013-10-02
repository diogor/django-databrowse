from django.test import TestCase
import django_databrowse
from . import SomeModel, SomeOtherModel, YetAnotherModel


class DatabrowseTests(TestCase):

    @classmethod
    def tearDownClass(self):
        django_databrowse.site.unregister(SomeModel)

    def test_databrowse_register_unregister(self):
        django_databrowse.site.register(SomeModel)
        self.assertTrue(SomeModel in django_databrowse.site.registry)
        django_databrowse.site.register(SomeOtherModel, YetAnotherModel)
        self.assertTrue(SomeOtherModel in django_databrowse.site.registry)
        self.assertTrue(YetAnotherModel in django_databrowse.site.registry)

        self.assertRaisesMessage(
            django_databrowse.sites.AlreadyRegistered,
            'The model SomeModel is already registered',
            django_databrowse.site.register, SomeModel, SomeOtherModel
        )

        django_databrowse.site.unregister(SomeOtherModel)
        self.assertFalse(SomeOtherModel in django_databrowse.site.registry)
        django_databrowse.site.unregister(SomeModel, YetAnotherModel)
        self.assertFalse(SomeModel in django_databrowse.site.registry)
        self.assertFalse(YetAnotherModel in django_databrowse.site.registry)

        self.assertRaisesMessage(
            django_databrowse.sites.NotRegistered,
            'The model SomeModel is not registered',
            django_databrowse.site.unregister, SomeModel, SomeOtherModel
        )

        self.assertRaisesMessage(
            django_databrowse.sites.AlreadyRegistered,
            'The model SomeModel is already registered',
            django_databrowse.site.register, SomeModel, SomeModel
        )
