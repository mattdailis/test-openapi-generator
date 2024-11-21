import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.run_static_checks_body import RunStaticChecksBody  # noqa: E501
from swagger_server import util


def run_static_checks(body):  # noqa: E501
    """Run static checks

    Given a sequence&#x27;s name and contents, return a list of check results # noqa: E501

    :param body: Run static checks
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = RunStaticChecksBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
