from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save, pre_init, post_init, pre_delete, post_delete


class DefaultAppConfig(AppConfig):
    model_signals = {
        'post_save': post_save,
        'pre_save': pre_save,
        'pre_init': pre_init,
        'post_init': post_init,
        'pre_delete': pre_delete,
        'post_delete': post_delete,
    }

    def ready(self):
        for model in self.get_models():
            for signal_name, signal in self.model_signals.items():
                if hasattr(model, signal_name):
                    method = getattr(model, signal_name)
                    if hasattr(method, "__call__"):
                        signal.connect(getattr(model, signal_name),
                                       sender=model, dispatch_uid=model.__name__+"_"+signal_name)
        return super(DefaultAppConfig, self).ready()
