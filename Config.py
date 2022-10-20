import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 15939361
    API_HASH = "f8beb0bd0054a717d84fbe9be12a23ea"
    BOT_TOKEN = "5696979182:AAF5nJjRjqdLT8cZO5DQqiyiUM5jg2Li1NE"
    MUST_JOIN = "@sources_cods"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
