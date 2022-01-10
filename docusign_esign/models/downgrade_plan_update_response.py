# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class DowngradePlanUpdateResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_payment_method': 'str',
        'discount_applied': 'str',
        'downgrade_effective_date': 'str',
        'downgrade_payment_cycle': 'str',
        'downgrade_plan_id': 'str',
        'downgrade_plan_name': 'str',
        'downgrade_request_status': 'str',
        'message': 'str',
        'product_id': 'str',
        'promo_code': 'str',
        'sale_discount': 'str',
        'sale_discount_periods': 'str',
        'sale_discount_type': 'str'
    }

    attribute_map = {
        'account_payment_method': 'accountPaymentMethod',
        'discount_applied': 'discountApplied',
        'downgrade_effective_date': 'downgradeEffectiveDate',
        'downgrade_payment_cycle': 'downgradePaymentCycle',
        'downgrade_plan_id': 'downgradePlanId',
        'downgrade_plan_name': 'downgradePlanName',
        'downgrade_request_status': 'downgradeRequestStatus',
        'message': 'message',
        'product_id': 'productId',
        'promo_code': 'promoCode',
        'sale_discount': 'saleDiscount',
        'sale_discount_periods': 'saleDiscountPeriods',
        'sale_discount_type': 'saleDiscountType'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DowngradePlanUpdateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_payment_method = None
        self._discount_applied = None
        self._downgrade_effective_date = None
        self._downgrade_payment_cycle = None
        self._downgrade_plan_id = None
        self._downgrade_plan_name = None
        self._downgrade_request_status = None
        self._message = None
        self._product_id = None
        self._promo_code = None
        self._sale_discount = None
        self._sale_discount_periods = None
        self._sale_discount_type = None
        self.discriminator = None

        setattr(self, "_{}".format('account_payment_method'), kwargs.get('account_payment_method', None))
        setattr(self, "_{}".format('discount_applied'), kwargs.get('discount_applied', None))
        setattr(self, "_{}".format('downgrade_effective_date'), kwargs.get('downgrade_effective_date', None))
        setattr(self, "_{}".format('downgrade_payment_cycle'), kwargs.get('downgrade_payment_cycle', None))
        setattr(self, "_{}".format('downgrade_plan_id'), kwargs.get('downgrade_plan_id', None))
        setattr(self, "_{}".format('downgrade_plan_name'), kwargs.get('downgrade_plan_name', None))
        setattr(self, "_{}".format('downgrade_request_status'), kwargs.get('downgrade_request_status', None))
        setattr(self, "_{}".format('message'), kwargs.get('message', None))
        setattr(self, "_{}".format('product_id'), kwargs.get('product_id', None))
        setattr(self, "_{}".format('promo_code'), kwargs.get('promo_code', None))
        setattr(self, "_{}".format('sale_discount'), kwargs.get('sale_discount', None))
        setattr(self, "_{}".format('sale_discount_periods'), kwargs.get('sale_discount_periods', None))
        setattr(self, "_{}".format('sale_discount_type'), kwargs.get('sale_discount_type', None))

    @property
    def account_payment_method(self):
        """Gets the account_payment_method of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The account_payment_method of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_payment_method

    @account_payment_method.setter
    def account_payment_method(self, account_payment_method):
        """Sets the account_payment_method of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param account_payment_method: The account_payment_method of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._account_payment_method = account_payment_method

    @property
    def discount_applied(self):
        """Gets the discount_applied of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The discount_applied of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._discount_applied

    @discount_applied.setter
    def discount_applied(self, discount_applied):
        """Sets the discount_applied of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param discount_applied: The discount_applied of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._discount_applied = discount_applied

    @property
    def downgrade_effective_date(self):
        """Gets the downgrade_effective_date of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The downgrade_effective_date of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_effective_date

    @downgrade_effective_date.setter
    def downgrade_effective_date(self, downgrade_effective_date):
        """Sets the downgrade_effective_date of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param downgrade_effective_date: The downgrade_effective_date of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._downgrade_effective_date = downgrade_effective_date

    @property
    def downgrade_payment_cycle(self):
        """Gets the downgrade_payment_cycle of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The downgrade_payment_cycle of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_payment_cycle

    @downgrade_payment_cycle.setter
    def downgrade_payment_cycle(self, downgrade_payment_cycle):
        """Sets the downgrade_payment_cycle of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param downgrade_payment_cycle: The downgrade_payment_cycle of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._downgrade_payment_cycle = downgrade_payment_cycle

    @property
    def downgrade_plan_id(self):
        """Gets the downgrade_plan_id of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The downgrade_plan_id of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_plan_id

    @downgrade_plan_id.setter
    def downgrade_plan_id(self, downgrade_plan_id):
        """Sets the downgrade_plan_id of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param downgrade_plan_id: The downgrade_plan_id of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._downgrade_plan_id = downgrade_plan_id

    @property
    def downgrade_plan_name(self):
        """Gets the downgrade_plan_name of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The downgrade_plan_name of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_plan_name

    @downgrade_plan_name.setter
    def downgrade_plan_name(self, downgrade_plan_name):
        """Sets the downgrade_plan_name of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param downgrade_plan_name: The downgrade_plan_name of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._downgrade_plan_name = downgrade_plan_name

    @property
    def downgrade_request_status(self):
        """Gets the downgrade_request_status of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The downgrade_request_status of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._downgrade_request_status

    @downgrade_request_status.setter
    def downgrade_request_status(self, downgrade_request_status):
        """Sets the downgrade_request_status of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param downgrade_request_status: The downgrade_request_status of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._downgrade_request_status = downgrade_request_status

    @property
    def message(self):
        """Gets the message of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The message of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param message: The message of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def product_id(self):
        """Gets the product_id of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The product_id of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param product_id: The product_id of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def promo_code(self):
        """Gets the promo_code of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The promo_code of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._promo_code

    @promo_code.setter
    def promo_code(self, promo_code):
        """Sets the promo_code of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param promo_code: The promo_code of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._promo_code = promo_code

    @property
    def sale_discount(self):
        """Gets the sale_discount of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The sale_discount of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount

    @sale_discount.setter
    def sale_discount(self, sale_discount):
        """Sets the sale_discount of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param sale_discount: The sale_discount of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._sale_discount = sale_discount

    @property
    def sale_discount_periods(self):
        """Gets the sale_discount_periods of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_periods of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_periods

    @sale_discount_periods.setter
    def sale_discount_periods(self, sale_discount_periods):
        """Sets the sale_discount_periods of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param sale_discount_periods: The sale_discount_periods of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._sale_discount_periods = sale_discount_periods

    @property
    def sale_discount_type(self):
        """Gets the sale_discount_type of this DowngradePlanUpdateResponse.  # noqa: E501

          # noqa: E501

        :return: The sale_discount_type of this DowngradePlanUpdateResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_discount_type

    @sale_discount_type.setter
    def sale_discount_type(self, sale_discount_type):
        """Sets the sale_discount_type of this DowngradePlanUpdateResponse.

          # noqa: E501

        :param sale_discount_type: The sale_discount_type of this DowngradePlanUpdateResponse.  # noqa: E501
        :type: str
        """

        self._sale_discount_type = sale_discount_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DowngradePlanUpdateResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DowngradePlanUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DowngradePlanUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()