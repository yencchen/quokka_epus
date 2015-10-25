# coding: utf-8

from quokka_themes import Themes


def configure(app, db=None):
    themes = Themes()
    themes.init_themes(app, app_identifier="quokka")

    # The code below is no longer needed since config reads database
    # try:
    #     from quokka.core.models import Config
    #     s = Config.objects.get(group='settings')
    #     settings = {i.name: i.value for i in s.values}
    #     app.config.update(settings)
    # except Exception as e:
    #     app.logger.error(str(e))
