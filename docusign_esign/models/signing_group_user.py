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


class SigningGroupUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email=None, error_details=None, user_name=None):
        """
        SigningGroupUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'error_details': 'ErrorDetails',
            'user_name': 'str'
        }

        self.attribute_map = {
            'email': 'email',
            'error_details': 'errorDetails',
            'user_name': 'userName'
        }

        self._email = email
        self._error_details = error_details
        self._user_name = user_name

    @property
    def email(self):
        """
        Gets the email of this SigningGroupUser.
        

        :return: The email of this SigningGroupUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SigningGroupUser.
        

        :param email: The email of this SigningGroupUser.
        :type: str
        """

        self._email = email

    @property
    def error_details(self):
        """
        Gets the error_details of this SigningGroupUser.

        :return: The error_details of this SigningGroupUser.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this SigningGroupUser.

        :param error_details: The error_details of this SigningGroupUser.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def user_name(self):
        """
        Gets the user_name of this SigningGroupUser.
        The name of the group member.   Maximum Length: 100 characters. 

        :return: The user_name of this SigningGroupUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this SigningGroupUser.
        The name of the group member.   Maximum Length: 100 characters. 

        :param user_name: The user_name of this SigningGroupUser.
        :type: str
        """

        self._user_name = user_name

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
