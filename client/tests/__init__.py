
from client import main


import pytest

class TestMain:

    # Configurator is created with the given settings
    def test_configurator_created_with_given_settings(self):
        global_config = None
        settings = {}
        result = main(global_config, **settings)
        assert isinstance(result, Configurator)
        assert result.settings == settings

    # pyramid_jinja2 is included in the configuration
    def test_pyramid_jinja2_included_in_configuration(self):
        global_config = None
        settings = {}
        result = main(global_config, **settings)
        assert 'pyramid_jinja2' in result.includes

    # .routes is included in the configuration
    def test_routes_included_in_configuration(self):
        global_config = None
        settings = {}
        result = main(global_config, **settings)
        assert '.routes' in result.includes

    # global_config is None
    def test_global_config_is_none(self):
        global_config = None
        settings = {}
        result = main(global_config, **settings)
        assert result.global_config is None

    # settings is empty
    def test_settings_is_empty(self):
        global_config = None
        settings = {}
        result = main(global_config, **settings)
        assert result.settings == {}

    # pyramid_jinja2 cannot be included
    def test_pyramid_jinja2_cannot_be_included(self):
        global_config = None
        settings = {'pyramid_jinja2': False}
        result = main(global_config, **settings)
        assert 'pyramid_jinja2' not in result.includes
