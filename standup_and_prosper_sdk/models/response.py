# coding: utf-8


import pprint
import re

import six


class Response(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    swagger_types = {
        'question': 'Question',
        'users': 'list[UserResponse]'
    }

    attribute_map = {
        'question': 'question',
        'users': 'users'
    }

    def __init__(self, question=None, users=None):
        """Response"""
        self._question = None
        self._users = None
        self.discriminator = None
        self.question = question
        self.users = users

    @property
    def question(self):
        """Gets the question of this Response.


        :return: The question of this Response.
        :rtype: Question
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this Response.


        :param question: The question of this Response.
        :type: Question
        """
        if question is None:
            raise ValueError("Invalid value for `question`, must not be `None`")

        self._question = question

    @property
    def users(self):
        """Gets the users of this Response.


        :return: The users of this Response.
        :rtype: list[UserResponse]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Response.


        :param users: The users of this Response.
        :type: list[UserResponse]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")

        self._users = users

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
