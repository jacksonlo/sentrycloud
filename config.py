import os


token = os.environ.get('sentrycloudtoken')
sentry_url = os.environ.get('sentryurl')
header = {'Authorization': 'Bearer {}'.format(token)}
cache_file_name = '.sentry_data.cache'
