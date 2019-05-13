# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, password=None, rotate=None):
        """
        PageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'password': 'str',
            'rotate': 'str'
        }

        self.attribute_map = {
            'password': 'password',
            'rotate': 'rotate'
        }

        self._password = password
        self._rotate = rotate

    @property
    def password(self):
        """
        Gets the password of this PageRequest.
        

        :return: The password of this PageRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this PageRequest.
        

        :param password: The password of this PageRequest.
        :type: str
        """

        self._password = password

    @property
    def rotate(self):
        """
        Gets the rotate of this PageRequest.
        Sets the direction the page image is rotated. The possible settings are: left or right

        :return: The rotate of this PageRequest.
        :rtype: str
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """
        Sets the rotate of this PageRequest.
        Sets the direction the page image is rotated. The possible settings are: left or right

        :param rotate: The rotate of this PageRequest.
        :type: str
        """

        self._rotate = rotate

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
