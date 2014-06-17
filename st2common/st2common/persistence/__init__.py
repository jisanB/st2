import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Access(object):

    @classmethod
    @abc.abstractmethod
    def _get_impl(kls):
        pass

    @classmethod
    def get_by_name(kls, value):
        return kls._get_impl().get_by_name(value)

    @classmethod
    def get_by_id(kls, value):
        return kls._get_impl().get_by_id(value)

    @classmethod
    def get_all(kls):
        return kls._get_impl().get_all()

    @classmethod
    def query(kls, **query_args):
        return kls._get_impl().query(**query_args)

    @classmethod
    def add_or_update(kls, model_object):
        return kls._get_impl().add_or_update(model_object)

    @classmethod
    def delete(kls, model_object):
        return kls._get_impl().delete(model_object)