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


class V1beta1DaemonSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'ApisExtensionsV1beta1',
            'type': 'update',
            'method': 'replace_namespaced_daemonset',
            'namespaced': True
        },
        {
            'class': 'ApisExtensionsV1beta1',
            'type': 'delete',
            'method': 'delete_namespaced_daemonset',
            'namespaced': True
        },
        {
            'class': 'ApisExtensionsV1beta1',
            'type': 'read',
            'method': 'get_namespaced_daemonset',
            'namespaced': True
        },
        {
            'class': 'ApisExtensionsV1beta1',
            'type': 'create',
            'method': 'create_daemonset',
            'namespaced': False
        },
        {
            'class': 'ApisExtensionsV1beta1',
            'type': 'create',
            'method': 'create_namespaced_daemonset',
            'namespaced': True
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'spec': 'V1beta1DaemonSetSpec',
        'status': 'V1beta1DaemonSetStatus'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        """
        V1beta1DaemonSet - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._spec = spec
        self._status = status

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1DaemonSet.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1DaemonSet.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1DaemonSet.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1DaemonSet.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1DaemonSet.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1DaemonSet.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1DaemonSet.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1DaemonSet.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta1DaemonSet.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1beta1DaemonSet.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta1DaemonSet.
        Standard object's metadata. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1beta1DaemonSet.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """
        Gets the spec of this V1beta1DaemonSet.
        Spec defines the desired behavior of this daemon set. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status

        :return: The spec of this V1beta1DaemonSet.
        :rtype: V1beta1DaemonSetSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec of this V1beta1DaemonSet.
        Spec defines the desired behavior of this daemon set. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status

        :param spec: The spec of this V1beta1DaemonSet.
        :type: V1beta1DaemonSetSpec
        """

        self._spec = spec

    @property
    def status(self):
        """
        Gets the status of this V1beta1DaemonSet.
        Status is the current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status

        :return: The status of this V1beta1DaemonSet.
        :rtype: V1beta1DaemonSetStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1beta1DaemonSet.
        Status is the current status of this daemon set. This data may be out of date by some window of time. Populated by the system. Read-only. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#spec-and-status

        :param status: The status of this V1beta1DaemonSet.
        :type: V1beta1DaemonSetStatus
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1beta1DaemonSet.swagger_types):
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
