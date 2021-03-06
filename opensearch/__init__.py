#coding:utf8

"""
Created on 2015-11-18

@author: tufei
@description:
         
Copyright (c) 2015 infohold inc. All rights reserved.
"""
import logging
import logging.config


# version is a human-readable version number.
version = "0.1.0"

# version_info is a four-tuple for programmatic comparison. The first
# three numbers are the components of the version number.  The fourth
# is zero for an official release, positive for a development branch,
# or negative for a release candidate or beta (after the base version
# number has been incremented)
version_info = (0, 1, 0, 0)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'opensearch': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}


logging.config.dictConfig(LOGGING_CONFIG)
log = logging.getLogger('opensearch')
