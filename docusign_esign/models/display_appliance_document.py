# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DisplayApplianceDocument(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attachment_date=None, attachment_description=None, copy_pdf_id=None, document_id=None, document_type=None, envelope_id=None, external_document_id=None, latest_pdf_id=None, name=None, original_pdf_id=None, pages=None, row_state=None, sequence=None, status=None):
        """
        DisplayApplianceDocument - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attachment_date': 'str',
            'attachment_description': 'str',
            'copy_pdf_id': 'str',
            'document_id': 'str',
            'document_type': 'str',
            'envelope_id': 'str',
            'external_document_id': 'str',
            'latest_pdf_id': 'str',
            'name': 'str',
            'original_pdf_id': 'str',
            'pages': 'str',
            'row_state': 'str',
            'sequence': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'attachment_date': 'attachmentDate',
            'attachment_description': 'attachmentDescription',
            'copy_pdf_id': 'copyPDFId',
            'document_id': 'documentId',
            'document_type': 'documentType',
            'envelope_id': 'envelopeId',
            'external_document_id': 'externalDocumentId',
            'latest_pdf_id': 'latestPDFId',
            'name': 'name',
            'original_pdf_id': 'originalPDFId',
            'pages': 'pages',
            'row_state': 'rowState',
            'sequence': 'sequence',
            'status': 'status'
        }

        self._attachment_date = attachment_date
        self._attachment_description = attachment_description
        self._copy_pdf_id = copy_pdf_id
        self._document_id = document_id
        self._document_type = document_type
        self._envelope_id = envelope_id
        self._external_document_id = external_document_id
        self._latest_pdf_id = latest_pdf_id
        self._name = name
        self._original_pdf_id = original_pdf_id
        self._pages = pages
        self._row_state = row_state
        self._sequence = sequence
        self._status = status

    @property
    def attachment_date(self):
        """
        Gets the attachment_date of this DisplayApplianceDocument.
        

        :return: The attachment_date of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._attachment_date

    @attachment_date.setter
    def attachment_date(self, attachment_date):
        """
        Sets the attachment_date of this DisplayApplianceDocument.
        

        :param attachment_date: The attachment_date of this DisplayApplianceDocument.
        :type: str
        """

        self._attachment_date = attachment_date

    @property
    def attachment_description(self):
        """
        Gets the attachment_description of this DisplayApplianceDocument.
        

        :return: The attachment_description of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._attachment_description

    @attachment_description.setter
    def attachment_description(self, attachment_description):
        """
        Sets the attachment_description of this DisplayApplianceDocument.
        

        :param attachment_description: The attachment_description of this DisplayApplianceDocument.
        :type: str
        """

        self._attachment_description = attachment_description

    @property
    def copy_pdf_id(self):
        """
        Gets the copy_pdf_id of this DisplayApplianceDocument.
        

        :return: The copy_pdf_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._copy_pdf_id

    @copy_pdf_id.setter
    def copy_pdf_id(self, copy_pdf_id):
        """
        Sets the copy_pdf_id of this DisplayApplianceDocument.
        

        :param copy_pdf_id: The copy_pdf_id of this DisplayApplianceDocument.
        :type: str
        """

        self._copy_pdf_id = copy_pdf_id

    @property
    def document_id(self):
        """
        Gets the document_id of this DisplayApplianceDocument.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :return: The document_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """
        Sets the document_id of this DisplayApplianceDocument.
        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.

        :param document_id: The document_id of this DisplayApplianceDocument.
        :type: str
        """

        self._document_id = document_id

    @property
    def document_type(self):
        """
        Gets the document_type of this DisplayApplianceDocument.
        

        :return: The document_type of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this DisplayApplianceDocument.
        

        :param document_type: The document_type of this DisplayApplianceDocument.
        :type: str
        """

        self._document_type = document_type

    @property
    def envelope_id(self):
        """
        Gets the envelope_id of this DisplayApplianceDocument.
        The envelope ID of the envelope status that failed to post.

        :return: The envelope_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """
        Sets the envelope_id of this DisplayApplianceDocument.
        The envelope ID of the envelope status that failed to post.

        :param envelope_id: The envelope_id of this DisplayApplianceDocument.
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def external_document_id(self):
        """
        Gets the external_document_id of this DisplayApplianceDocument.
        

        :return: The external_document_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._external_document_id

    @external_document_id.setter
    def external_document_id(self, external_document_id):
        """
        Sets the external_document_id of this DisplayApplianceDocument.
        

        :param external_document_id: The external_document_id of this DisplayApplianceDocument.
        :type: str
        """

        self._external_document_id = external_document_id

    @property
    def latest_pdf_id(self):
        """
        Gets the latest_pdf_id of this DisplayApplianceDocument.
        

        :return: The latest_pdf_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._latest_pdf_id

    @latest_pdf_id.setter
    def latest_pdf_id(self, latest_pdf_id):
        """
        Sets the latest_pdf_id of this DisplayApplianceDocument.
        

        :param latest_pdf_id: The latest_pdf_id of this DisplayApplianceDocument.
        :type: str
        """

        self._latest_pdf_id = latest_pdf_id

    @property
    def name(self):
        """
        Gets the name of this DisplayApplianceDocument.
        

        :return: The name of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DisplayApplianceDocument.
        

        :param name: The name of this DisplayApplianceDocument.
        :type: str
        """

        self._name = name

    @property
    def original_pdf_id(self):
        """
        Gets the original_pdf_id of this DisplayApplianceDocument.
        

        :return: The original_pdf_id of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._original_pdf_id

    @original_pdf_id.setter
    def original_pdf_id(self, original_pdf_id):
        """
        Sets the original_pdf_id of this DisplayApplianceDocument.
        

        :param original_pdf_id: The original_pdf_id of this DisplayApplianceDocument.
        :type: str
        """

        self._original_pdf_id = original_pdf_id

    @property
    def pages(self):
        """
        Gets the pages of this DisplayApplianceDocument.
        

        :return: The pages of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this DisplayApplianceDocument.
        

        :param pages: The pages of this DisplayApplianceDocument.
        :type: str
        """

        self._pages = pages

    @property
    def row_state(self):
        """
        Gets the row_state of this DisplayApplianceDocument.
        

        :return: The row_state of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._row_state

    @row_state.setter
    def row_state(self, row_state):
        """
        Sets the row_state of this DisplayApplianceDocument.
        

        :param row_state: The row_state of this DisplayApplianceDocument.
        :type: str
        """

        self._row_state = row_state

    @property
    def sequence(self):
        """
        Gets the sequence of this DisplayApplianceDocument.
        

        :return: The sequence of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this DisplayApplianceDocument.
        

        :param sequence: The sequence of this DisplayApplianceDocument.
        :type: str
        """

        self._sequence = sequence

    @property
    def status(self):
        """
        Gets the status of this DisplayApplianceDocument.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this DisplayApplianceDocument.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DisplayApplianceDocument.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this DisplayApplianceDocument.
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
