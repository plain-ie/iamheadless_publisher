from django.conf import settings as dj_settings

from .apps import IamheadlessPublisherConfig


class Settings:

    APP_NAME = IamheadlessPublisherConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_ITEM_MODEL_CLASS = f'{VAR_PREFIX}_ITEM_MODEL_CLASS'
    VAR_CONTENT_MODEL_CLASS = f'{VAR_PREFIX}_CONTENT_MODEL_CLASS'
    VAR_ITEM_RELATION_MODEL_CLASS = f'{VAR_PREFIX}_ITEM_RELATION_MODEL_CLASS'
    VAR_TEXT_LOOKUP_INDEX_MODEL_CLASS = f'{VAR_PREFIX}_TEXT_LOOKUP_INDEX_MODEL_CLASS'

    @property
    def ITEM_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_ITEM_MODEL_CLASS,
            f'{self.APP_NAME}.Item'
        )

    @property
    def CONTENT_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_CONTENT_MODEL_CLASS,
            f'{self.APP_NAME}.Content'
        )

    @property
    def ITEM_RELATION_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_ITEM_RELATION_MODEL_CLASS,
            f'{self.APP_NAME}.ItemRelation'
        )

    @property
    def TEXT_LOOKUP_INDEX_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TEXT_LOOKUP_INDEX_MODEL_CLASS,
            f'{self.APP_NAME}.TextLookupIndex'
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
