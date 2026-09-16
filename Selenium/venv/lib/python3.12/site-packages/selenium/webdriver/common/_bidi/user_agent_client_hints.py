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
from typing import Any

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, UnsetType, meta, register


@register("userAgentClientHints.ClientHintsMetadata")
@dataclass(frozen=True)
class ClientHintsMetadata(Record):
    """userAgentClientHints.ClientHintsMetadata.

    See https://wicg.github.io/ua-client-hints/#cddl-type-useragentclienthintsclienthintsmetadata
    """

    brands: list[BrandVersion] | UnsetType = field(
        default=UNSET,
        metadata=meta("brands", ref="userAgentClientHints.BrandVersion", is_list=True),
    )
    full_version_list: list[BrandVersion] | UnsetType = field(
        default=UNSET,
        metadata=meta("fullVersionList", ref="userAgentClientHints.BrandVersion", is_list=True),
    )
    platform: str | UnsetType = field(default=UNSET, metadata=meta("platform", primitive="str"))
    platform_version: str | UnsetType = field(default=UNSET, metadata=meta("platformVersion", primitive="str"))
    architecture: str | UnsetType = field(default=UNSET, metadata=meta("architecture", primitive="str"))
    model: str | UnsetType = field(default=UNSET, metadata=meta("model", primitive="str"))
    mobile: bool | UnsetType = field(default=UNSET, metadata=meta("mobile", primitive="bool"))
    bitness: str | UnsetType = field(default=UNSET, metadata=meta("bitness", primitive="str"))
    wow64: bool | UnsetType = field(default=UNSET, metadata=meta("wow64", primitive="bool"))
    form_factors: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("formFactors", is_list=True, primitive="str"),
    )


@register("userAgentClientHints.BrandVersion")
@dataclass(frozen=True)
class BrandVersion(Record):
    """userAgentClientHints.BrandVersion.

    See https://wicg.github.io/ua-client-hints/#cddl-type-useragentclienthintsbrandversion
    """

    brand: str = field(metadata=meta("brand", required=True, primitive="str"))
    version: str = field(metadata=meta("version", required=True, primitive="str"))


@register("userAgentClientHints.SetClientHintsOverrideCommandParams")
@dataclass(frozen=True)
class SetClientHintsOverrideCommandParams(Record):
    client_hints: ClientHintsMetadata | None = field(
        metadata=meta("clientHints", required=True, nullable=True, ref="userAgentClientHints.ClientHintsMetadata"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


class UserAgentClientHints(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    """

    def set_client_hints_override(
        self,
        client_hints: ClientHintsMetadata | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute userAgentClientHints.setClientHintsOverride (internal, unsupported)."""
        params = SetClientHintsOverrideCommandParams(
            client_hints=client_hints,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("userAgentClientHints.setClientHintsOverride", params=params, result=None)
