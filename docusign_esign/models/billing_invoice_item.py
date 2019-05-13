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


class BillingInvoiceItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, charge_amount=None, charge_name=None, invoice_item_id=None, quantity=None, unit_price=None):
        """
        BillingInvoiceItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'charge_amount': 'str',
            'charge_name': 'str',
            'invoice_item_id': 'str',
            'quantity': 'str',
            'unit_price': 'str'
        }

        self.attribute_map = {
            'charge_amount': 'chargeAmount',
            'charge_name': 'chargeName',
            'invoice_item_id': 'invoiceItemId',
            'quantity': 'quantity',
            'unit_price': 'unitPrice'
        }

        self._charge_amount = charge_amount
        self._charge_name = charge_name
        self._invoice_item_id = invoice_item_id
        self._quantity = quantity
        self._unit_price = unit_price

    @property
    def charge_amount(self):
        """
        Gets the charge_amount of this BillingInvoiceItem.
        Reserved: TBD

        :return: The charge_amount of this BillingInvoiceItem.
        :rtype: str
        """
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, charge_amount):
        """
        Sets the charge_amount of this BillingInvoiceItem.
        Reserved: TBD

        :param charge_amount: The charge_amount of this BillingInvoiceItem.
        :type: str
        """

        self._charge_amount = charge_amount

    @property
    def charge_name(self):
        """
        Gets the charge_name of this BillingInvoiceItem.
        Reserved: TBD

        :return: The charge_name of this BillingInvoiceItem.
        :rtype: str
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """
        Sets the charge_name of this BillingInvoiceItem.
        Reserved: TBD

        :param charge_name: The charge_name of this BillingInvoiceItem.
        :type: str
        """

        self._charge_name = charge_name

    @property
    def invoice_item_id(self):
        """
        Gets the invoice_item_id of this BillingInvoiceItem.
        Reserved: TBD

        :return: The invoice_item_id of this BillingInvoiceItem.
        :rtype: str
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """
        Sets the invoice_item_id of this BillingInvoiceItem.
        Reserved: TBD

        :param invoice_item_id: The invoice_item_id of this BillingInvoiceItem.
        :type: str
        """

        self._invoice_item_id = invoice_item_id

    @property
    def quantity(self):
        """
        Gets the quantity of this BillingInvoiceItem.
        

        :return: The quantity of this BillingInvoiceItem.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this BillingInvoiceItem.
        

        :param quantity: The quantity of this BillingInvoiceItem.
        :type: str
        """

        self._quantity = quantity

    @property
    def unit_price(self):
        """
        Gets the unit_price of this BillingInvoiceItem.
        Reserved: TBD

        :return: The unit_price of this BillingInvoiceItem.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this BillingInvoiceItem.
        Reserved: TBD

        :param unit_price: The unit_price of this BillingInvoiceItem.
        :type: str
        """

        self._unit_price = unit_price

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
