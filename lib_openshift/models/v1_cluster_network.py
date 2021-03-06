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


class V1ClusterNetwork(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_clusternetwork',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_clusternetwork',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_clusternetwork',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_clusternetwork',
            'namespaced': False
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'network': 'str',
        'hostsubnetlength': 'int',
        'service_network': 'str'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'network': 'network',
        'hostsubnetlength': 'hostsubnetlength',
        'service_network': 'serviceNetwork'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, network=None, hostsubnetlength=None, service_network=None):
        """
        V1ClusterNetwork - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._network = network
        self._hostsubnetlength = hostsubnetlength
        self._service_network = service_network

    @property
    def kind(self):
        """
        Gets the kind of this V1ClusterNetwork.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ClusterNetwork.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ClusterNetwork.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ClusterNetwork.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ClusterNetwork.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ClusterNetwork.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ClusterNetwork.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ClusterNetwork.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ClusterNetwork.
        Standard object's metadata.

        :return: The metadata of this V1ClusterNetwork.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ClusterNetwork.
        Standard object's metadata.

        :param metadata: The metadata of this V1ClusterNetwork.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def network(self):
        """
        Gets the network of this V1ClusterNetwork.
        Network is a CIDR string to specify the global overlay network's L3 space

        :return: The network of this V1ClusterNetwork.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this V1ClusterNetwork.
        Network is a CIDR string to specify the global overlay network's L3 space

        :param network: The network of this V1ClusterNetwork.
        :type: str
        """

        self._network = network

    @property
    def hostsubnetlength(self):
        """
        Gets the hostsubnetlength of this V1ClusterNetwork.
        HostSubnetLength is the number of bits to allocate to each host's subnet e.g. 8 would mean a /24 network on the host

        :return: The hostsubnetlength of this V1ClusterNetwork.
        :rtype: int
        """
        return self._hostsubnetlength

    @hostsubnetlength.setter
    def hostsubnetlength(self, hostsubnetlength):
        """
        Sets the hostsubnetlength of this V1ClusterNetwork.
        HostSubnetLength is the number of bits to allocate to each host's subnet e.g. 8 would mean a /24 network on the host

        :param hostsubnetlength: The hostsubnetlength of this V1ClusterNetwork.
        :type: int
        """

        self._hostsubnetlength = hostsubnetlength

    @property
    def service_network(self):
        """
        Gets the service_network of this V1ClusterNetwork.
        ServiceNetwork is the CIDR string to specify the service network

        :return: The service_network of this V1ClusterNetwork.
        :rtype: str
        """
        return self._service_network

    @service_network.setter
    def service_network(self, service_network):
        """
        Sets the service_network of this V1ClusterNetwork.
        ServiceNetwork is the CIDR string to specify the service network

        :param service_network: The service_network of this V1ClusterNetwork.
        :type: str
        """

        self._service_network = service_network

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1ClusterNetwork.swagger_types):
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
