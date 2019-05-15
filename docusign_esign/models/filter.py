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


class Filter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action_required=None, expires=None, folder_ids=None, from_date_time=None, is_template=None, order=None, order_by=None, search_target=None, search_text=None, status=None, to_date_time=None):
        """
        Filter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_required': 'str',
            'expires': 'str',
            'folder_ids': 'str',
            'from_date_time': 'str',
            'is_template': 'str',
            'order': 'str',
            'order_by': 'str',
            'search_target': 'str',
            'search_text': 'str',
            'status': 'str',
            'to_date_time': 'str'
        }

        self.attribute_map = {
            'action_required': 'actionRequired',
            'expires': 'expires',
            'folder_ids': 'folderIds',
            'from_date_time': 'fromDateTime',
            'is_template': 'isTemplate',
            'order': 'order',
            'order_by': 'orderBy',
            'search_target': 'searchTarget',
            'search_text': 'searchText',
            'status': 'status',
            'to_date_time': 'toDateTime'
        }

        self._action_required = action_required
        self._expires = expires
        self._folder_ids = folder_ids
        self._from_date_time = from_date_time
        self._is_template = is_template
        self._order = order
        self._order_by = order_by
        self._search_target = search_target
        self._search_text = search_text
        self._status = status
        self._to_date_time = to_date_time

    @property
    def action_required(self):
        """
        Gets the action_required of this Filter.
        Access token information.

        :return: The action_required of this Filter.
        :rtype: str
        """
        return self._action_required

    @action_required.setter
    def action_required(self, action_required):
        """
        Sets the action_required of this Filter.
        Access token information.

        :param action_required: The action_required of this Filter.
        :type: str
        """

        self._action_required = action_required

    @property
    def expires(self):
        """
        Gets the expires of this Filter.
        

        :return: The expires of this Filter.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this Filter.
        

        :param expires: The expires of this Filter.
        :type: str
        """

        self._expires = expires

    @property
    def folder_ids(self):
        """
        Gets the folder_ids of this Filter.
        

        :return: The folder_ids of this Filter.
        :rtype: str
        """
        return self._folder_ids

    @folder_ids.setter
    def folder_ids(self, folder_ids):
        """
        Sets the folder_ids of this Filter.
        

        :param folder_ids: The folder_ids of this Filter.
        :type: str
        """

        self._folder_ids = folder_ids

    @property
    def from_date_time(self):
        """
        Gets the from_date_time of this Filter.
        

        :return: The from_date_time of this Filter.
        :rtype: str
        """
        return self._from_date_time

    @from_date_time.setter
    def from_date_time(self, from_date_time):
        """
        Sets the from_date_time of this Filter.
        

        :param from_date_time: The from_date_time of this Filter.
        :type: str
        """

        self._from_date_time = from_date_time

    @property
    def is_template(self):
        """
        Gets the is_template of this Filter.
        

        :return: The is_template of this Filter.
        :rtype: str
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        """
        Sets the is_template of this Filter.
        

        :param is_template: The is_template of this Filter.
        :type: str
        """

        self._is_template = is_template

    @property
    def order(self):
        """
        Gets the order of this Filter.
        

        :return: The order of this Filter.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this Filter.
        

        :param order: The order of this Filter.
        :type: str
        """

        self._order = order

    @property
    def order_by(self):
        """
        Gets the order_by of this Filter.
        

        :return: The order_by of this Filter.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """
        Sets the order_by of this Filter.
        

        :param order_by: The order_by of this Filter.
        :type: str
        """

        self._order_by = order_by

    @property
    def search_target(self):
        """
        Gets the search_target of this Filter.
        

        :return: The search_target of this Filter.
        :rtype: str
        """
        return self._search_target

    @search_target.setter
    def search_target(self, search_target):
        """
        Sets the search_target of this Filter.
        

        :param search_target: The search_target of this Filter.
        :type: str
        """

        self._search_target = search_target

    @property
    def search_text(self):
        """
        Gets the search_text of this Filter.
        

        :return: The search_text of this Filter.
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """
        Sets the search_text of this Filter.
        

        :param search_text: The search_text of this Filter.
        :type: str
        """

        self._search_text = search_text

    @property
    def status(self):
        """
        Gets the status of this Filter.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this Filter.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Filter.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this Filter.
        :type: str
        """

        self._status = status

    @property
    def to_date_time(self):
        """
        Gets the to_date_time of this Filter.
        Must be set to \"bearer\".

        :return: The to_date_time of this Filter.
        :rtype: str
        """
        return self._to_date_time

    @to_date_time.setter
    def to_date_time(self, to_date_time):
        """
        Sets the to_date_time of this Filter.
        Must be set to \"bearer\".

        :param to_date_time: The to_date_time of this Filter.
        :type: str
        """

        self._to_date_time = to_date_time

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
