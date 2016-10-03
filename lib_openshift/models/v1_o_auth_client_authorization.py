# coding: utf-8

"""
    

    

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1OAuthClientAuthorization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_oauthclientauthorization',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_oauthclientauthorization',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_oauthclientauthorization',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_oauthclientauthorization',
            'namespaced': False
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'client_name': 'str',
        'user_name': 'str',
        'user_uid': 'str',
        'scopes': 'list[str]'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'client_name': 'clientName',
        'user_name': 'userName',
        'user_uid': 'userUID',
        'scopes': 'scopes'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, client_name=None, user_name=None, user_uid=None, scopes=None):
        """
        V1OAuthClientAuthorization - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._client_name = client_name
        self._user_name = user_name
        self._user_uid = user_uid
        self._scopes = scopes

    @property
    def kind(self):
        """
        Gets the kind of this V1OAuthClientAuthorization.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1OAuthClientAuthorization.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1OAuthClientAuthorization.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1OAuthClientAuthorization.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1OAuthClientAuthorization.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1OAuthClientAuthorization.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1OAuthClientAuthorization.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1OAuthClientAuthorization.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1OAuthClientAuthorization.
        Standard object's metadata.

        :return: The metadata of this V1OAuthClientAuthorization.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1OAuthClientAuthorization.
        Standard object's metadata.

        :param metadata: The metadata of this V1OAuthClientAuthorization.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def client_name(self):
        """
        Gets the client_name of this V1OAuthClientAuthorization.
        ClientName references the client that created this authorization

        :return: The client_name of this V1OAuthClientAuthorization.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """
        Sets the client_name of this V1OAuthClientAuthorization.
        ClientName references the client that created this authorization

        :param client_name: The client_name of this V1OAuthClientAuthorization.
        :type: str
        """

        self._client_name = client_name

    @property
    def user_name(self):
        """
        Gets the user_name of this V1OAuthClientAuthorization.
        UserName is the user name that authorized this client

        :return: The user_name of this V1OAuthClientAuthorization.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this V1OAuthClientAuthorization.
        UserName is the user name that authorized this client

        :param user_name: The user_name of this V1OAuthClientAuthorization.
        :type: str
        """

        self._user_name = user_name

    @property
    def user_uid(self):
        """
        Gets the user_uid of this V1OAuthClientAuthorization.
        UserUID is the unique UID associated with this authorization. UserUID and UserName must both match for this authorization to be valid.

        :return: The user_uid of this V1OAuthClientAuthorization.
        :rtype: str
        """
        return self._user_uid

    @user_uid.setter
    def user_uid(self, user_uid):
        """
        Sets the user_uid of this V1OAuthClientAuthorization.
        UserUID is the unique UID associated with this authorization. UserUID and UserName must both match for this authorization to be valid.

        :param user_uid: The user_uid of this V1OAuthClientAuthorization.
        :type: str
        """

        self._user_uid = user_uid

    @property
    def scopes(self):
        """
        Gets the scopes of this V1OAuthClientAuthorization.
        Scopes is an array of the granted scopes.

        :return: The scopes of this V1OAuthClientAuthorization.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this V1OAuthClientAuthorization.
        Scopes is an array of the granted scopes.

        :param scopes: The scopes of this V1OAuthClientAuthorization.
        :type: list[str]
        """

        self._scopes = scopes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1OAuthClientAuthorization.swagger_types):
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
