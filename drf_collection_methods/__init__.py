class CollectionMethodRouterMixin(object):
    def get_routes(self, viewset):
        # do some magic to hooked up our decorated methods


def collection_link(**kwargs):
    def decorator(func):
        func.bind_to_collection_methods = ['get']
        func.kwargs = kwargs
        return func
    return decorator


def collection_action(methods=['post'], **kwargs):
    def decorator(func):
        func.bind_to_collection_methods = methods
        func.kwargs = kwargs
        return func
    return decorator
