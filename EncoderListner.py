import abc

class IEncoderListener(object, metaclass=abc.ABCMeta):
    """
    Interface for encoder listeners
    """
    @abc.abstractmethod
    def newAngularPosition(self, coord, orientation ):
        raise NotImplementedError('users must define newPosition to use this base class')
