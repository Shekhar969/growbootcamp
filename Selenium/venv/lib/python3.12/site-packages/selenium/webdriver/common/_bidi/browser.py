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
from typing import TYPE_CHECKING, Any, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register

if TYPE_CHECKING:
    from selenium.webdriver.common._bidi.session import ProxyConfigurationValue, UserPromptHandler


@register("browser.ClientWindowInfoState")
class ClientWindowInfoState(str, Enum):
    FULLSCREEN = "fullscreen"
    MAXIMIZED = "maximized"
    MINIMIZED = "minimized"
    NORMAL = "normal"


@register("browser.ClientWindowNamedStateState")
class ClientWindowNamedStateState(str, Enum):
    FULLSCREEN = "fullscreen"
    MAXIMIZED = "maximized"
    MINIMIZED = "minimized"


@register("browser.ClientWindowInfo")
@dataclass(frozen=True)
class ClientWindowInfo(Record):
    """browser.ClientWindowInfo.

    See https://w3c.github.io/webdriver-bidi/#type-browser-ClientWindowInfo
    """

    active: bool = field(metadata=meta("active", required=True, primitive="bool"))
    client_window: str = field(metadata=meta("clientWindow", required=True, primitive="str"))
    height: int = field(metadata=meta("height", required=True, primitive="int"))
    state: ClientWindowInfoState = field(
        metadata=meta("state", required=True, enum="browser.ClientWindowInfoState"),
    )
    width: int = field(metadata=meta("width", required=True, primitive="int"))
    x: int = field(metadata=meta("x", required=True, primitive="int"))
    y: int = field(metadata=meta("y", required=True, primitive="int"))


@register("browser.UserContextInfo")
@dataclass(frozen=True)
class UserContextInfo(Record):
    """browser.UserContextInfo.

    See https://w3c.github.io/webdriver-bidi/#type-browser-UserContextInfo
    """

    user_context: str = field(metadata=meta("userContext", required=True, primitive="str"))


@register("browser.CreateUserContextParameters")
@dataclass(frozen=True)
class CreateUserContextParameters(Record):
    """browser.CreateUserContextParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsercreateusercontextparameters
    """

    accept_insecure_certs: bool | UnsetType = field(
        default=UNSET,
        metadata=meta("acceptInsecureCerts", primitive="bool"),
    )
    proxy: ProxyConfigurationValue | UnsetType = field(
        default=UNSET,
        metadata=meta("proxy", ref="session.ProxyConfiguration"),
    )
    unhandled_prompt_behavior: UserPromptHandler | UnsetType = field(
        default=UNSET,
        metadata=meta("unhandledPromptBehavior", ref="session.UserPromptHandler"),
    )


@register("browser.GetClientWindowsResult")
@dataclass(frozen=True)
class GetClientWindowsResult(Record):
    """browser.GetClientWindowsResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsergetclientwindowsresult
    """

    client_windows: list[ClientWindowInfo] = field(
        metadata=meta("clientWindows", required=True, ref="browser.ClientWindowInfo", is_list=True),
    )


@register("browser.GetUserContextsResult")
@dataclass(frozen=True)
class GetUserContextsResult(Record):
    """browser.GetUserContextsResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsergetusercontextsresult
    """

    user_contexts: list[UserContextInfo] = field(
        metadata=meta("userContexts", required=True, ref="browser.UserContextInfo", is_list=True),
    )


@register("browser.RemoveUserContextParameters")
@dataclass(frozen=True)
class RemoveUserContextParameters(Record):
    """browser.RemoveUserContextParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browserremoveusercontextparameters
    """

    user_context: str = field(metadata=meta("userContext", required=True, primitive="str"))


@register("browser.SetDownloadBehaviorParameters")
@dataclass(frozen=True)
class SetDownloadBehaviorParameters(Record):
    """browser.SetDownloadBehaviorParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsersetdownloadbehaviorparameters
    """

    download_behavior: DownloadBehaviorValue | None = field(
        metadata=meta("downloadBehavior", required=True, nullable=True, ref="browser.DownloadBehavior"),
    )
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("browser.SetClientWindowStateParameters_ClientWindowNamedState")
@dataclass(frozen=True)
class SetClientWindowStateParametersClientWindowNamedState(Record):
    client_window: str = field(metadata=meta("clientWindow", required=True, primitive="str"))
    state: ClientWindowNamedStateState = field(
        metadata=meta("state", required=True, enum="browser.ClientWindowNamedStateState"),
    )


