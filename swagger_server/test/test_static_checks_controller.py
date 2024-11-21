# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.run_static_checks_body import RunStaticChecksBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStaticChecksController(BaseTestCase):
    """StaticChecksController integration test stubs"""

    def test_run_static_checks(self):
        """Test case for run_static_checks

        Run static checks
        """
        body = RunStaticChecksBody()
        response = self.client.open(
            '/runStaticChecks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
