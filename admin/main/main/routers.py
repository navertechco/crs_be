from django.conf import settings


class PostgresRouter:
    route_app_labels = [
        "postgres",
    ]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:  # noqa
            return settings.DMS_DB_ROUTER
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:  # noqa
            return settings.DMS_DB_ROUTER
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels  # noqa
            or obj2._meta.app_label in self.route_app_labels  # noqa
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == settings.DMS_DB_ROUTER
        return False