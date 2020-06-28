# coding: utf-8


import pprint
import re

import six


class ThreadCollection(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    swagger_types = {
        'threads': 'list[Thread]'
    }

    attribute_map = {
        'threads': 'threads'
    }

    def __init__(self, threads=None):
        """ThreadCollection"""
        self._threads = None
        self.discriminator = None
        self.threads = threads

    @property
    def threads(self):
        """Gets the threads of this ThreadCollection.


        :return: The threads of this ThreadCollection.
        :rtype: list[ResourcePermission]
        """
        return self._threads

    @threads.setter
    def threads(self, threads):
        """Sets the threads of this ThreadCollection.


        :param threads: The threads of this ThreadCollection.
        :type: ResourcePermission
        """
        if threads is None:
            raise ValueError("Invalid value for `threads`, must not be `None`")

        self._threads = threads

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ThreadCollection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThreadCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
