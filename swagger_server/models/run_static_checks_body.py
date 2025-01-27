# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RunStaticChecksBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sequence_name: str=None, sequence_contents: str=None):  # noqa: E501
        """RunStaticChecksBody - a model defined in Swagger

        :param sequence_name: The sequence_name of this RunStaticChecksBody.  # noqa: E501
        :type sequence_name: str
        :param sequence_contents: The sequence_contents of this RunStaticChecksBody.  # noqa: E501
        :type sequence_contents: str
        """
        self.swagger_types = {
            'sequence_name': str,
            'sequence_contents': str
        }

        self.attribute_map = {
            'sequence_name': 'sequence_name',
            'sequence_contents': 'sequence_contents'
        }
        self._sequence_name = sequence_name
        self._sequence_contents = sequence_contents

    @classmethod
    def from_dict(cls, dikt) -> 'RunStaticChecksBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The runStaticChecks_body of this RunStaticChecksBody.  # noqa: E501
        :rtype: RunStaticChecksBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sequence_name(self) -> str:
        """Gets the sequence_name of this RunStaticChecksBody.


        :return: The sequence_name of this RunStaticChecksBody.
        :rtype: str
        """
        return self._sequence_name

    @sequence_name.setter
    def sequence_name(self, sequence_name: str):
        """Sets the sequence_name of this RunStaticChecksBody.


        :param sequence_name: The sequence_name of this RunStaticChecksBody.
        :type sequence_name: str
        """

        self._sequence_name = sequence_name

    @property
    def sequence_contents(self) -> str:
        """Gets the sequence_contents of this RunStaticChecksBody.


        :return: The sequence_contents of this RunStaticChecksBody.
        :rtype: str
        """
        return self._sequence_contents

    @sequence_contents.setter
    def sequence_contents(self, sequence_contents: str):
        """Sets the sequence_contents of this RunStaticChecksBody.


        :param sequence_contents: The sequence_contents of this RunStaticChecksBody.
        :type sequence_contents: str
        """

        self._sequence_contents = sequence_contents
