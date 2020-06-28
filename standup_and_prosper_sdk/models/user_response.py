# coding: utf-8


import pprint
import re

import six


class UserResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'text': 'text'
    }

    def __init__(self, user_id=None, text=None):
        """UserResponse"""
        self._user_id = None
        self._text = None
        self.discriminator = None
        self.user_id = user_id
        self.text = text

    @property
    def user_id(self):
        """Gets the user_id of this UserResponse.


        :return: The user_id of this UserResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserResponse.


        :param user_id: The user_id of this UserResponse.
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def text(self):
        """Gets the text of this UserResponse.


        :return: The text of this UserResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this UserResponse.


        :param text: The text of this UserResponse.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

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
        if issubclass(UserResponse, dict):
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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
