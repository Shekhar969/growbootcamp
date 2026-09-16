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
    from selenium.webdriver.common._bidi.script import StackTrace


@register("network.CollectorType")
class CollectorType(str, Enum):
    """network.CollectorType.

    See https://w3c.github.io/webdriver-bidi/#type-network-CollectorType
    """

    BLOB = "blob"


@register("network.SameSite")
class SameSite(str, Enum):
    """network.SameSite.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networksamesite
    """

    STRICT = "strict"
    LAX = "lax"
    NONE = "none"
    DEFAULT = "default"


@register("network.DataType")
class DataType(str, Enum):
    """network.DataType.

    See https://w3c.github.io/webdriver-bidi/#type-network-dataType
    """

    REQUEST = "request"
    RESPONSE = "response"


@register("network.InterceptPhase")
class InterceptPhase(str, Enum):
    """network.InterceptPhase.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkinterceptphase
    """

    BEFORE_REQUEST_SENT = "beforeRequestSent"
    RESPONSE_STARTED = "responseStarted"
    AUTH_REQUIRED = "authRequired"


@register("network.InitiatorType")
class InitiatorType(str, Enum):
    PARSER = "parser"
    SCRIPT = "script"
    PREFLIGHT = "preflight"
    OTHER = "other"


@register("network.ContinueWithAuthNoCredentialsAction")
class ContinueWithAuthNoCredentialsAction(str, Enum):
    DEFAULT = "default"
    CANCEL = "cancel"


@register("network.SetCacheBehaviorParametersCacheBehavior")
class SetCacheBehaviorParametersCacheBehavior(str, Enum):
    DEFAULT = "default"
    BYPASS = "bypass"


@register("network.AuthChallenge")
@dataclass(frozen=True)
class AuthChallenge(Record):
    """network.AuthChallenge.

    See https://w3c.github.io/webdriver-bidi/#type-network-AuthChallenge
    """

    scheme: str = field(metadata=meta("scheme", required=True, primitive="str"))
    realm: str = field(metadata=meta("realm", required=True, primitive="str"))


@register("network.AuthCredentials")
@dataclass(frozen=True)
class AuthCredentials(Record):
    """network.AuthCredentials.

    See https://w3c.github.io/webdriver-bidi/#type-network-AuthCredentials
    """

    username: str = field(metadata=meta("username", required=True, primitive="str"))
    password: str = field(metadata=meta("password", required=True, primitive="str"))
    type: str = field(default="password", init=False, metadata=meta("type", required=True, fixed="password"))


@register("network.BaseParameters")
@dataclass(frozen=True)
class BaseParameters(Record):
    """network.BaseParameters.

    See https://w3c.github.io/webdriver-bidi/#type-network-BaseParameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )


@register("network.StringValue")
@dataclass(frozen=True)
class StringValue(Record):
    """network.StringValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkstringvalue
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="string", init=False, metadata=meta("type", required=True, fixed="string"))


