import attr
import stevedore

ENTRY_POINT_NAME = 'psy.lambda_handler'


@attr.s()
class Function(object):
    distribution = attr.ib()
    handler = attr.ib()

    @classmethod
    def functions(cls):
        manager = stevedore.ExtensionManager(ENTRY_POINT_NAME)
        for ext in manager.extensions:
            yield cls(ext.entry_point.dist, ext.name)
