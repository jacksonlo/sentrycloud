from collections import defaultdict
import requests
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread
from config import cache_file_name
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from cache import cached
from log import logger


@cached(cache_file_name)
def get_data():
    from config import sentry_url, header

    dataMap = []
    logger.info('Request to: {}'.format(sentry_url))
    response = requests.get(sentry_url, headers=header)
    dataMap = add_data(dataMap, response.json())
    while response.links['next']['results'] == 'true':
        sentry_url = response.links['next']['url']
        logger.info('Request to: {}'.format(sentry_url))
        response = requests.get(sentry_url, headers=header)
        dataMap = add_data(dataMap, response.json())

    logger.info('Total data retrieved from sentry: {}'.format(dataMap))
    return dataMap


def add_data(dataMap, data):
    for issue in data:
        dataMap.append({
            **issue['metadata'],
            'title': issue['title'],
            'culprit': issue['culprit'],
        })
    return dataMap


def count(data, field):
    counts = defaultdict(int)
    for row in data:
        counts[row[field]] += 1
    return counts


def create_word_cloud(counts, filepath):
    logger.info('Generating word cloud')
    back_coloring = imread('static/gradient.png')
    image_colors_byImg = ImageColorGenerator(back_coloring)

    wc = WordCloud(
        background_color="white",
        max_words=2000,
        mask=back_coloring,
        random_state=42,
        width=1000,
        height=1000,
        margin=2,
        relative_scaling=0,
        repeat=False,
    )
    wc.generate_from_frequencies(counts)

    # create coloring from image
    image_colors_byImg = ImageColorGenerator(back_coloring)

    plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(back_coloring, interpolation="bilinear")
    plt.axis("off")

    logger.info('Writing wordcloud image to file: {}'.format(filepath))
    wc.to_file(filepath)
