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
from enum import Enum
from typing import Any

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, UnsetType, meta, register


@register("permissions.PermissionState")
class PermissionState(str, Enum):
    GRANTED = "granted"
    DENIED = "denied"
    PROMPT = "prompt"


@register("permissions.PermissionDescriptor")
@dataclass(frozen=True)
class PermissionDescriptor(Record):
    name: str = field(metadata=meta("name", required=True, primitive="str"))


@register("permissions.SetPermissionParameters")
@dataclass(frozen=True)
class SetPermissionParameters(Record):
    descriptor: PermissionDescriptor = field(
        metadata=meta("descriptor", required=True, ref="permissions.PermissionDescriptor"),
    )
    state: PermissionState = field(metadata=meta("state", required=True, enum="permissions.PermissionState"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    embedded_origin: str | UnsetType = field(default=UNSET, metadata=meta("embeddedOrigin", primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


class Permissions(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    """

    def set_permission(
        self,
        descriptor: PermissionDescriptor,
        state: PermissionState,
        origin: str,
        embedded_origin: str | UnsetType = UNSET,
        user_context: str | UnsetType = UNSET,
    ) -> Any:
        """Execute permissions.setPermission (internal, unsupported)."""
        params = SetPermissionParameters(
            descriptor=descriptor,
            state=state,
            origin=origin,
            embedded_origin=embedded_origin,
            user_context=user_context,
        )
        return self._execute("permissions.setPermission", params=params, result=None)
