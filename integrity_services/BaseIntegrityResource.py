from abc import ABC, abstractmethod


class BaseIntegrityException(Exception):

    def __init__(self):
        pass


class BaseIntegrityResource(ABC):

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def get_responses(cls, res):
        pass

    @classmethod
    @abstractmethod
    def input_validation(cls, data):
        pass

    @classmethod
    @abstractmethod
    def post_responses(cls, res):
        pass

    @classmethod
    @abstractmethod
    def put_responses(cls, res):
        pass

    @classmethod
    @abstractmethod
    def delete_responses(cls, res):
        pass


class ValidationFunction():
    def __init__(self, fn, error_msg):
        self.fn = fn
        self.error_msg = error_msg

    def validate(self, input):
        return self.fn(input)


