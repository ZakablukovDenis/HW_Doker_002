from django.contrib import admin
from .models import Movie, Director, Actor
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'filter_param'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Максимальный'),
        ]

    def queryset(self, request, queryset=QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40, rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60, rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gt=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'director', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'budget']
    ordering = ['id']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__istartswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    # filter_horizontal = ['actors']
    filter_vertical = ['actors']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?!'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'ЗачЁтт!'
        return 'ТОПчик'

    @admin.action(description='Установить значение "USD"')
    def set_dollars(self, request, qs=QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить значение "EUR"')
    def set_euro(self, request, qs=QuerySet):
        count_upd = qs.update(currency=Movie.EUR)
        self.message_user(request, f'Было обновлено {count_upd} записей')

