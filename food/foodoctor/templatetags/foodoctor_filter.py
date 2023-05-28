from django import template

register = template.Library()


@register.filter
def get_value_with_key(dict_data: dict, key: str):
    return dict_data.get(key)


@register.filter
def get_value_with_index(list_data: list, index: int):
    return list_data[index]


@register.filter
def get_type(item):
    return type(item)
