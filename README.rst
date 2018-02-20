=====
Django Signals as Methods
=====

Make django signals great again::

    # in your my_app/apps.py
    from signals_as_methods import DefaultAppConfig

    class MyAppConfig(DefaultAppConfig):
        name = 'my_app'


    # in your my_app/__init__.py
    default_app_config = 'my_app.apps.MyAppConfig'

    # in your my_app/models.py

    class MyModels(models.Model):
        some_fields = ....

        @staticmethod
        def pre_save(sender, instance, **kwargs):
            # Do some stuff
            ...

        @staticmethod
        def post_save(sender, instance, created, **kwargs):
            # Do other stuff
            ...
