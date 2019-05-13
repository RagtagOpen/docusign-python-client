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


class RecipientPhoneAuthentication(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, recip_may_provide_number=None, record_voice_print=None, sender_provided_numbers=None, validate_recip_provided_number=None):
        """
        RecipientPhoneAuthentication - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'recip_may_provide_number': 'str',
            'record_voice_print': 'str',
            'sender_provided_numbers': 'list[str]',
            'validate_recip_provided_number': 'str'
        }

        self.attribute_map = {
            'recip_may_provide_number': 'recipMayProvideNumber',
            'record_voice_print': 'recordVoicePrint',
            'sender_provided_numbers': 'senderProvidedNumbers',
            'validate_recip_provided_number': 'validateRecipProvidedNumber'
        }

        self._recip_may_provide_number = recip_may_provide_number
        self._record_voice_print = record_voice_print
        self._sender_provided_numbers = sender_provided_numbers
        self._validate_recip_provided_number = validate_recip_provided_number

    @property
    def recip_may_provide_number(self):
        """
        Gets the recip_may_provide_number of this RecipientPhoneAuthentication.
        Boolean. When set to **true**, the recipient can supply a phone number their choice.

        :return: The recip_may_provide_number of this RecipientPhoneAuthentication.
        :rtype: str
        """
        return self._recip_may_provide_number

    @recip_may_provide_number.setter
    def recip_may_provide_number(self, recip_may_provide_number):
        """
        Sets the recip_may_provide_number of this RecipientPhoneAuthentication.
        Boolean. When set to **true**, the recipient can supply a phone number their choice.

        :param recip_may_provide_number: The recip_may_provide_number of this RecipientPhoneAuthentication.
        :type: str
        """

        self._recip_may_provide_number = recip_may_provide_number

    @property
    def record_voice_print(self):
        """
        Gets the record_voice_print of this RecipientPhoneAuthentication.
        Reserved.

        :return: The record_voice_print of this RecipientPhoneAuthentication.
        :rtype: str
        """
        return self._record_voice_print

    @record_voice_print.setter
    def record_voice_print(self, record_voice_print):
        """
        Sets the record_voice_print of this RecipientPhoneAuthentication.
        Reserved.

        :param record_voice_print: The record_voice_print of this RecipientPhoneAuthentication.
        :type: str
        """

        self._record_voice_print = record_voice_print

    @property
    def sender_provided_numbers(self):
        """
        Gets the sender_provided_numbers of this RecipientPhoneAuthentication.
        An Array containing a list of phone numbers the recipient may use for SMS text authentication. 

        :return: The sender_provided_numbers of this RecipientPhoneAuthentication.
        :rtype: list[str]
        """
        return self._sender_provided_numbers

    @sender_provided_numbers.setter
    def sender_provided_numbers(self, sender_provided_numbers):
        """
        Sets the sender_provided_numbers of this RecipientPhoneAuthentication.
        An Array containing a list of phone numbers the recipient may use for SMS text authentication. 

        :param sender_provided_numbers: The sender_provided_numbers of this RecipientPhoneAuthentication.
        :type: list[str]
        """

        self._sender_provided_numbers = sender_provided_numbers

    @property
    def validate_recip_provided_number(self):
        """
        Gets the validate_recip_provided_number of this RecipientPhoneAuthentication.
         Reserved.

        :return: The validate_recip_provided_number of this RecipientPhoneAuthentication.
        :rtype: str
        """
        return self._validate_recip_provided_number

    @validate_recip_provided_number.setter
    def validate_recip_provided_number(self, validate_recip_provided_number):
        """
        Sets the validate_recip_provided_number of this RecipientPhoneAuthentication.
         Reserved.

        :param validate_recip_provided_number: The validate_recip_provided_number of this RecipientPhoneAuthentication.
        :type: str
        """

        self._validate_recip_provided_number = validate_recip_provided_number

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
