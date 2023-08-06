class VendeurRouter(object):
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.app_label == 'existing_db':
            return 'existing_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.app_label == 'vente':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""
        return True

        # Block relationship if one object is in the Example app and the other isn't.
        #    return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'vente':
            # The Example app should be migrated only on the example_db database.
            return db == 'default'
        elif db == 'existing_db':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False

        # No opinion for all other scenarios
        return None