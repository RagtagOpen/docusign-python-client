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


class DateSigned(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, anchor_case_sensitive=None, anchor_horizontal_alignment=None, anchor_ignore_if_not_present=None, anchor_match_whole_word=None, anchor_string=None, anchor_units=None, anchor_x_offset=None, anchor_y_offset=None, bold=None, conditional_parent_label=None, conditional_parent_value=None, custom_tab_id=None, document_id=None, error_details=None, font=None, font_color=None, font_size=None, italic=None, merge_field=None, name=None, page_number=None, recipient_id=None, status=None, tab_group_labels=None, tab_id=None, tab_label=None, tab_order=None, template_locked=None, template_required=None, tooltip=None, underline=None, value=None, x_position=None, y_position=None):
        """
        DateSigned - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'anchor_case_sensitive': 'str',
            'anchor_horizontal_alignment': 'str',
            'anchor_ignore_if_not_present': 'str',
            'anchor_match_whole_word': 'str',
            'anchor_string': 'str',
            'anchor_units': 'str',
            'anchor_x_offset': 'str',
            'anchor_y_offset': 'str',
            'bold': 'str',
            'conditional_parent_label': 'str',
            'conditional_parent_value': 'str',
            'custom_tab_id': 'str',
            'document_id': 'str',
            'error_details': 'ErrorDetails',
            'font': 'str',
            'font_color': 'str',
            'font_size': 'str',
            'italic': 'str',
            'merge_field': 'MergeField',
            'name': 'str',
            'page_number': 'str',
            'recipient_id': 'str',
            'status': 'str',
            'tab_group_labels': 'list[str]',
            'tab_id': 'str',
            'tab_label': 'str',
            'tab_order': 'str',
            'template_locked': 'str',
            'template_required': 'str',
            'tooltip': 'str',
            'underline': 'str',
            'value': 'str',
            'x_position': 'str',
            'y_position': 'str'
        }

        self.attribute_map = {
            'anchor_case_sensitive': 'anchorCaseSensitive',
            'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
            'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
            'anchor_match_whole_word': 'anchorMatchWholeWord',
            'anchor_string': 'anchorString',
            'anchor_units': 'anchorUnits',
            'anchor_x_offset': 'anchorXOffset',
            'anchor_y_offset': 'anchorYOffset',
            'bold': 'bold',
            'conditional_parent_label': 'conditionalParentLabel',
            'conditional_parent_value': 'conditionalParentValue',
            'custom_tab_id': 'customTabId',
            'document_id': 'documentId',
            'error_details': 'errorDetails',
            'font': 'font',
            'font_color': 'fontColor',
            'font_size': 'fontSize',
            'italic': 'italic',
            'merge_field': 'mergeField',
            'name': 'name',
            'page_number': 'pageNumber',
            'recipient_id': 'recipientId',
            'status': 'status',
            'tab_group_labels': 'tabGroupLabels',
            'tab_id': 'tabId',
            'tab_label': 'tabLabel',
            'tab_order': 'tabOrder',
            'template_locked': 'templateLocked',
            'template_required': 'templateRequired',
            'tooltip': 'tooltip',
            'underline': 'underline',
            'value': 'value',
            'x_position': 'xPosition',
            'y_position': 'yPosition'
        }

        self._anchor_case_sensitive = anchor_case_sensitive
        self._anchor_horizontal_alignment = anchor_horizontal_alignment
        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present
        self._anchor_match_whole_word = anchor_match_whole_word
        self._anchor_string = anchor_string
        self._anchor_units = anchor_units
        self._anchor_x_offset = anchor_x_offset
        self._anchor_y_offset = anchor_y_offset
        self._bold = bold
        self._conditional_parent_label = conditional_parent_label
        self._conditional_parent_value = conditional_parent_value
        self._custom_tab_id = custom_tab_id
        self._document_id = document_id
        self._error_details = error_details
        self._font = font
        self._font_color = font_color
        self._font_size = font_size
        self._italic = italic
        self._merge_field = merge_field
        self._name = name
        self._page_number = page_number
        self._recipient_id = recipient_id
        self._status = status
        self._tab_group_labels = tab_group_labels
        self._tab_id = tab_id
        self._tab_label = tab_label
        self._tab_order = tab_order
        self._template_locked = template_locked
        self._template_required = template_required
        self._tooltip = tooltip
        self._underline = underline
        self._value = value
        self._x_position = x_position
        self._y_position = y_position

    @property
    def anchor_case_sensitive(self):
        """
        Gets the anchor_case_sensitive of this DateSigned.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :return: The anchor_case_sensitive of this DateSigned.
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """
        Sets the anchor_case_sensitive of this DateSigned.
        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.

        :param anchor_case_sensitive: The anchor_case_sensitive of this DateSigned.
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """
        Gets the anchor_horizontal_alignment of this DateSigned.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :return: The anchor_horizontal_alignment of this DateSigned.
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """
        Sets the anchor_horizontal_alignment of this DateSigned.
        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this DateSigned.
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """
        Gets the anchor_ignore_if_not_present of this DateSigned.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :return: The anchor_ignore_if_not_present of this DateSigned.
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """
        Sets the anchor_ignore_if_not_present of this DateSigned.
        When set to **true**, this tab is ignored if anchorString is not found in the document.

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this DateSigned.
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """
        Gets the anchor_match_whole_word of this DateSigned.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :return: The anchor_match_whole_word of this DateSigned.
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """
        Sets the anchor_match_whole_word of this DateSigned.
        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.

        :param anchor_match_whole_word: The anchor_match_whole_word of this DateSigned.
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_string(self):
        """
        Gets the anchor_string of this DateSigned.
        Anchor text information for a radio button.

        :return: The anchor_string of this DateSigned.
        :rtype: str
        """
        return self._anchor_string

    @anchor_string.setter
    def anchor_string(self, anchor_string):
        """
        Sets the anchor_string of this DateSigned.
        Anchor text information for a radio button.

        :param anchor_string: The anchor_string of this DateSigned.
        :type: str
        """

        self._anchor_string = anchor_string

    @property
    def anchor_units(self):
        """
        Gets the anchor_units of this DateSigned.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :return: The anchor_units of this DateSigned.
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """
        Sets the anchor_units of this DateSigned.
        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.

        :param anchor_units: The anchor_units of this DateSigned.
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """
        Gets the anchor_x_offset of this DateSigned.
        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.

        :return: The anchor_x_offset of this DateSigned.
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """
        Sets the anchor_x_offset of this DateSigned.
        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.

        :param anchor_x_offset: The anchor_x_offset of this DateSigned.
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """
        Gets the anchor_y_offset of this DateSigned.
        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.

        :return: The anchor_y_offset of this DateSigned.
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """
        Sets the anchor_y_offset of this DateSigned.
        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.

        :param anchor_y_offset: The anchor_y_offset of this DateSigned.
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def bold(self):
        """
        Gets the bold of this DateSigned.
        When set to **true**, the information in the tab is bold.

        :return: The bold of this DateSigned.
        :rtype: str
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """
        Sets the bold of this DateSigned.
        When set to **true**, the information in the tab is bold.

        :param bold: The bold of this DateSigned.
        :type: str
        """

        self._bold = bold

    @property
    def conditional_parent_label(self):
        """
        Gets the conditional_parent_label of this DateSigned.
        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.

        :return: The conditional_parent_label of this DateSigned.
        :rtype: str
        """
        return self._conditional_parent_label

    @conditional_parent_label.setter
    def conditional_parent_label(self, conditional_parent_label):
        """
        Sets the conditional_parent_label of this DateSigned.
        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.

        :param conditional_parent_label: The conditional_parent_label of this DateSigned.
        :type: str
        """

        self._conditional_parent_label = conditional_parent_label

    @property
    def conditional_parent_value(self):
        """
        Gets the conditional_parent_value of this DateSigned.
        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active. 

        :return: The conditional_parent_value of this DateSigned.
        :rtype: str
        """
        return self._conditional_parent_value

    @conditional_parent_value.setter
    def conditional_parent_value(self, conditional_parent_value):
        """
        Sets the conditional_parent_value of this DateSigned.
        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active. 

        :param conditional_parent_value: The conditional_parent_value of this DateSigned.
        :type: str
        """

        self._conditional_parent_value = conditional_parent_value

    @property
    def custom_tab_id(self):
        """
        Gets the custom_tab_id of this DateSigned.
        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.

        :return: The custom_tab_id of this DateSigned.
        :rtype: str
        """
        return self._custom_tab_id

    @custom_tab_id.setter
    def custom_tab_id(self, custom_tab_id):
        """
        Sets the custom_tab_id of this DateSigned.
        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.

        :param custom_tab_id: The custom_tab_id of this DateSigned.
        :type: str
        """

        self._custom_tab_id = custom_tab_id

    @property
    def document_id(self):
        """
        Gets the document_id of this DateSigned.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :return: The document_id of this DateSigned.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this DateSigned.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :param document_id: The document_id of this DateSigned.
        :type: str
        """

        self._document_id = document_id

    @property
    def error_details(self):
        """
        Gets the error_details of this DateSigned.

        :return: The error_details of this DateSigned.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this DateSigned.

        :param error_details: The error_details of this DateSigned.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def font(self):
        """
        Gets the font of this DateSigned.
        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.

        :return: The font of this DateSigned.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this DateSigned.
        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.

        :param font: The font of this DateSigned.
        :type: str
        """

        self._font = font

    @property
    def font_color(self):
        """
        Gets the font_color of this DateSigned.
        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.

        :return: The font_color of this DateSigned.
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """
        Sets the font_color of this DateSigned.
        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.

        :param font_color: The font_color of this DateSigned.
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """
        Gets the font_size of this DateSigned.
        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.

        :return: The font_size of this DateSigned.
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size of this DateSigned.
        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.

        :param font_size: The font_size of this DateSigned.
        :type: str
        """

        self._font_size = font_size

    @property
    def italic(self):
        """
        Gets the italic of this DateSigned.
        When set to **true**, the information in the tab is italic.

        :return: The italic of this DateSigned.
        :rtype: str
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """
        Sets the italic of this DateSigned.
        When set to **true**, the information in the tab is italic.

        :param italic: The italic of this DateSigned.
        :type: str
        """

        self._italic = italic

    @property
    def merge_field(self):
        """
        Gets the merge_field of this DateSigned.

        :return: The merge_field of this DateSigned.
        :rtype: MergeField
        """
        return self._merge_field

    @merge_field.setter
    def merge_field(self, merge_field):
        """
        Sets the merge_field of this DateSigned.

        :param merge_field: The merge_field of this DateSigned.
        :type: MergeField
        """

        self._merge_field = merge_field

    @property
    def name(self):
        """
        Gets the name of this DateSigned.
        

        :return: The name of this DateSigned.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DateSigned.
        

        :param name: The name of this DateSigned.
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """
        Gets the page_number of this DateSigned.
        Specifies the page number on which the tab is located.

        :return: The page_number of this DateSigned.
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this DateSigned.
        Specifies the page number on which the tab is located.

        :param page_number: The page_number of this DateSigned.
        :type: str
        """

        self._page_number = page_number

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this DateSigned.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this DateSigned.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this DateSigned.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this DateSigned.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def status(self):
        """
        Gets the status of this DateSigned.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this DateSigned.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DateSigned.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this DateSigned.
        :type: str
        """

        self._status = status

    @property
    def tab_group_labels(self):
        """
        Gets the tab_group_labels of this DateSigned.
        

        :return: The tab_group_labels of this DateSigned.
        :rtype: list[str]
        """
        return self._tab_group_labels

    @tab_group_labels.setter
    def tab_group_labels(self, tab_group_labels):
        """
        Sets the tab_group_labels of this DateSigned.
        

        :param tab_group_labels: The tab_group_labels of this DateSigned.
        :type: list[str]
        """

        self._tab_group_labels = tab_group_labels

    @property
    def tab_id(self):
        """
        Gets the tab_id of this DateSigned.
        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].     

        :return: The tab_id of this DateSigned.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """
        Sets the tab_id of this DateSigned.
        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].     

        :param tab_id: The tab_id of this DateSigned.
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_label(self):
        """
        Gets the tab_label of this DateSigned.
        The label string associated with the tab.

        :return: The tab_label of this DateSigned.
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """
        Sets the tab_label of this DateSigned.
        The label string associated with the tab.

        :param tab_label: The tab_label of this DateSigned.
        :type: str
        """

        self._tab_label = tab_label

    @property
    def tab_order(self):
        """
        Gets the tab_order of this DateSigned.
        

        :return: The tab_order of this DateSigned.
        :rtype: str
        """
        return self._tab_order

    @tab_order.setter
    def tab_order(self, tab_order):
        """
        Sets the tab_order of this DateSigned.
        

        :param tab_order: The tab_order of this DateSigned.
        :type: str
        """

        self._tab_order = tab_order

    @property
    def template_locked(self):
        """
        Gets the template_locked of this DateSigned.
        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients. 

        :return: The template_locked of this DateSigned.
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """
        Sets the template_locked of this DateSigned.
        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients. 

        :param template_locked: The template_locked of this DateSigned.
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """
        Gets the template_required of this DateSigned.
        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.

        :return: The template_required of this DateSigned.
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """
        Sets the template_required of this DateSigned.
        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.

        :param template_required: The template_required of this DateSigned.
        :type: str
        """

        self._template_required = template_required

    @property
    def tooltip(self):
        """
        Gets the tooltip of this DateSigned.
        

        :return: The tooltip of this DateSigned.
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """
        Sets the tooltip of this DateSigned.
        

        :param tooltip: The tooltip of this DateSigned.
        :type: str
        """

        self._tooltip = tooltip

    @property
    def underline(self):
        """
        Gets the underline of this DateSigned.
        When set to **true**, the information in the tab is underlined.

        :return: The underline of this DateSigned.
        :rtype: str
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """
        Sets the underline of this DateSigned.
        When set to **true**, the information in the tab is underlined.

        :param underline: The underline of this DateSigned.
        :type: str
        """

        self._underline = underline

    @property
    def value(self):
        """
        Gets the value of this DateSigned.
        Specifies the value of the tab. 

        :return: The value of this DateSigned.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DateSigned.
        Specifies the value of the tab. 

        :param value: The value of this DateSigned.
        :type: str
        """

        self._value = value

    @property
    def x_position(self):
        """
        Gets the x_position of this DateSigned.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The x_position of this DateSigned.
        :rtype: str
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """
        Sets the x_position of this DateSigned.
        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param x_position: The x_position of this DateSigned.
        :type: str
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """
        Gets the y_position of this DateSigned.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :return: The y_position of this DateSigned.
        :rtype: str
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """
        Sets the y_position of this DateSigned.
        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.

        :param y_position: The y_position of this DateSigned.
        :type: str
        """

        self._y_position = y_position

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
