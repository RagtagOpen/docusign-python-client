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


class ApiRequestLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_date_time=None, description=None, request_log_id=None, status=None):
        """
        ApiRequestLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_date_time': 'str',
            'description': 'str',
            'request_log_id': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'created_date_time': 'createdDateTime',
            'description': 'description',
            'request_log_id': 'requestLogId',
            'status': 'status'
        }

        self._created_date_time = created_date_time
        self._description = description
        self._request_log_id = request_log_id
        self._status = status

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this ApiRequestLog.
        Indicates the date and time the item was created.

        :return: The created_date_time of this ApiRequestLog.
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this ApiRequestLog.
        Indicates the date and time the item was created.

        :param created_date_time: The created_date_time of this ApiRequestLog.
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def description(self):
        """
        Gets the description of this ApiRequestLog.
        

        :return: The description of this ApiRequestLog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ApiRequestLog.
        

        :param description: The description of this ApiRequestLog.
        :type: str
        """

        self._description = description

    @property
    def request_log_id(self):
        """
        Gets the request_log_id of this ApiRequestLog.
        

        :return: The request_log_id of this ApiRequestLog.
        :rtype: str
        """
        return self._request_log_id

    @request_log_id.setter
    def request_log_id(self, request_log_id):
        """
        Sets the request_log_id of this ApiRequestLog.
        

        :param request_log_id: The request_log_id of this ApiRequestLog.
        :type: str
        """

        self._request_log_id = request_log_id

    @property
    def status(self):
        """
        Gets the status of this ApiRequestLog.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this ApiRequestLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ApiRequestLog.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this ApiRequestLog.
        :type: str
        """

        self._status = status

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
