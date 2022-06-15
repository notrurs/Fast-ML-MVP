from django.views.generic.base import ContextMixin


class UserContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['prediction'] = {key: 'nan' for key in range(10)}
        return context
