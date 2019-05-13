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


class AccountPasswordQuestionsRequired(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, maximum_questions=None, minimum_questions=None):
        """
        AccountPasswordQuestionsRequired - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maximum_questions': 'str',
            'minimum_questions': 'str'
        }

        self.attribute_map = {
            'maximum_questions': 'maximumQuestions',
            'minimum_questions': 'minimumQuestions'
        }

        self._maximum_questions = maximum_questions
        self._minimum_questions = minimum_questions

    @property
    def maximum_questions(self):
        """
        Gets the maximum_questions of this AccountPasswordQuestionsRequired.
        

        :return: The maximum_questions of this AccountPasswordQuestionsRequired.
        :rtype: str
        """
        return self._maximum_questions

    @maximum_questions.setter
    def maximum_questions(self, maximum_questions):
        """
        Sets the maximum_questions of this AccountPasswordQuestionsRequired.
        

        :param maximum_questions: The maximum_questions of this AccountPasswordQuestionsRequired.
        :type: str
        """

        self._maximum_questions = maximum_questions

    @property
    def minimum_questions(self):
        """
        Gets the minimum_questions of this AccountPasswordQuestionsRequired.
        

        :return: The minimum_questions of this AccountPasswordQuestionsRequired.
        :rtype: str
        """
        return self._minimum_questions

    @minimum_questions.setter
    def minimum_questions(self, minimum_questions):
        """
        Sets the minimum_questions of this AccountPasswordQuestionsRequired.
        

        :param minimum_questions: The minimum_questions of this AccountPasswordQuestionsRequired.
        :type: str
        """

        self._minimum_questions = minimum_questions

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
