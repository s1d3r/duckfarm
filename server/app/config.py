import os

# import validators.volgactf

CONFIG = {
    'DEBUG': os.getenv('DEBUG') == '1',

    'TEAMS': {
        f'Team #{i}': f'10.60.{i}.3'
        for i in range(0, 10)
    },
    # 'FLAG_FORMAT': r'CTF\.Moscow\{[a-zA-Z\.0-9_-]+\}',
    # 'FLAG_FORMAT': r'VolgaCTF{[\w-]*\.[\w-]*\.[\w-]*}',
    'FLAG_FORMAT': r'CHANGE_FLAG_REGEX',

    #'SYSTEM_PROTOCOL': 'ructf_http',
    #'SYSTEM_URL': 'http://CHANGE_SYSTEM_URL/flags',
    #'SYSTEM_TOKEN': 'CHANGE_TOKEN',

    'SYSTEM_PROTOCOL': 'ctf01d',
    'SYSTEM_HOST': 'CHANGE_IP',
    'SYSTEM_PORT': 'CHANGE_PORT',
    'TEAM_TOKEN': 'CHANGE_TOKEN',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '10.10.10.10',
    # 'SYSTEM_PORT': '31337',
    # 'TEAM_TOKEN': '4fdcd6e54faa8991',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_VALIDATOR': 'volgactf',
    # 'SYSTEM_HOST': 'final.volgactf.ru',
    # 'SYSTEM_SERVER_KEY': validators.volgactf.get_public_key('https://final.volgactf.ru'),

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 2,
    'FLAG_LIFETIME': 5 * 60,

    # VOLGA: Don't make more than INFO_FLAG_LIMIT requests to get flag info,
    # usually should be more than SUBMIT_FLAG_LIMIT
    # 'INFO_FLAG_LIMIT': 10,

    'SERVER_PASSWORD': 'CHANGE_FARM_PASSWORD',

    # For all time-related operations
    'TIMEZONE': 'Europe/Moscow',
}
