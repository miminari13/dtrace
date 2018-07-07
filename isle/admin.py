from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from isle.models import Event, Team


class RemoveDeleteActionMixin:
    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Event)
class EventAdmin(RemoveDeleteActionMixin, admin.ModelAdmin):
    actions = ['make_active', 'make_inactive']
    list_display = ('uid', 'title', 'dt_start', 'dt_end', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('uid', 'dt_start', 'dt_end', 'data', 'title')

    def has_add_permission(self, request):
        return False

    def make_active(self, request, queryset):
        selected = request.POST.getlist('_selected_action')
        Event.objects.filter(id__in=selected).update(is_active=True)
        return HttpResponseRedirect(request.get_full_path())
    make_active.short_description = _(u'Сделать доступным для оцифровки')

    def make_inactive(self, request, queryset):
        selected = request.POST.getlist('_selected_action')
        Event.objects.filter(id__in=selected).update(is_active=False)
        return HttpResponseRedirect(request.get_full_path())
    make_inactive.short_description = _(u'Сделать недоступным для оцифровки')


@admin.register(Team)
class TeamAdmin(RemoveDeleteActionMixin, admin.ModelAdmin):
    list_display = ('event', 'name')
    search_fields = ('name', 'event__uid', 'event__title')
    filter_horizontal = ('users', )

    def has_add_permission(self, request):
        return False
