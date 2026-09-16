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
from typing import Any, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register


@register("session.UserPromptHandlerType")
class UserPromptHandlerType(str, Enum):
    """session.UserPromptHandlerType.

    See https://w3c.github.io/webdriver-bidi/#type-session-UserPromptHandlerType
    """

    ACCEPT = "accept"
    DISMISS = "dismiss"
    IGNORE = "ignore"


@register("session.CapabilitiesRequest")
@dataclass(frozen=True)
class CapabilitiesRequest(Record):
    """session.CapabilitiesRequest.

    See https://w3c.github.io/webdriver-bidi/#type-session-CapabilitiesRequest
    """

    always_match: CapabilityRequest | UnsetType = field(
        default=UNSET,
        metadata=meta("alwaysMatch", ref="session.CapabilityRequest"),
    )
    first_match: list[CapabilityRequest] | UnsetType = field(
        default=UNSET,
        metadata=meta("firstMatch", ref="session.CapabilityRequest", is_list=True),
    )


@register("session.CapabilityRequest")
@dataclass(frozen=True)
class CapabilityRequest(Record):
    """session.CapabilityRequest.

    See https://w3c.github.io/webdriver-bidi/#type-session-CapabilityRequest
    """

    _EXTENSIBLE = True
    accept_insecure_certs: bool | UnsetType = field(
        default=UNSET,
        metadata=meta("acceptInsecureCerts", primitive="bool"),
    )
    browser_name: str | UnsetType = field(default=UNSET, metadata=meta("browserName", primitive="str"))
    browser_version: str | UnsetType = field(default=UNSET, metadata=meta("browserVersion", primitive="str"))
    platform_name: str | UnsetType = field(default=UNSET, metadata=meta("platformName", primitive="str"))
    proxy: ProxyConfigurationValue | UnsetType = field(
        default=UNSET,
        metadata=meta("proxy", ref="session.ProxyConfiguration"),
    )
    unhandled_prompt_behavior: UserPromptHandler | UnsetType = field(
        default=UNSET,
        metadata=meta("unhandledPromptBehavior", ref="session.UserPromptHandler"),
    )
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.AutodetectProxyConfiguration")
@dataclass(frozen=True)
class AutodetectProxyConfiguration(Record):
    """session.AutodetectProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionautodetectproxyconfiguration
    """

    _EXTENSIBLE = True
    proxy_type: str = field(
        default="autodetect",
        init=False,
        metadata=meta("proxyType", required=True, fixed="autodetect"),
    )
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.DirectProxyConfiguration")
@dataclass(frozen=True)
class DirectProxyConfiguration(Record):
    """session.DirectProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessiondirectproxyconfiguration
    """

    _EXTENSIBLE = True
    proxy_type: str = field(default="direct", init=False, metadata=meta("proxyType", required=True, fixed="direct"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.ManualProxyConfiguration")
@dataclass(frozen=True)
class ManualProxyConfiguration(Record):
    """session.ManualProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionmanualproxyconfiguration
    """

    _EXTENSIBLE = True
    socks_proxy: str = field(metadata=meta("socksProxy", required=True, primitive="str"))
    socks_version: int = field(metadata=meta("socksVersion", required=True, primitive="int"))
    proxy_type: str = field(default="manual", init=False, metadata=meta("proxyType", required=True, fixed="manual"))
    http_proxy: str | UnsetType = field(default=UNSET, metadata=meta("httpProxy", primitive="str"))
    ssl_proxy: str | UnsetType = field(default=UNSET, metadata=meta("sslProxy", primitive="str"))
    no_proxy: list[str] | UnsetType = field(default=UNSET, metadata=meta("noProxy", is_list=True, primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.SocksProxyConfiguration")
@dataclass(frozen=True)
class SocksProxyConfiguration(Record):
    """session.SocksProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionsocksproxyconfiguration
    """

    socks_proxy: str = field(metadata=meta("socksProxy", required=True, primitive="str"))
    socks_version: int = field(metadata=meta("socksVersion", required=True, primitive="int"))


@register("session.PacProxyConfiguration")
@dataclass(frozen=True)
class PacProxyConfiguration(Record):
    """session.PacProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionpacproxyconfiguration
    """

    _EXTENSIBLE = True
    proxy_autoconfig_url: str = field(metadata=meta("proxyAutoconfigUrl", required=True, primitive="str"))
    proxy_type: str = field(default="pac", init=False, metadata=meta("proxyType", required=True, fixed="pac"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.SystemProxyConfiguration")
@dataclass(frozen=True)
class SystemProxyConfiguration(Record):
    """session.SystemProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionsystemproxyconfiguration
    """

    _EXTENSIBLE = True
    proxy_type: str = field(default="system", init=False, metadata=meta("proxyType", required=True, fixed="system"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.UserPromptHandler")
@dataclass(frozen=True)
class UserPromptHandler(Record):
    """session.UserPromptHandler.

    See https://w3c.github.io/webdriver-bidi/#type-session-UserPromptHandler
    """

    alert: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("alert", enum="session.UserPromptHandlerType"),
    )
    before_unload: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("beforeUnload", enum="session.UserPromptHandlerType"),
    )
    confirm: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("confirm", enum="session.UserPromptHandlerType"),
    )
    default: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("default", enum="session.UserPromptHandlerType"),
    )
    file: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("file", enum="session.UserPromptHandlerType"),
    )
    prompt: UserPromptHandlerType | UnsetType = field(
        default=UNSET,
        metadata=meta("prompt", enum="session.UserPromptHandlerType"),
    )


@register("session.SubscribeParameters")
@dataclass(frozen=True)
class SubscribeParameters(Record):
    """session.SubscribeParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionsubscribeparameters
    """

    events: list[str] = field(metadata=meta("events", required=True, is_list=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("session.UnsubscribeByIDRequest")
@dataclass(frozen=True)
class UnsubscribeByIDRequest(Record):
    """session.UnsubscribeByIDRequest.

    See https://w3c.github.io/webdriver-bidi/#type-session-UnsubscribeByIDRequest
    """

    subscriptions: list[str] = field(metadata=meta("subscriptions", required=True, is_list=True, primitive="str"))


@register("session.UnsubscribeByAttributesRequest")
@dataclass(frozen=True)
class UnsubscribeByAttributesRequest(Record):
    """session.UnsubscribeByAttributesRequest.

    See https://w3c.github.io/webdriver-bidi/#type-session-UnsubscribeByAttributesRequest
    """

    events: list[str] = field(metadata=meta("events", required=True, is_list=True, primitive="str"))


@register("session.StatusResult")
@dataclass(frozen=True)
class StatusResult(Record):
    """session.StatusResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionstatusresult
    """

    ready: bool = field(metadata=meta("ready", required=True, primitive="bool"))
    message: str = field(metadata=meta("message", required=True, primitive="str"))


@register("session.NewParameters")
@dataclass(frozen=True)
class NewParameters(Record):
    """session.NewParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionnewparameters
    """

    capabilities: CapabilitiesRequest = field(
        metadata=meta("capabilities", required=True, ref="session.CapabilitiesRequest"),
    )


@register("session.NewResult")
@dataclass(frozen=True)
class NewResult(Record):
    """session.NewResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionnewresult
    """

    session_id: str = field(metadata=meta("sessionId", required=True, primitive="str"))
    capabilities: NewResultCapabilities = field(
        metadata=meta("capabilities", required=True, ref="session.NewResultCapabilities"),
    )


@register("session.SubscribeResult")
@dataclass(frozen=True)
class SubscribeResult(Record):
    """session.SubscribeResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionsubscriberesult
    """

    subscription: str = field(metadata=meta("subscription", required=True, primitive="str"))


@register("session.NewResultCapabilities")
@dataclass(frozen=True)
class NewResultCapabilities(Record):
    _EXTENSIBLE = True
    accept_insecure_certs: bool = field(metadata=meta("acceptInsecureCerts", required=True, primitive="bool"))
    browser_name: str = field(metadata=meta("browserName", required=True, primitive="str"))
    browser_version: str = field(metadata=meta("browserVersion", required=True, primitive="str"))
    platform_name: str = field(metadata=meta("platformName", required=True, primitive="str"))
    set_window_rect: bool = field(metadata=meta("setWindowRect", required=True, primitive="bool"))
    user_agent: str = field(metadata=meta("userAgent", required=True, primitive="str"))
    proxy: ProxyConfigurationValue | UnsetType = field(
        default=UNSET,
        metadata=meta("proxy", ref="session.ProxyConfiguration"),
    )
    unhandled_prompt_behavior: UserPromptHandler | UnsetType = field(
        default=UNSET,
        metadata=meta("unhandledPromptBehavior", ref="session.UserPromptHandler"),
    )
    web_socket_url: str | UnsetType = field(default=UNSET, metadata=meta("webSocketUrl", primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("session.ProxyConfiguration")
class ProxyConfiguration(Union):
    """session.ProxyConfiguration.

    See https://w3c.github.io/webdriver-bidi/#type-session-ProxyConfiguration
    """

    _DISCRIMINATOR = "proxyType"
    _VARIANTS = {
        "autodetect": "session.AutodetectProxyConfiguration",
        "direct": "session.DirectProxyConfiguration",
        "manual": "session.ManualProxyConfiguration",
        "pac": "session.PacProxyConfiguration",
        "system": "session.SystemProxyConfiguration",
    }
    _DISCRIMINATOR_VALUES = frozenset({"autodetect", "direct", "manual", "pac", "system"})
    _OBJECT_ONLY = True


ProxyConfigurationValue: TypeAlias = (
    "AutodetectProxyConfiguration | DirectProxyConfiguration | ManualProxyConfiguration | PacProxyConfiguration"
    " | SystemProxyConfiguration"
)


@register("session.UnsubscribeParameters")
class UnsubscribeParameters(Union):
    """session.UnsubscribeParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-sessionunsubscribeparameters
    """

    _PRESENCE = (
        ("session.UnsubscribeByAttributesRequest", ("events",)),
        ("session.UnsubscribeByIDRequest", ("subscriptions",)),
    )
    _OBJECT_ONLY = True


UnsubscribeParametersValue: TypeAlias = "UnsubscribeByAttributesRequest | UnsubscribeByIDRequest"


class Session(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-session
    """

    def end(self) -> Any:
        """Execute session.end (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-session-end
        """
        return self._execute("session.end", params=None, result=None)

    def new(self, capabilities: CapabilitiesRequest) -> NewResult:
        """Execute session.new (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-session-new
        """
        params = NewParameters(capabilities=capabilities)
        return self._execute("session.new", params=params, result=NewResult)

    def status(self) -> StatusResult:
        """Execute session.status (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-session-status
        """
        return self._execute("session.status", params=None, result=StatusResult)

    def subscribe(
        self,
        events: list[str],
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> SubscribeResult:
        """Execute session.subscribe (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-session-subscribe
        """
        params = SubscribeParameters(events=events, contexts=contexts, user_contexts=user_contexts)
        return self._execute("session.subscribe", params=params, result=SubscribeResult)

    def unsubscribe(
        self,
        events: list[str] | UnsetType = UNSET,
        subscriptions: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute session.unsubscribe (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-session-unsubscribe
        """
        params = UnsubscribeParameters.build(events=events, subscriptions=subscriptions)
        return self._execute("session.unsubscribe", params=params, result=None)
