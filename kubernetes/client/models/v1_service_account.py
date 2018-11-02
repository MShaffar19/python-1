# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ServiceAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'api_version': 'str',
        'automount_service_account_token': 'bool',
        'image_pull_secrets': 'list[V1LocalObjectReference]',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'secrets': 'list[V1ObjectReference]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'automount_service_account_token': 'automountServiceAccountToken',
        'image_pull_secrets': 'imagePullSecrets',
        'kind': 'kind',
        'metadata': 'metadata',
        'secrets': 'secrets'
    }

    def __init__(self, api_version=None, automount_service_account_token=None, image_pull_secrets=None, kind=None, metadata=None, secrets=None):
        """
        V1ServiceAccount - a model defined in Swagger
        """

        self._api_version = None
        self._automount_service_account_token = None
        self._image_pull_secrets = None
        self._kind = None
        self._metadata = None
        self._secrets = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        if automount_service_account_token is not None:
          self.automount_service_account_token = automount_service_account_token
        if image_pull_secrets is not None:
          self.image_pull_secrets = image_pull_secrets
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        if secrets is not None:
          self.secrets = secrets

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ServiceAccount.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1ServiceAccount.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ServiceAccount.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ServiceAccount.
        :type: str
        """

        self._api_version = api_version

    @property
    def automount_service_account_token(self):
        """
        Gets the automount_service_account_token of this V1ServiceAccount.
        AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.

        :return: The automount_service_account_token of this V1ServiceAccount.
        :rtype: bool
        """
        return self._automount_service_account_token

    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token):
        """
        Sets the automount_service_account_token of this V1ServiceAccount.
        AutomountServiceAccountToken indicates whether pods running as this service account should have an API token automatically mounted. Can be overridden at the pod level.

        :param automount_service_account_token: The automount_service_account_token of this V1ServiceAccount.
        :type: bool
        """

        self._automount_service_account_token = automount_service_account_token

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1ServiceAccount.
        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod

        :return: The image_pull_secrets of this V1ServiceAccount.
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1ServiceAccount.
        ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod

        :param image_pull_secrets: The image_pull_secrets of this V1ServiceAccount.
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def kind(self):
        """
        Gets the kind of this V1ServiceAccount.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ServiceAccount.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ServiceAccount.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ServiceAccount.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ServiceAccount.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :return: The metadata of this V1ServiceAccount.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ServiceAccount.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1ServiceAccount.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def secrets(self):
        """
        Gets the secrets of this V1ServiceAccount.
        Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: https://kubernetes.io/docs/concepts/configuration/secret

        :return: The secrets of this V1ServiceAccount.
        :rtype: list[V1ObjectReference]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """
        Sets the secrets of this V1ServiceAccount.
        Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: https://kubernetes.io/docs/concepts/configuration/secret

        :param secrets: The secrets of this V1ServiceAccount.
        :type: list[V1ObjectReference]
        """

        self._secrets = secrets

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
        if not isinstance(other, V1ServiceAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