@register("network.Base64Value")
@dataclass(frozen=True)
class Base64Value(Record):
    """network.Base64Value.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkbase64value
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="base64", init=False, metadata=meta("type", required=True, fixed="base64"))


@register("network.Cookie")
@dataclass(frozen=True)
class Cookie(Record):
    """network.Cookie.

    See https://w3c.github.io/webdriver-bidi/#type-network-Cookie
    """

    _EXTENSIBLE = True
    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: BytesValueValue = field(metadata=meta("value", required=True, ref="network.BytesValue"))
    domain: str = field(metadata=meta("domain", required=True, primitive="str"))
    path: str = field(metadata=meta("path", required=True, primitive="str"))
    size: int = field(metadata=meta("size", required=True, primitive="int"))
    http_only: bool = field(metadata=meta("httpOnly", required=True, primitive="bool"))
    secure: bool = field(metadata=meta("secure", required=True, primitive="bool"))
    same_site: SameSite = field(metadata=meta("sameSite", required=True, enum="network.SameSite"))
    expiry: int | UnsetType = field(default=UNSET, metadata=meta("expiry", primitive="int"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("network.CookieHeader")
@dataclass(frozen=True)
class CookieHeader(Record):
    """network.CookieHeader.

    See https://w3c.github.io/webdriver-bidi/#type-network-CookieHeader
    """

    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: BytesValueValue = field(metadata=meta("value", required=True, ref="network.BytesValue"))


@register("network.FetchTimingInfo")
@dataclass(frozen=True)
class FetchTimingInfo(Record):
    """network.FetchTimingInfo.

    See https://w3c.github.io/webdriver-bidi/#type-network-FetchTimingInfo
    """

    time_origin: float = field(metadata=meta("timeOrigin", required=True, primitive="float"))
    request_time: float = field(metadata=meta("requestTime", required=True, primitive="float"))
    redirect_start: float = field(metadata=meta("redirectStart", required=True, primitive="float"))
    redirect_end: float = field(metadata=meta("redirectEnd", required=True, primitive="float"))
    fetch_start: float = field(metadata=meta("fetchStart", required=True, primitive="float"))
    dns_start: float = field(metadata=meta("dnsStart", required=True, primitive="float"))
    dns_end: float = field(metadata=meta("dnsEnd", required=True, primitive="float"))
    connect_start: float = field(metadata=meta("connectStart", required=True, primitive="float"))
    connect_end: float = field(metadata=meta("connectEnd", required=True, primitive="float"))
    tls_start: float = field(metadata=meta("tlsStart", required=True, primitive="float"))
    request_start: float = field(metadata=meta("requestStart", required=True, primitive="float"))
    response_start: float = field(metadata=meta("responseStart", required=True, primitive="float"))
    response_end: float = field(metadata=meta("responseEnd", required=True, primitive="float"))


@register("network.Header")
@dataclass(frozen=True)
class Header(Record):
    """network.Header.

    See https://w3c.github.io/webdriver-bidi/#type-network-Header
    """

    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: BytesValueValue = field(metadata=meta("value", required=True, ref="network.BytesValue"))


@register("network.Initiator")
@dataclass(frozen=True)
class Initiator(Record):
    """network.Initiator.

    See https://w3c.github.io/webdriver-bidi/#type-network-Initiator
    """

    column_number: int | UnsetType = field(default=UNSET, metadata=meta("columnNumber", primitive="int"))
    line_number: int | UnsetType = field(default=UNSET, metadata=meta("lineNumber", primitive="int"))
    request: str | UnsetType = field(default=UNSET, metadata=meta("request", primitive="str"))
    stack_trace: StackTrace | UnsetType = field(default=UNSET, metadata=meta("stackTrace", ref="script.StackTrace"))
    type: InitiatorType | UnsetType = field(default=UNSET, metadata=meta("type", enum="network.InitiatorType"))


@register("network.RequestData")
@dataclass(frozen=True)
class RequestData(Record):
    """network.RequestData.

    See https://w3c.github.io/webdriver-bidi/#type-network-RequestData
    """

    request: str = field(metadata=meta("request", required=True, primitive="str"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    method: str = field(metadata=meta("method", required=True, primitive="str"))
    headers: list[Header] = field(metadata=meta("headers", required=True, ref="network.Header", is_list=True))
    cookies: list[Cookie] = field(metadata=meta("cookies", required=True, ref="network.Cookie", is_list=True))
    headers_size: int = field(metadata=meta("headersSize", required=True, primitive="int"))
    body_size: int | None = field(metadata=meta("bodySize", required=True, nullable=True, primitive="int"))
    destination: str = field(metadata=meta("destination", required=True, primitive="str"))
    initiator_type: str | None = field(
        metadata=meta("initiatorType", required=True, nullable=True, primitive="str"),
    )
    timings: FetchTimingInfo = field(metadata=meta("timings", required=True, ref="network.FetchTimingInfo"))


@register("network.ResponseContent")
@dataclass(frozen=True)
class ResponseContent(Record):
    """network.ResponseContent.

    See https://w3c.github.io/webdriver-bidi/#type-network-ResponseContent
    """

    size: int = field(metadata=meta("size", required=True, primitive="int"))


@register("network.ResponseData")
@dataclass(frozen=True)
class ResponseData(Record):
    """network.ResponseData.

    See https://w3c.github.io/webdriver-bidi/#type-network-ResponseData
    """

    url: str = field(metadata=meta("url", required=True, primitive="str"))
    protocol: str = field(metadata=meta("protocol", required=True, primitive="str"))
    status: int = field(metadata=meta("status", required=True, primitive="int"))
    status_text: str = field(metadata=meta("statusText", required=True, primitive="str"))
    from_cache: bool = field(metadata=meta("fromCache", required=True, primitive="bool"))
    headers: list[Header] = field(metadata=meta("headers", required=True, ref="network.Header", is_list=True))
    mime_type: str = field(metadata=meta("mimeType", required=True, primitive="str"))
    bytes_received: int = field(metadata=meta("bytesReceived", required=True, primitive="int"))
    headers_size: int | None = field(metadata=meta("headersSize", required=True, nullable=True, primitive="int"))
    body_size: int | None = field(metadata=meta("bodySize", required=True, nullable=True, primitive="int"))
    content: ResponseContent = field(metadata=meta("content", required=True, ref="network.ResponseContent"))
    auth_challenges: list[AuthChallenge] | UnsetType = field(
        default=UNSET,
        metadata=meta("authChallenges", ref="network.AuthChallenge", is_list=True),
    )


@register("network.SetCookieHeader")
@dataclass(frozen=True)
class SetCookieHeader(Record):
    """network.SetCookieHeader.

    See https://w3c.github.io/webdriver-bidi/#type-network-SetCookieHeader
    """

    name: str = field(metadata=meta("name", required=True, primitive="str"))
    value: BytesValueValue = field(metadata=meta("value", required=True, ref="network.BytesValue"))
    domain: str | UnsetType = field(default=UNSET, metadata=meta("domain", primitive="str"))
    http_only: bool | UnsetType = field(default=UNSET, metadata=meta("httpOnly", primitive="bool"))
    expiry: str | UnsetType = field(default=UNSET, metadata=meta("expiry", primitive="str"))
    max_age: int | UnsetType = field(default=UNSET, metadata=meta("maxAge", primitive="int"))
    path: str | UnsetType = field(default=UNSET, metadata=meta("path", primitive="str"))
    same_site: SameSite | UnsetType = field(default=UNSET, metadata=meta("sameSite", enum="network.SameSite"))
    secure: bool | UnsetType = field(default=UNSET, metadata=meta("secure", primitive="bool"))


@register("network.UrlPatternPattern")
@dataclass(frozen=True)
class UrlPatternPattern(Record):
    """network.UrlPatternPattern.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkurlpatternpattern
    """

    type: str = field(default="pattern", init=False, metadata=meta("type", required=True, fixed="pattern"))
    protocol: str | UnsetType = field(default=UNSET, metadata=meta("protocol", primitive="str"))
    hostname: str | UnsetType = field(default=UNSET, metadata=meta("hostname", primitive="str"))
    port: str | UnsetType = field(default=UNSET, metadata=meta("port", primitive="str"))
    pathname: str | UnsetType = field(default=UNSET, metadata=meta("pathname", primitive="str"))
    search: str | UnsetType = field(default=UNSET, metadata=meta("search", primitive="str"))


@register("network.UrlPatternString")
@dataclass(frozen=True)
class UrlPatternString(Record):
    """network.UrlPatternString.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkurlpatternstring
    """

    pattern: str = field(metadata=meta("pattern", required=True, primitive="str"))
    type: str = field(default="string", init=False, metadata=meta("type", required=True, fixed="string"))


@register("network.AddDataCollectorParameters")
@dataclass(frozen=True)
class AddDataCollectorParameters(Record):
    """network.AddDataCollectorParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkadddatacollectorparameters
    """

    data_types: list[DataType] = field(
        metadata=meta("dataTypes", required=True, is_list=True, enum="network.DataType"),
    )
    max_encoded_data_size: int = field(metadata=meta("maxEncodedDataSize", required=True, primitive="int"))
    collector_type: CollectorType | UnsetType = field(
        default=UNSET,
        metadata=meta("collectorType", enum="network.CollectorType"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("network.AddDataCollectorResult")
@dataclass(frozen=True)
class AddDataCollectorResult(Record):
    """network.AddDataCollectorResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkadddatacollectorresult
    """

    collector: str = field(metadata=meta("collector", required=True, primitive="str"))


@register("network.AddInterceptParameters")
@dataclass(frozen=True)
class AddInterceptParameters(Record):
    """network.AddInterceptParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkaddinterceptparameters
    """

    phases: list[InterceptPhase] = field(
        metadata=meta("phases", required=True, is_list=True, enum="network.InterceptPhase"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    url_patterns: list[UrlPatternValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("urlPatterns", ref="network.UrlPattern", is_list=True),
    )


@register("network.AddInterceptResult")
@dataclass(frozen=True)
class AddInterceptResult(Record):
    """network.AddInterceptResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkaddinterceptresult
    """

    intercept: str = field(metadata=meta("intercept", required=True, primitive="str"))


@register("network.ContinueRequestParameters")
@dataclass(frozen=True)
class ContinueRequestParameters(Record):
    """network.ContinueRequestParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkcontinuerequestparameters
    """

    request: str = field(metadata=meta("request", required=True, primitive="str"))
    body: BytesValueValue | UnsetType = field(default=UNSET, metadata=meta("body", ref="network.BytesValue"))
    cookies: list[CookieHeader] | UnsetType = field(
        default=UNSET,
        metadata=meta("cookies", ref="network.CookieHeader", is_list=True),
    )
    headers: list[Header] | UnsetType = field(
        default=UNSET,
        metadata=meta("headers", ref="network.Header", is_list=True),
    )
    method: str | UnsetType = field(default=UNSET, metadata=meta("method", primitive="str"))
    url: str | UnsetType = field(default=UNSET, metadata=meta("url", primitive="str"))


@register("network.ContinueResponseParameters")
@dataclass(frozen=True)
class ContinueResponseParameters(Record):
    """network.ContinueResponseParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkcontinueresponseparameters
    """

    request: str = field(metadata=meta("request", required=True, primitive="str"))
    cookies: list[SetCookieHeader] | UnsetType = field(
        default=UNSET,
        metadata=meta("cookies", ref="network.SetCookieHeader", is_list=True),
    )
    credentials: AuthCredentials | UnsetType = field(
        default=UNSET,
        metadata=meta("credentials", ref="network.AuthCredentials"),
    )
    headers: list[Header] | UnsetType = field(
        default=UNSET,
        metadata=meta("headers", ref="network.Header", is_list=True),
    )
    reason_phrase: str | UnsetType = field(default=UNSET, metadata=meta("reasonPhrase", primitive="str"))
    status_code: int | UnsetType = field(default=UNSET, metadata=meta("statusCode", primitive="int"))


@register("network.DisownDataParameters")
@dataclass(frozen=True)
class DisownDataParameters(Record):
    """network.DisownDataParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkdisowndataparameters
    """

    data_type: DataType = field(metadata=meta("dataType", required=True, enum="network.DataType"))
    collector: str = field(metadata=meta("collector", required=True, primitive="str"))
    request: str = field(metadata=meta("request", required=True, primitive="str"))


@register("network.FailRequestParameters")
@dataclass(frozen=True)
class FailRequestParameters(Record):
    """network.FailRequestParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkfailrequestparameters
    """

    request: str = field(metadata=meta("request", required=True, primitive="str"))


@register("network.GetDataParameters")
@dataclass(frozen=True)
class GetDataParameters(Record):
    """network.GetDataParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkgetdataparameters
    """

    data_type: DataType = field(metadata=meta("dataType", required=True, enum="network.DataType"))
    request: str = field(metadata=meta("request", required=True, primitive="str"))
    collector: str | UnsetType = field(default=UNSET, metadata=meta("collector", primitive="str"))
    disown: bool | UnsetType = field(default=UNSET, metadata=meta("disown", primitive="bool"))


@register("network.GetDataResult")
@dataclass(frozen=True)
class GetDataResult(Record):
    """network.GetDataResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkgetdataresult
    """

    bytes: BytesValueValue = field(metadata=meta("bytes", required=True, ref="network.BytesValue"))


@register("network.ProvideResponseParameters")
@dataclass(frozen=True)
class ProvideResponseParameters(Record):
    """network.ProvideResponseParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkprovideresponseparameters
    """

    request: str = field(metadata=meta("request", required=True, primitive="str"))
    body: BytesValueValue | UnsetType = field(default=UNSET, metadata=meta("body", ref="network.BytesValue"))
    cookies: list[SetCookieHeader] | UnsetType = field(
        default=UNSET,
        metadata=meta("cookies", ref="network.SetCookieHeader", is_list=True),
    )
    headers: list[Header] | UnsetType = field(
        default=UNSET,
        metadata=meta("headers", ref="network.Header", is_list=True),
    )
    reason_phrase: str | UnsetType = field(default=UNSET, metadata=meta("reasonPhrase", primitive="str"))
    status_code: int | UnsetType = field(default=UNSET, metadata=meta("statusCode", primitive="int"))


@register("network.RemoveDataCollectorParameters")
@dataclass(frozen=True)
class RemoveDataCollectorParameters(Record):
    """network.RemoveDataCollectorParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkremovedatacollectorparameters
    """

    collector: str = field(metadata=meta("collector", required=True, primitive="str"))


@register("network.RemoveInterceptParameters")
@dataclass(frozen=True)
class RemoveInterceptParameters(Record):
    """network.RemoveInterceptParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkremoveinterceptparameters
    """

    intercept: str = field(metadata=meta("intercept", required=True, primitive="str"))


@register("network.SetCacheBehaviorParameters")
@dataclass(frozen=True)
class SetCacheBehaviorParameters(Record):
    """network.SetCacheBehaviorParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networksetcachebehaviorparameters
    """

    cache_behavior: SetCacheBehaviorParametersCacheBehavior = field(
        metadata=meta("cacheBehavior", required=True, enum="network.SetCacheBehaviorParametersCacheBehavior"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))


@register("network.SetExtraHeadersParameters")
@dataclass(frozen=True)
class SetExtraHeadersParameters(Record):
    """network.SetExtraHeadersParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networksetextraheadersparameters
    """

    headers: list[Header] = field(metadata=meta("headers", required=True, ref="network.Header", is_list=True))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("network.AuthRequiredParameters")
@dataclass(frozen=True)
class AuthRequiredParameters(Record):
    """network.AuthRequiredParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkauthrequiredparameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    response: ResponseData = field(metadata=meta("response", required=True, ref="network.ResponseData"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )


@register("network.BeforeRequestSentParameters")
@dataclass(frozen=True)
class BeforeRequestSentParameters(Record):
    """network.BeforeRequestSentParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkbeforerequestsentparameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )
    initiator: Initiator | UnsetType = field(default=UNSET, metadata=meta("initiator", ref="network.Initiator"))


@register("network.FetchErrorParameters")
@dataclass(frozen=True)
class FetchErrorParameters(Record):
    """network.FetchErrorParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkfetcherrorparameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    error_text: str = field(metadata=meta("errorText", required=True, primitive="str"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )


@register("network.ResponseCompletedParameters")
@dataclass(frozen=True)
class ResponseCompletedParameters(Record):
    """network.ResponseCompletedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkresponsecompletedparameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    response: ResponseData = field(metadata=meta("response", required=True, ref="network.ResponseData"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )


@register("network.ResponseStartedParameters")
@dataclass(frozen=True)
class ResponseStartedParameters(Record):
    """network.ResponseStartedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkresponsestartedparameters
    """

    context: str | None = field(metadata=meta("context", required=True, nullable=True, primitive="str"))
    is_blocked: bool = field(metadata=meta("isBlocked", required=True, primitive="bool"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    redirect_count: int = field(metadata=meta("redirectCount", required=True, primitive="int"))
    request: RequestData = field(metadata=meta("request", required=True, ref="network.RequestData"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    response: ResponseData = field(metadata=meta("response", required=True, ref="network.ResponseData"))
    user_context: str | None | UnsetType = field(
        default=UNSET,
        metadata=meta("userContext", nullable=True, primitive="str"),
    )
    intercepts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("intercepts", is_list=True, primitive="str"),
    )


@register("network.ContinueWithAuthParameters_Credentials")
@dataclass(frozen=True)
class ContinueWithAuthParametersCredentials(Record):
    request: str = field(metadata=meta("request", required=True, primitive="str"))
    credentials: AuthCredentials = field(metadata=meta("credentials", required=True, ref="network.AuthCredentials"))
    action: str = field(
        default="provideCredentials",
        init=False,
        metadata=meta("action", required=True, fixed="provideCredentials"),
    )


@register("network.ContinueWithAuthParameters_NoCredentials")
@dataclass(frozen=True)
class ContinueWithAuthParametersNoCredentials(Record):
    request: str = field(metadata=meta("request", required=True, primitive="str"))
    action: ContinueWithAuthNoCredentialsAction = field(
        metadata=meta("action", required=True, enum="network.ContinueWithAuthNoCredentialsAction"),
    )


@register("network.BytesValue")
class BytesValue(Union):
    """network.BytesValue.

    See https://w3c.github.io/webdriver-bidi/#type-network-BytesValue
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "string": "network.StringValue",
        "base64": "network.Base64Value",
    }
    _DISCRIMINATOR_VALUES = frozenset({"string", "base64"})
    _OBJECT_ONLY = True


BytesValueValue: TypeAlias = "StringValue | Base64Value"


@register("network.UrlPattern")
class UrlPattern(Union):
    """network.UrlPattern.

    See https://w3c.github.io/webdriver-bidi/#type-network-UrlPattern
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "pattern": "network.UrlPatternPattern",
        "string": "network.UrlPatternString",
    }
    _DISCRIMINATOR_VALUES = frozenset({"pattern", "string"})
    _OBJECT_ONLY = True


UrlPatternValue: TypeAlias = "UrlPatternPattern | UrlPatternString"


@register("network.ContinueWithAuthParameters")
class ContinueWithAuthParameters(Union):
    """network.ContinueWithAuthParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-networkcontinuewithauthparameters
    """

    _DISCRIMINATOR = "action"
    _VARIANTS = {
        "provideCredentials": "network.ContinueWithAuthParameters_Credentials",
    }
    _FALLBACK = "network.ContinueWithAuthParameters_NoCredentials"
    _DISCRIMINATOR_VALUES = frozenset({"provideCredentials", "default", "cancel"})
    _OBJECT_ONLY = True


ContinueWithAuthParametersValue: TypeAlias = (
    "ContinueWithAuthParametersCredentials | ContinueWithAuthParametersNoCredentials"
)


class Network(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-network
    """

    EVENTS = {
        "auth_required": "network.authRequired",
        "before_request_sent": "network.beforeRequestSent",
        "fetch_error": "network.fetchError",
        "response_completed": "network.responseCompleted",
        "response_started": "network.responseStarted",
    }
    EVENT_TYPES = {
        "network.authRequired": "network.AuthRequiredParameters",
        "network.beforeRequestSent": "network.BeforeRequestSentParameters",
        "network.fetchError": "network.FetchErrorParameters",
        "network.responseCompleted": "network.ResponseCompletedParameters",
        "network.responseStarted": "network.ResponseStartedParameters",
    }

    def add_data_collector(
        self,
        data_types: list[DataType],
        max_encoded_data_size: int,
        collector_type: CollectorType | UnsetType = UNSET,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> AddDataCollectorResult:
        """Execute network.addDataCollector (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-addDataCollector
        """
        params = AddDataCollectorParameters(
            data_types=data_types,
            max_encoded_data_size=max_encoded_data_size,
            collector_type=collector_type,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("network.addDataCollector", params=params, result=AddDataCollectorResult)

    def add_intercept(
        self,
        phases: list[InterceptPhase],
        contexts: list[str] | UnsetType = UNSET,
        url_patterns: list[UrlPatternValue] | UnsetType = UNSET,
    ) -> AddInterceptResult:
        """Execute network.addIntercept (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-addIntercept
        """
        params = AddInterceptParameters(phases=phases, contexts=contexts, url_patterns=url_patterns)
        return self._execute("network.addIntercept", params=params, result=AddInterceptResult)

    def continue_request(
        self,
        request: str,
        body: BytesValueValue | UnsetType = UNSET,
        cookies: list[CookieHeader] | UnsetType = UNSET,
        headers: list[Header] | UnsetType = UNSET,
        method: str | UnsetType = UNSET,
        url: str | UnsetType = UNSET,
    ) -> Any:
        """Execute network.continueRequest (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-continueRequest
        """
        params = ContinueRequestParameters(
            request=request,
            body=body,
            cookies=cookies,
            headers=headers,
            method=method,
            url=url,
        )
        return self._execute("network.continueRequest", params=params, result=None)

    def continue_response(
        self,
        request: str,
        cookies: list[SetCookieHeader] | UnsetType = UNSET,
        credentials: AuthCredentials | UnsetType = UNSET,
        headers: list[Header] | UnsetType = UNSET,
        reason_phrase: str | UnsetType = UNSET,
        status_code: int | UnsetType = UNSET,
    ) -> Any:
        """Execute network.continueResponse (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-continueResponse
        """
        params = ContinueResponseParameters(
            request=request,
            cookies=cookies,
            credentials=credentials,
            headers=headers,
            reason_phrase=reason_phrase,
            status_code=status_code,
        )
        return self._execute("network.continueResponse", params=params, result=None)

    def continue_with_auth(
        self,
        request: str,
        action: str,
        credentials: AuthCredentials | UnsetType = UNSET,
    ) -> Any:
        """Execute network.continueWithAuth (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-continueWithAuth
        """
        params = ContinueWithAuthParameters.build(request=request, action=action, credentials=credentials)
        return self._execute("network.continueWithAuth", params=params, result=None)

    def disown_data(self, data_type: DataType, collector: str, request: str) -> Any:
        """Execute network.disownData (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-disownData
        """
        params = DisownDataParameters(data_type=data_type, collector=collector, request=request)
        return self._execute("network.disownData", params=params, result=None)

    def fail_request(self, request: str) -> Any:
        """Execute network.failRequest (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-failRequest
        """
        params = FailRequestParameters(request=request)
        return self._execute("network.failRequest", params=params, result=None)

    def get_data(
        self,
        data_type: DataType,
        request: str,
        collector: str | UnsetType = UNSET,
        disown: bool | UnsetType = UNSET,
    ) -> GetDataResult:
        """Execute network.getData (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-getData
        """
        params = GetDataParameters(data_type=data_type, collector=collector, disown=disown, request=request)
        return self._execute("network.getData", params=params, result=GetDataResult)

    def provide_response(
        self,
        request: str,
        body: BytesValueValue | UnsetType = UNSET,
        cookies: list[SetCookieHeader] | UnsetType = UNSET,
        headers: list[Header] | UnsetType = UNSET,
        reason_phrase: str | UnsetType = UNSET,
        status_code: int | UnsetType = UNSET,
    ) -> Any:
        """Execute network.provideResponse (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-provideResponse
        """
        params = ProvideResponseParameters(
            request=request,
            body=body,
            cookies=cookies,
            headers=headers,
            reason_phrase=reason_phrase,
            status_code=status_code,
        )
        return self._execute("network.provideResponse", params=params, result=None)

    def remove_data_collector(self, collector: str) -> Any:
        """Execute network.removeDataCollector (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-removeDataCollector
        """
        params = RemoveDataCollectorParameters(collector=collector)
        return self._execute("network.removeDataCollector", params=params, result=None)

    def remove_intercept(self, intercept: str) -> Any:
        """Execute network.removeIntercept (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-removeIntercept
        """
        params = RemoveInterceptParameters(intercept=intercept)
        return self._execute("network.removeIntercept", params=params, result=None)

    def set_cache_behavior(
        self,
        cache_behavior: SetCacheBehaviorParametersCacheBehavior,
        contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute network.setCacheBehavior (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-setCacheBehavior
        """
        params = SetCacheBehaviorParameters(cache_behavior=cache_behavior, contexts=contexts)
        return self._execute("network.setCacheBehavior", params=params, result=None)

    def set_extra_headers(
        self,
        headers: list[Header],
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute network.setExtraHeaders (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-network-setExtraHeaders
        """
        params = SetExtraHeadersParameters(headers=headers, contexts=contexts, user_contexts=user_contexts)
        return self._execute("network.setExtraHeaders", params=params, result=None)
