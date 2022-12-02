"""
App configuration for eox_rates.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EoxRatesConfig(AppConfig):
    """
    Eox rates configuration.
    """
    name = 'eox_rates'
    verbose_name = 'Eox rates'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'eox_rates',
                'regex': r'^eox_rates/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'eox_rates',
                'regex': r'^eox_rates/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
