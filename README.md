# Wordcloud for Sentry exception issues
Quick and short hackday project that generates a wordcloud on fields from sentry issues from the Sentry.io API.

## Required environment variables:
```
sentryurl
Example: https://sentry.io/api/0/projects/{PROJECT}/app/issues/?query=is%3Aunresolved+is%3Aunassigned&sort=date&environment=production
```
```
sentrycloudtoken
Example: askdjalsjdklajsdkjasd
Generate this from sentry.io: https://sentry.io/settings/account/api/auth-tokens/
```
## Usage via CLI
1. `pip install -r requirements.txt`
2. `python main.py --field culprit --file super.png --verbose True --cache False`

### Parameters:
#### field
```
Values: [culprit, filename, title, type]
Default: title
```
The field from sentry to generate the wordcloud with.

#### file
```
Default: result.png
Example: result.png
```
The filepath to generate the image to.

#### verbose
```
Values: [True, False]
Default: False
```
Logging verbosity.


#### cache
```
Values: [True, False]
Default: False
```
Caches the result from the sentry.io API call to local file. False will not save the result to cache as well as remove
existing cache results.

## Usage via browser
1. `pip install -r requirements.txt`
2. `./run` to run webserver

Go to one of:
```
http://localhost:5000/?field=title
http://localhost:5000/?field=type
http://localhost:5000/?field=filename
http://localhost:5000/?field=culprit
```
