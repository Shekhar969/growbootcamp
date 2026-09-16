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
from typing import Any, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register


@register("webExtension.ExtensionPath")
@dataclass(frozen=True)
class ExtensionPath(Record):
    """webExtension.ExtensionPath.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensionextensionpath
    """

    path: str = field(metadata=meta("path", required=True, primitive="str"))
    type: str = field(default="path", init=False, metadata=meta("type", required=True, fixed="path"))


@register("webExtension.ExtensionArchivePath")
@dataclass(frozen=True)
class ExtensionArchivePath(Record):
    """webExtension.ExtensionArchivePath.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensionextensionarchivepath
    """

    path: str = field(metadata=meta("path", required=True, primitive="str"))
    type: str = field(default="archivePath", init=False, metadata=meta("type", required=True, fixed="archivePath"))


@register("webExtension.ExtensionBase64Encoded")
@dataclass(frozen=True)
class ExtensionBase64Encoded(Record):
    """webExtension.ExtensionBase64Encoded.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensionextensionbase64encoded
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="base64", init=False, metadata=meta("type", required=True, fixed="base64"))


@register("webExtension.InstallResult")
@dataclass(frozen=True)
class InstallResult(Record):
    """webExtension.InstallResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensioninstallresult
    """

    extension: str = field(metadata=meta("extension", required=True, primitive="str"))


@register("webExtension.UninstallParameters")
@dataclass(frozen=True)
class UninstallParameters(Record):
    """webExtension.UninstallParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensionuninstallparameters
    """

    extension: str = field(metadata=meta("extension", required=True, primitive="str"))


@register("webExtension.InstallParameters")
@dataclass(frozen=True)
class InstallParameters(Record):
    """webExtension.InstallParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensioninstallparameters
    """

    _EXTENSIBLE = True
    extension_data: ExtensionDataValue = field(
        metadata=meta("extensionData", required=True, ref="webExtension.ExtensionData"),
    )
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("webExtension.ExtensionData")
class ExtensionData(Union):
    """webExtension.ExtensionData.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-webextensionextensiondata
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "archivePath": "webExtension.ExtensionArchivePath",
        "base64": "webExtension.ExtensionBase64Encoded",
        "path": "webExtension.ExtensionPath",
    }
    _DISCRIMINATOR_VALUES = frozenset({"archivePath", "base64", "path"})
    _OBJECT_ONLY = True


ExtensionDataValue: TypeAlias = "ExtensionArchivePath | ExtensionBase64Encoded | ExtensionPath"


class WebExtension(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-webExtension
    """

    def install(self, extension_data: ExtensionDataValue) -> InstallResult:
        """Execute webExtension.install (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-webExtension-install
        """
        params = InstallParameters(extension_data=extension_data)
        return self._execute("webExtension.install", params=params, result=InstallResult)

    def uninstall(self, extension: str) -> Any:
        """Execute webExtension.uninstall (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-webExtension-uninstall
        """
        params = UninstallParameters(extension=extension)
        return self._execute("webExtension.uninstall", params=params, result=None)
