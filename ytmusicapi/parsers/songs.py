from ._utils import *
import re


def parse_song_artists(data, index):
    if flex_item := get_flex_column_item(data, index):
        runs = flex_item['text']['runs']
        return parse_song_artists_runs(runs)
    else:
        return None


def parse_song_artists_runs(runs):
    return [
        {
            'name': runs[j * 2]['text'],
            'id': nav(runs[j * 2], NAVIGATION_BROWSE_ID, True),
        }
        for j in range(len(runs) // 2 + 1)
    ]


def parse_song_runs(runs):
    parsed = {'artists': []}
    for i, run in enumerate(runs):
        if i % 2:  # uneven items are always separators
            continue
        text = run['text']
        if 'navigationEndpoint' in run:  # artist or album
            item = {'name': text, 'id': nav(run, NAVIGATION_BROWSE_ID, True)}

            if item['id'] and (item['id'].startswith('MPRE')
                               or "release_detail" in item['id']):  # album
                parsed['album'] = item
            else:  # artist
                parsed['artists'].append(item)

        elif re.match(r"^\d([^ ])* [^ ]*$", text):
            parsed['views'] = text.split(' ')[0]

        elif re.match(r"^(\d+:)*\d+:\d+$", text):
            parsed['duration'] = text
            parsed['duration_seconds'] = parse_duration(text)

        elif re.match(r"^\d{4}$", text):
            parsed['year'] = text

        else:  # artist without id
            parsed['artists'].append({'name': text, 'id': None})

    return parsed


def parse_song_album(data, index):
    flex_item = get_flex_column_item(data, index)
    return (
        {'name': get_item_text(data, index), 'id': get_browse_id(flex_item, 0)}
        if flex_item
        else None
    )


def parse_song_menu_tokens(item):
    toggle_menu = item[TOGGLE_MENU]
    service_type = toggle_menu['defaultIcon']['iconType']
    library_add_token = nav(toggle_menu, ['defaultServiceEndpoint'] + FEEDBACK_TOKEN, True)
    library_remove_token = nav(toggle_menu, ['toggledServiceEndpoint'] + FEEDBACK_TOKEN, True)

    if service_type == "LIBRARY_REMOVE":  # swap if already in library
        library_add_token, library_remove_token = library_remove_token, library_add_token

    return {'add': library_add_token, 'remove': library_remove_token}


def parse_like_status(service):
    status = ['LIKE', 'INDIFFERENT']
    return status[status.index(service['likeEndpoint']['status']) - 1]
