# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class GeoReplicationStatusType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the secondary location.
    """

    LIVE = "live"
    BOOTSTRAP = "bootstrap"
    UNAVAILABLE = "unavailable"

class OdataMetadataFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    APPLICATION_JSON_ODATA_NOMETADATA = "application/json;odata=nometadata"
    APPLICATION_JSON_ODATA_MINIMALMETADATA = "application/json;odata=minimalmetadata"
    APPLICATION_JSON_ODATA_FULLMETADATA = "application/json;odata=fullmetadata"

class ResponseFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    RETURN_NO_CONTENT = "return-no-content"
    RETURN_CONTENT = "return-content"