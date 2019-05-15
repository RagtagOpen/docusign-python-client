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


class FolderItemResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, end_position=None, folder_items=None, next_uri=None, previous_uri=None, result_set_size=None, start_position=None, total_rows=None):
        """
        FolderItemResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_position': 'str',
            'folder_items': 'list[FolderItemV2]',
            'next_uri': 'str',
            'previous_uri': 'str',
            'result_set_size': 'str',
            'start_position': 'str',
            'total_rows': 'str'
        }

        self.attribute_map = {
            'end_position': 'endPosition',
            'folder_items': 'folderItems',
            'next_uri': 'nextUri',
            'previous_uri': 'previousUri',
            'result_set_size': 'resultSetSize',
            'start_position': 'startPosition',
            'total_rows': 'totalRows'
        }

        self._end_position = end_position
        self._folder_items = folder_items
        self._next_uri = next_uri
        self._previous_uri = previous_uri
        self._result_set_size = result_set_size
        self._start_position = start_position
        self._total_rows = total_rows

    @property
    def end_position(self):
        """
        Gets the end_position of this FolderItemResponse.
        The last position in the result set. 

        :return: The end_position of this FolderItemResponse.
        :rtype: str
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        """
        Sets the end_position of this FolderItemResponse.
        The last position in the result set. 

        :param end_position: The end_position of this FolderItemResponse.
        :type: str
        """

        self._end_position = end_position

    @property
    def folder_items(self):
        """
        Gets the folder_items of this FolderItemResponse.
        A list of the envelopes in the specified folder or folders. 

        :return: The folder_items of this FolderItemResponse.
        :rtype: list[FolderItemV2]
        """
        return self._folder_items

    @folder_items.setter
    def folder_items(self, folder_items):
        """
        Sets the folder_items of this FolderItemResponse.
        A list of the envelopes in the specified folder or folders. 

        :param folder_items: The folder_items of this FolderItemResponse.
        :type: list[FolderItemV2]
        """

        self._folder_items = folder_items

    @property
    def next_uri(self):
        """
        Gets the next_uri of this FolderItemResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :return: The next_uri of this FolderItemResponse.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri):
        """
        Sets the next_uri of this FolderItemResponse.
        The URI to the next chunk of records based on the search request. If the endPosition is the entire results of the search, this is null. 

        :param next_uri: The next_uri of this FolderItemResponse.
        :type: str
        """

        self._next_uri = next_uri

    @property
    def previous_uri(self):
        """
        Gets the previous_uri of this FolderItemResponse.
        The postal code for the billing address.

        :return: The previous_uri of this FolderItemResponse.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri):
        """
        Sets the previous_uri of this FolderItemResponse.
        The postal code for the billing address.

        :param previous_uri: The previous_uri of this FolderItemResponse.
        :type: str
        """

        self._previous_uri = previous_uri

    @property
    def result_set_size(self):
        """
        Gets the result_set_size of this FolderItemResponse.
        The number of results returned in this response. 

        :return: The result_set_size of this FolderItemResponse.
        :rtype: str
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """
        Sets the result_set_size of this FolderItemResponse.
        The number of results returned in this response. 

        :param result_set_size: The result_set_size of this FolderItemResponse.
        :type: str
        """

        self._result_set_size = result_set_size

    @property
    def start_position(self):
        """
        Gets the start_position of this FolderItemResponse.
        Starting position of the current result set.

        :return: The start_position of this FolderItemResponse.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this FolderItemResponse.
        Starting position of the current result set.

        :param start_position: The start_position of this FolderItemResponse.
        :type: str
        """

        self._start_position = start_position

    @property
    def total_rows(self):
        """
        Gets the total_rows of this FolderItemResponse.
        

        :return: The total_rows of this FolderItemResponse.
        :rtype: str
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """
        Sets the total_rows of this FolderItemResponse.
        

        :param total_rows: The total_rows of this FolderItemResponse.
        :type: str
        """

        self._total_rows = total_rows

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
