# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class BulkSendingList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bulk_copies': 'list[BulkSendingCopy]',
        'list_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'bulk_copies': 'bulkCopies',
        'list_id': 'listId',
        'name': 'name'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BulkSendingList - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bulk_copies = None
        self._list_id = None
        self._name = None
        self.discriminator = None

        setattr(self, "_{}".format('bulk_copies'), kwargs.get('bulk_copies', None))
        setattr(self, "_{}".format('list_id'), kwargs.get('list_id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))

    @property
    def bulk_copies(self):
        """Gets the bulk_copies of this BulkSendingList.  # noqa: E501

          # noqa: E501

        :return: The bulk_copies of this BulkSendingList.  # noqa: E501
        :rtype: list[BulkSendingCopy]
        """
        return self._bulk_copies

    @bulk_copies.setter
    def bulk_copies(self, bulk_copies):
        """Sets the bulk_copies of this BulkSendingList.

          # noqa: E501

        :param bulk_copies: The bulk_copies of this BulkSendingList.  # noqa: E501
        :type: list[BulkSendingCopy]
        """

        self._bulk_copies = bulk_copies

    @property
    def list_id(self):
        """Gets the list_id of this BulkSendingList.  # noqa: E501

          # noqa: E501

        :return: The list_id of this BulkSendingList.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this BulkSendingList.

          # noqa: E501

        :param list_id: The list_id of this BulkSendingList.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def name(self):
        """Gets the name of this BulkSendingList.  # noqa: E501

          # noqa: E501

        :return: The name of this BulkSendingList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulkSendingList.

          # noqa: E501

        :param name: The name of this BulkSendingList.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(BulkSendingList, dict):
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
        if not isinstance(other, BulkSendingList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendingList):
            return True

        return self.to_dict() != other.to_dict()