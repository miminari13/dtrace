from urllib import parse
from django import template
from isle.forms import EventMaterialForm

register = template.Library()


@register.filter
def add_class(value, arg):
    old_class = value.field.widget.attrs.get('class')
    if old_class:
        new_class = '{} {}'.format(old_class, arg)
    else:
        new_class = arg
    value.field.widget.attrs.update({'class': new_class})
    return value


@register.filter
def set_placeholder(value, arg):
    value.field.widget.attrs['placeholder'] = arg
    return value


@register.inclusion_tag('includes/_material_event_block.html')
def render_event_block_form(prefix, event):
    """
    отрисовка форм с различными префиксами, чтобы автокомплиты не конфликтовали
    """
    return {'blocks_form': EventMaterialForm(event=event, prefix=prefix)}


@register.filter
def user_can_edit_team(team, user):
    return team.user_can_edit_team(user)


@register.filter
def add_page_num(url, page_num):
    parts = parse.urlparse(url)
    query = dict(parse.parse_qsl(parts.query))
    query['page'] = str(page_num)
    parts = list(parts)
    parts[4] = parse.urlencode(query)
    return parse.urlunparse(parts)


@register.filter
def show_block(block):
    return any(len(result.results) for result in block.results.all()) if block.deleted else True


@register.filter
def show_result(result):
    return len(result.results) if result.deleted or result.block.deleted else True


@register.simple_tag
def item_not_in_container(item, container):
    return item not in container

  
@register.simple_tag(takes_context=True)
def upload_files_compact_view(context):
    cnt = 0
    for block in context['blocks'] or []:
        personal_result_only = not block.deleted and context.get('can_upload') and context.get('user_upload') and \
                               block.block_has_only_group_results()
        group_result_only = not block.deleted and context.get('can_upload') and context.get('team_upload') and \
                            block.block_has_only_personal_results()
        if personal_result_only or group_result_only:
            cnt += 1
            continue
        if show_block(block):
            for result in block.results.all():
                if show_result(result) and (context.get('user_upload') and result.is_personal() or
                                            context.get('team_upload') and result.is_group() or
                                            result.results):
                    cnt += 1
    return cnt == 1
