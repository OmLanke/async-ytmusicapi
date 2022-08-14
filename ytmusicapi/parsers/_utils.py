from functools import wraps

from ytmusicapi.navigation import *


def parse_menu_playlists(data, result):
    watch_menu = find_objects_by_key(nav(data, MENU_ITEMS), 'menuNavigationItemRenderer')
    for item in [_x['menuNavigationItemRenderer'] for _x in watch_menu]:
        icon = nav(item, ['icon', 'iconType'])
        if icon == 'MIX':
            watch_key = 'radioId'
        elif icon == 'MUSIC_SHUFFLE':
            watch_key = 'shuffleId'
        else:
            continue

        if watch_id := nav(
            item,
            ['navigationEndpoint', 'watchPlaylistEndpoint', 'playlistId'],
            True,
        ) or nav(
            item, ['navigationEndpoint', 'watchEndpoint', 'playlistId'], True
        ):
            result[watch_key] = watch_id


def get_item_text(item, index, run_index=0, none_if_absent=False):
    if column := get_flex_column_item(item, index):
        return (
            None
            if none_if_absent and len(column['text']['runs']) < run_index + 1
            else column['text']['runs'][run_index]['text']
        )

    else:
        return None


def get_flex_column_item(item, index):
    if len(item['flexColumns']) <= index or \
            'text' not in item['flexColumns'][index]['musicResponsiveListItemFlexColumnRenderer'] or \
            'runs' not in item['flexColumns'][index]['musicResponsiveListItemFlexColumnRenderer']['text']:
        return None

    return item['flexColumns'][index]['musicResponsiveListItemFlexColumnRenderer']


def get_fixed_column_item(item, index):
    if 'text' not in item['fixedColumns'][index]['musicResponsiveListItemFixedColumnRenderer'] or \
            'runs' not in item['fixedColumns'][index]['musicResponsiveListItemFixedColumnRenderer']['text']:
        return None

    return item['fixedColumns'][index]['musicResponsiveListItemFixedColumnRenderer']


def get_browse_id(item, index):
    if 'navigationEndpoint' not in item['text']['runs'][index]:
        return None
    else:
        return nav(item['text']['runs'][index], NAVIGATION_BROWSE_ID)


def get_dot_separator_index(runs):
    index = len(runs)
    try:
        index = runs.index({'text': ' • '})
    except ValueError:
        len(runs)
    return index


def parse_duration(duration):
    if duration is None:
        return duration
    mapped_increments = zip([1, 60, 3600], reversed(duration.split(":")))
    return sum(multiplier * int(time) for multiplier, time in mapped_increments)


def i18n(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method.__globals__['_'] = self.lang.gettext
        return method(self, *method_args, **method_kwargs)

    return _impl
