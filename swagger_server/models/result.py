# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_sequence_location import ResultSequenceLocation  # noqa: F401,E501
from swagger_server import util


class Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rule_id: str=None, level: str=None, sequence_location: ResultSequenceLocation=None):  # noqa: E501
        """Result - a model defined in Swagger

        :param rule_id: The rule_id of this Result.  # noqa: E501
        :type rule_id: str
        :param level: The level of this Result.  # noqa: E501
        :type level: str
        :param sequence_location: The sequence_location of this Result.  # noqa: E501
        :type sequence_location: ResultSequenceLocation
        """
        self.swagger_types = {
            'rule_id': str,
            'level': str,
            'sequence_location': ResultSequenceLocation
        }

        self.attribute_map = {
            'rule_id': 'rule_id',
            'level': 'level',
            'sequence_location': 'sequence_location'
        }
        self._rule_id = rule_id
        self._level = level
        self._sequence_location = sequence_location

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rule_id(self) -> str:
        """Gets the rule_id of this Result.


        :return: The rule_id of this Result.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id: str):
        """Sets the rule_id of this Result.


        :param rule_id: The rule_id of this Result.
        :type rule_id: str
        """

        self._rule_id = rule_id

    @property
    def level(self) -> str:
        """Gets the level of this Result.


        :return: The level of this Result.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str):
        """Sets the level of this Result.


        :param level: The level of this Result.
        :type level: str
        """
        allowed_values = ["PASS", "WARNING", "VIOLATED", "ERROR", "INFO"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def sequence_location(self) -> ResultSequenceLocation:
        """Gets the sequence_location of this Result.


        :return: The sequence_location of this Result.
        :rtype: ResultSequenceLocation
        """
        return self._sequence_location

    @sequence_location.setter
    def sequence_location(self, sequence_location: ResultSequenceLocation):
        """Sets the sequence_location of this Result.


        :param sequence_location: The sequence_location of this Result.
        :type sequence_location: ResultSequenceLocation
        """

        self._sequence_location = sequence_location
