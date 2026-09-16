# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# This file is generated from the WebDriver BiDi specification.
# DO NOT EDIT. Regenerate with:
#   bazel run //py:generate-bidi-protocol


from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register

if TYPE_CHECKING:
    from selenium.webdriver.common._bidi.network import BytesValueValue, Cookie, SameSite


@register("storage.PartitionKey")
@dataclass(frozen=True)
class PartitionKey(Record):
    """storage.PartitionKey.

    See https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
    """

    _EXTENSIBLE = True
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    source_origin: str | UnsetType = field(default=UNSET, metadata=meta("sourceOrigin", primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("storage.CookieFilter")
@dataclass(frozen=True)
class CookieFilter(Record):
    """storage.CookieFilter.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagecookiefilter
    """

    _EXTENSIBLE = True
    name: str | UnsetType = field(default=UNSET, metadata=meta("name", primitive="str"))
    value: BytesValueValue | UnsetType = field(default=UNSET, metadata=meta("value", ref="network.BytesValue"))
    domain: str | UnsetType = field(default=UNSET, metadata=meta("domain", primitive="str"))
    path: str | UnsetType = field(default=UNSET, metadata=meta("path", primitive="str"))
    size: int | UnsetType = field(default=UNSET, metadata=meta("size", primitive="int"))
    http_only: bool | UnsetType = field(default=UNSET, metadata=meta("httpOnly", primitive="bool"))
    secure: bool | UnsetType = field(default=UNSET, metadata=meta("secure", primitive="bool"))
    same_site: SameSite | UnsetType = field(default=UNSET, metadata=meta("sameSite", enum="network.SameSite"))
    expiry: int | UnsetType = field(default=UNSET, metadata=meta("expiry", primitive="int"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("storage.BrowsingContextPartitionDescriptor")
@dataclass(frozen=True)
class BrowsingContextPartitionDescriptor(Record):
    """storage.BrowsingContextPartitionDescriptor.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagebrowsingcontextpartitiondescriptor
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    type: str = field(default="context", init=False, metadata=meta("type", required=True, fixed="context"))


@register("storage.StorageKeyPartitionDescriptor")
@dataclass(frozen=True)
class StorageKeyPartitionDescriptor(Record):
    """storage.StorageKeyPartitionDescriptor.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagestoragekeypartitiondescriptor
    """

    _EXTENSIBLE = True
    type: str = field(default="storageKey", init=False, metadata=meta("type", required=True, fixed="storageKey"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    source_origin: str | UnsetType = field(default=UNSET, metadata=meta("sourceOrigin", primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("storage.GetCookiesParameters")
@dataclass(frozen=True)
class GetCookiesParameters(Record):
    """storage.GetCookiesParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagegetcookiesparameters
    """

    filter: CookieFilter | UnsetType = field(default=UNSET, metadata=meta("filter", ref="storage.CookieFilter"))
    partition: PartitionDescriptorValue | UnsetType = field(
        default=UNSET,
        metadata=meta("partition", ref="storage.PartitionDescriptor"),
    )


@register("storage.GetCookiesResult")
@dataclass(frozen=True)
class GetCookiesResult(Record):
    """storage.GetCookiesResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagegetcookiesresult
    """

    cookies: list[Cookie] = field(metadata=meta("cookies", required=True, ref="network.Cookie", is_list=True))
    partition_key: PartitionKey = field(metadata=meta("partitionKey", required=True, ref="storage.PartitionKey"))


@register("storage.PartialCookie")
@dataclass(frozen=True)
class PartialCookie(Record):
    """storage.PartialCookie.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagepartialcookie
    """

    _EXTENSIBLE = True
    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: BytesValueValue = field(metadata=meta("value", required=True, ref="network.BytesValue"))
    domain: str = field(metadata=meta("domain", required=True, primitive="str"))
    path: str | UnsetType = field(default=UNSET, metadata=meta("path", primitive="str"))
    http_only: bool | UnsetType = field(default=UNSET, metadata=meta("httpOnly", primitive="bool"))
    secure: bool | UnsetType = field(default=UNSET, metadata=meta("secure", primitive="bool"))
    same_site: SameSite | UnsetType = field(default=UNSET, metadata=meta("sameSite", enum="network.SameSite"))
    expiry: int | UnsetType = field(default=UNSET, metadata=meta("expiry", primitive="int"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("storage.SetCookieParameters")
@dataclass(frozen=True)
class SetCookieParameters(Record):
    """storage.SetCookieParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagesetcookieparameters
    """

    cookie: PartialCookie = field(metadata=meta("cookie", required=True, ref="storage.PartialCookie"))
    partition: PartitionDescriptorValue | UnsetType = field(
        default=UNSET,
        metadata=meta("partition", ref="storage.PartitionDescriptor"),
    )


@register("storage.SetCookieResult")
@dataclass(frozen=True)
class SetCookieResult(Record):
    """storage.SetCookieResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagesetcookieresult
    """

    partition_key: PartitionKey = field(metadata=meta("partitionKey", required=True, ref="storage.PartitionKey"))


@register("storage.DeleteCookiesParameters")
@dataclass(frozen=True)
class DeleteCookiesParameters(Record):
    """storage.DeleteCookiesParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagedeletecookiesparameters
    """

    filter: CookieFilter | UnsetType = field(default=UNSET, metadata=meta("filter", ref="storage.CookieFilter"))
    partition: PartitionDescriptorValue | UnsetType = field(
        default=UNSET,
        metadata=meta("partition", ref="storage.PartitionDescriptor"),
    )


@register("storage.DeleteCookiesResult")
@dataclass(frozen=True)
class DeleteCookiesResult(Record):
    """storage.DeleteCookiesResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagedeletecookiesresult
    """

    partition_key: PartitionKey = field(metadata=meta("partitionKey", required=True, ref="storage.PartitionKey"))


@register("storage.PartitionDescriptor")
class PartitionDescriptor(Union):
    """storage.PartitionDescriptor.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-storagepartitiondescriptor
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "context": "storage.BrowsingContextPartitionDescriptor",
        "storageKey": "storage.StorageKeyPartitionDescriptor",
    }
    _DISCRIMINATOR_VALUES = frozenset({"context", "storageKey"})
    _OBJECT_ONLY = True


PartitionDescriptorValue: TypeAlias = "BrowsingContextPartitionDescriptor | StorageKeyPartitionDescriptor"


class Storage(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-storage
    """

    def delete_cookies(
        self,
        filter: CookieFilter | UnsetType = UNSET,
        partition: PartitionDescriptorValue | UnsetType = UNSET,
    ) -> DeleteCookiesResult:
        """Execute storage.deleteCookies (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-storage-deleteCookies
        """
        params = DeleteCookiesParameters(filter=filter, partition=partition)
        return self._execute("storage.deleteCookies", params=params, result=DeleteCookiesResult)

    def get_cookies(
        self,
        filter: CookieFilter | UnsetType = UNSET,
        partition: PartitionDescriptorValue | UnsetType = UNSET,
    ) -> GetCookiesResult:
        """Execute storage.getCookies (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-storage-getCookies
        """
        params = GetCookiesParameters(filter=filter, partition=partition)
        return self._execute("storage.getCookies", params=params, result=GetCookiesResult)

    def set_cookie(
        self,
        cookie: PartialCookie,
        partition: PartitionDescriptorValue | UnsetType = UNSET,
    ) -> SetCookieResult:
        """Execute storage.setCookie (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-storage-setCookie
        """
        params = SetCookieParameters(cookie=cookie, partition=partition)
        return self._execute("storage.setCookie", params=params, result=SetCookieResult)
