#Class for hwbi_db routing
class HwbiRouter(object):
    """
    A router to control all database operations on models in the
    hwbi application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read hem models go to hwbi_db.
        """
        if model._meta.app_label == 'hwbi_app':
            return 'hwbi_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the hem app only appears in the 'hwbi_db'
        database.
        """
        if app_label == 'hwbi_app':
            return db == 'hwbi_db'
        return None
