from django.apps import AppConfig


class AppConfig(AppConfig):
    name = '.'.join(__name__.split('.')[:-1])
    label = "ik_event_listing"
    verbose_name = "Event Content Listing"
