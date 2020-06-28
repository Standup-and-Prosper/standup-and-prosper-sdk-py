# coding: utf-8


import pprint
import re

import six


class Thread(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    swagger_types = {
        'scheduled_date': 'str',
        'last_updated': 'str',
        'status': 'str',
        'responses': 'list[Response]',
    }

    attribute_map = {
        'scheduled_date': 'scheduledDate',
        'last_updated': 'lastUpdated',
        'status': 'status',
        'responses': 'responses',
    }

    def __init__(self, scheduled_date=None, last_updated=None, status=None, responses=None):
        """Thread"""
        self._scheduled_date = None
        self._last_updated = None
        self._status = None
        self._responses = None
        self.discriminator = None
        self.scheduled_date = scheduled_date
        self.last_updated = last_updated
        self.status = status
        self.responses = responses

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this Thread.

        Unique identifier for the record, can be specified on record creation.

        :return: The scheduled_date of this Thread.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this Thread.

        Unique identifier for the record, can be specified on record creation.

        :param scheduled_date: The scheduled_date of this Thread.
        :type: str
        """
        if scheduled_date is None:
            raise ValueError("Invalid value for `scheduled_date`, must not be `None`")

        self._scheduled_date = scheduled_date

    @property
    def last_updated(self):
        """Gets the last_updated of this Thread.

        A helpful last_updated for this record

        :return: The last_updated of this Thread.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Thread.

        A helpful last_updated for this record

        :param last_updated: The last_updated of this Thread.
        :type: str
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")

        self._last_updated = last_updated

    @property
    def status(self):
        """Gets the status of this Thread.


        :return: The status of this Thread.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Thread.


        :param status: The status of this Thread.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def responses(self):
        """Gets the responses of this Thread.

        The list of responses this record applies to

        :return: The responses of this Thread.
        :rtype: list[Response]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this Thread.

        The list of responses this record applies to

        :param responses: The responses of this Thread.
        :type: list[Response]
        """
        if responses is None:
            raise ValueError("Invalid value for `responses`, must not be `None`")

        self._responses = responses

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
        if issubclass(Thread, dict):
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
        if not isinstance(other, Thread):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
