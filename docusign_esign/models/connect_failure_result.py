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


class ConnectFailureResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, config_id=None, config_url=None, envelope_id=None, status=None, status_message=None):
        """
        ConnectFailureResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'config_id': 'str',
            'config_url': 'str',
            'envelope_id': 'str',
            'status': 'str',
            'status_message': 'str'
        }

        self.attribute_map = {
            'config_id': 'configId',
            'config_url': 'configUrl',
            'envelope_id': 'envelopeId',
            'status': 'status',
            'status_message': 'statusMessage'
        }

        self._config_id = config_id
        self._config_url = config_url
        self._envelope_id = envelope_id
        self._status = status
        self._status_message = status_message

    @property
    def config_id(self):
        """
        Gets the config_id of this ConnectFailureResult.
        Reserved: TBD

        :return: The config_id of this ConnectFailureResult.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """
        Sets the config_id of this ConnectFailureResult.
        Reserved: TBD

        :param config_id: The config_id of this ConnectFailureResult.
        :type: str
        """

        self._config_id = config_id

    @property
    def config_url(self):
        """
        Gets the config_url of this ConnectFailureResult.
        Reserved: TBD

        :return: The config_url of this ConnectFailureResult.
        :rtype: str
        """
        return self._config_url

    @config_url.setter
    def config_url(self, config_url):
        """
        Sets the config_url of this ConnectFailureResult.
        Reserved: TBD

        :param config_url: The config_url of this ConnectFailureResult.
        :type: str
        """

        self._config_url = config_url

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this ConnectFailureResult.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this ConnectFailureResult.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this ConnectFailureResult.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this ConnectFailureResult.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def status(self):
        """
        Gets the status of this ConnectFailureResult.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this ConnectFailureResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectFailureResult.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this ConnectFailureResult.
        :type: str
        """

        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this ConnectFailureResult.
        

        :return: The status_message of this ConnectFailureResult.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ConnectFailureResult.
        

        :param status_message: The status_message of this ConnectFailureResult.
        :type: str
        """

        self._status_message = status_message

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