@register("browser.SetClientWindowStateParameters_ClientWindowRectState")
@dataclass(frozen=True)
class SetClientWindowStateParametersClientWindowRectState(Record):
    client_window: str = field(metadata=meta("clientWindow", required=True, primitive="str"))
    state: str = field(default="normal", init=False, metadata=meta("state", required=True, fixed="normal"))
    width: int | UnsetType = field(default=UNSET, metadata=meta("width", primitive="int"))
    height: int | UnsetType = field(default=UNSET, metadata=meta("height", primitive="int"))
    x: int | UnsetType = field(default=UNSET, metadata=meta("x", primitive="int"))
    y: int | UnsetType = field(default=UNSET, metadata=meta("y", primitive="int"))


@register("browser.DownloadBehavior_Allowed")
@dataclass(frozen=True)
class DownloadBehaviorAllowed(Record):
    destination_folder: str = field(metadata=meta("destinationFolder", required=True, primitive="str"))
    type: str = field(default="allowed", init=False, metadata=meta("type", required=True, fixed="allowed"))


@register("browser.DownloadBehavior_Denied")
@dataclass(frozen=True)
class DownloadBehaviorDenied(Record):
    type: str = field(default="denied", init=False, metadata=meta("type", required=True, fixed="denied"))


@register("browser.SetClientWindowStateParameters")
class SetClientWindowStateParameters(Union):
    """browser.SetClientWindowStateParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsersetclientwindowstateparameters
    """

    _DISCRIMINATOR = "state"
    _VARIANTS = {
        "normal": "browser.SetClientWindowStateParameters_ClientWindowRectState",
    }
    _FALLBACK = "browser.SetClientWindowStateParameters_ClientWindowNamedState"
    _DISCRIMINATOR_VALUES = frozenset({"normal", "fullscreen", "maximized", "minimized"})
    _OBJECT_ONLY = True


SetClientWindowStateParametersValue: TypeAlias = (
    "SetClientWindowStateParametersClientWindowRectState | SetClientWindowStateParametersClientWindowNamedState"
)


@register("browser.DownloadBehavior")
class DownloadBehavior(Union):
    """browser.DownloadBehavior.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browserdownloadbehavior
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "allowed": "browser.DownloadBehavior_Allowed",
        "denied": "browser.DownloadBehavior_Denied",
    }
    _DISCRIMINATOR_VALUES = frozenset({"allowed", "denied"})
    _OBJECT_ONLY = True


DownloadBehaviorValue: TypeAlias = "DownloadBehaviorAllowed | DownloadBehaviorDenied"


class Browser(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-browser
    """

    def close(self) -> Any:
        """Execute browser.close (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-close
        """
        return self._execute("browser.close", params=None, result=None)

    def create_user_context(
        self,
        accept_insecure_certs: bool | UnsetType = UNSET,
        proxy: ProxyConfigurationValue | UnsetType = UNSET,
        unhandled_prompt_behavior: UserPromptHandler | UnsetType = UNSET,
    ) -> UserContextInfo:
        """Execute browser.createUserContext (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-createUserContext
        """
        params = CreateUserContextParameters(
            accept_insecure_certs=accept_insecure_certs,
            proxy=proxy,
            unhandled_prompt_behavior=unhandled_prompt_behavior,
        )
        return self._execute("browser.createUserContext", params=params, result=UserContextInfo)

    def get_client_windows(self) -> GetClientWindowsResult:
        """Execute browser.getClientWindows (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-getClientWindows
        """
        return self._execute("browser.getClientWindows", params=None, result=GetClientWindowsResult)

    def get_user_contexts(self) -> GetUserContextsResult:
        """Execute browser.getUserContexts (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-getUserContexts
        """
        return self._execute("browser.getUserContexts", params=None, result=GetUserContextsResult)

    def remove_user_context(self, user_context: str) -> Any:
        """Execute browser.removeUserContext (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-removeUserContext
        """
        params = RemoveUserContextParameters(user_context=user_context)
        return self._execute("browser.removeUserContext", params=params, result=None)

    def set_client_window_state(
        self,
        client_window: str,
        state: ClientWindowNamedStateState,
        width: int | UnsetType = UNSET,
        height: int | UnsetType = UNSET,
        x: int | UnsetType = UNSET,
        y: int | UnsetType = UNSET,
    ) -> ClientWindowInfo:
        """Execute browser.setClientWindowState (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-setClientWindowState
        """
        params = SetClientWindowStateParameters.build(
            client_window=client_window,
            state=state,
            width=width,
            height=height,
            x=x,
            y=y,
        )
        return self._execute("browser.setClientWindowState", params=params, result=ClientWindowInfo)

    def set_download_behavior(
        self,
        download_behavior: DownloadBehaviorValue | None,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute browser.setDownloadBehavior (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browser-setDownloadBehavior
        """
        params = SetDownloadBehaviorParameters(download_behavior=download_behavior, user_contexts=user_contexts)
        return self._execute("browser.setDownloadBehavior", params=params, result=None)
