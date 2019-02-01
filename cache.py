import os
import pickle
from log import logger


def cached(cachefile):
    """
    Simple decorator that pickles result to file from:
    https://datascience.blog.wzb.eu/2016/08/12/a-tip-for-the-impatient-simple-caching-with-python-pickle-and-decorators/

    Modified logging
    """
    def decorator(fn):
        def wrapped(*args, **kwargs):
            if os.path.exists(cachefile):
                    with open(cachefile, 'rb') as cachehandle:
                        logger.info("Using cached result from '%s'" % cachefile)
                        return pickle.load(cachehandle)

            res = fn(*args, **kwargs)

            with open(cachefile, 'wb') as cachehandle:
                logger.info("Saving result to cache '%s'" % cachefile)
                pickle.dump(res, cachehandle)

            return res

        return wrapped

    return decorator
