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


@register("script.SpecialNumber")
class SpecialNumber(str, Enum):
    """script.SpecialNumber.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptspecialnumber
    """

    NA_N = "NaN"
    NEG0 = "-0"
    INFINITY = "Infinity"
    NEG_INFINITY = "-Infinity"


@register("script.RealmType")
class RealmType(str, Enum):
    """script.RealmType.

    See https://w3c.github.io/webdriver-bidi/#type-script-RealmType
    """

    WINDOW = "window"
    DEDICATED_WORKER = "dedicated-worker"
    SHARED_WORKER = "shared-worker"
    SERVICE_WORKER = "service-worker"
    WORKER = "worker"
    PAINT_WORKLET = "paint-worklet"
    AUDIO_WORKLET = "audio-worklet"
    WORKLET = "worklet"


@register("script.ResultOwnership")
class ResultOwnership(str, Enum):
    """script.ResultOwnership.

    See https://w3c.github.io/webdriver-bidi/#type-script-ResultOwnership
    """

    ROOT = "root"
    NONE = "none"


@register("script.NodePropertiesMode")
class NodePropertiesMode(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


@register("script.SerializationOptionsIncludeShadowTree")
class SerializationOptionsIncludeShadowTree(str, Enum):
    NONE = "none"
    OPEN = "open"
    ALL = "all"


@register("script.ChannelValue")
@dataclass(frozen=True)
class ChannelValue(Record):
    """script.ChannelValue.

    See https://w3c.github.io/webdriver-bidi/#type-script-ChannelValue
    """

    value: ChannelProperties = field(metadata=meta("value", required=True, ref="script.ChannelProperties"))
    type: str = field(default="channel", init=False, metadata=meta("type", required=True, fixed="channel"))


@register("script.ChannelProperties")
@dataclass(frozen=True)
class ChannelProperties(Record):
    """script.ChannelProperties.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptchannelproperties
    """

    channel: str = field(metadata=meta("channel", required=True, primitive="str"))
    serialization_options: SerializationOptions | UnsetType = field(
        default=UNSET,
        metadata=meta("serializationOptions", ref="script.SerializationOptions"),
    )
    ownership: ResultOwnership | UnsetType = field(
        default=UNSET,
        metadata=meta("ownership", enum="script.ResultOwnership"),
    )


@register("script.EvaluateResultSuccess")
@dataclass(frozen=True)
class EvaluateResultSuccess(Record):
    """script.EvaluateResultSuccess.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptevaluateresultsuccess
    """

    result: RemoteValueValue = field(metadata=meta("result", required=True, ref="script.RemoteValue"))
    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    type: str = field(default="success", init=False, metadata=meta("type", required=True, fixed="success"))


@register("script.EvaluateResultException")
@dataclass(frozen=True)
class EvaluateResultException(Record):
    """script.EvaluateResultException.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptevaluateresultexception
    """

    exception_details: ExceptionDetails = field(
        metadata=meta("exceptionDetails", required=True, ref="script.ExceptionDetails"),
    )
    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    type: str = field(default="exception", init=False, metadata=meta("type", required=True, fixed="exception"))


@register("script.ExceptionDetails")
@dataclass(frozen=True)
class ExceptionDetails(Record):
    """script.ExceptionDetails.

    See https://w3c.github.io/webdriver-bidi/#type-script-ExceptionDetails
    """

    column_number: int = field(metadata=meta("columnNumber", required=True, primitive="int"))
    exception: RemoteValueValue = field(metadata=meta("exception", required=True, ref="script.RemoteValue"))
    line_number: int = field(metadata=meta("lineNumber", required=True, primitive="int"))
    stack_trace: StackTrace = field(metadata=meta("stackTrace", required=True, ref="script.StackTrace"))
    text: str = field(metadata=meta("text", required=True, primitive="str"))


@register("script.ArrayLocalValue")
@dataclass(frozen=True)
class ArrayLocalValue(Record):
    """script.ArrayLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptarraylocalvalue
    """

    value: list[LocalValueValue] = field(
        metadata=meta("value", required=True, ref="script.LocalValue", is_list=True),
    )
    type: str = field(default="array", init=False, metadata=meta("type", required=True, fixed="array"))


@register("script.DateLocalValue")
@dataclass(frozen=True)
class DateLocalValue(Record):
    """script.DateLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptdatelocalvalue
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="date", init=False, metadata=meta("type", required=True, fixed="date"))


@register("script.MapLocalValue")
@dataclass(frozen=True)
class MapLocalValue(Record):
    """script.MapLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptmaplocalvalue
    """

    value: list[list[Any]] = field(
        metadata=meta("value", required=True, ref="script.LocalValue", is_list=True, scalar="str"),
    )
    type: str = field(default="map", init=False, metadata=meta("type", required=True, fixed="map"))


@register("script.ObjectLocalValue")
@dataclass(frozen=True)
class ObjectLocalValue(Record):
    """script.ObjectLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptobjectlocalvalue
    """

    value: list[list[Any]] = field(
        metadata=meta("value", required=True, ref="script.LocalValue", is_list=True, scalar="str"),
    )
    type: str = field(default="object", init=False, metadata=meta("type", required=True, fixed="object"))


@register("script.RegExpValue")
@dataclass(frozen=True)
class RegExpValue(Record):
    """script.RegExpValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptregexpvalue
    """

    pattern: str = field(metadata=meta("pattern", required=True, primitive="str"))
    flags: str | UnsetType = field(default=UNSET, metadata=meta("flags", primitive="str"))


@register("script.RegExpLocalValue")
@dataclass(frozen=True)
class RegExpLocalValue(Record):
    """script.RegExpLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptregexplocalvalue
    """

    value: RegExpValue = field(metadata=meta("value", required=True, ref="script.RegExpValue"))
    type: str = field(default="regexp", init=False, metadata=meta("type", required=True, fixed="regexp"))


@register("script.SetLocalValue")
@dataclass(frozen=True)
class SetLocalValue(Record):
    """script.SetLocalValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptsetlocalvalue
    """

    value: list[LocalValueValue] = field(
        metadata=meta("value", required=True, ref="script.LocalValue", is_list=True),
    )
    type: str = field(default="set", init=False, metadata=meta("type", required=True, fixed="set"))


@register("script.UndefinedValue")
@dataclass(frozen=True)
class UndefinedValue(Record):
    """script.UndefinedValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptundefinedvalue
    """

    type: str = field(default="undefined", init=False, metadata=meta("type", required=True, fixed="undefined"))


@register("script.NullValue")
@dataclass(frozen=True)
class NullValue(Record):
    """script.NullValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptnullvalue
    """

    type: str = field(default="null", init=False, metadata=meta("type", required=True, fixed="null"))


@register("script.StringValue")
@dataclass(frozen=True)
class StringValue(Record):
    """script.StringValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptstringvalue
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="string", init=False, metadata=meta("type", required=True, fixed="string"))


@register("script.NumberValue")
@dataclass(frozen=True)
class NumberValue(Record):
    """script.NumberValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptnumbervalue
    """

    value: Any = field(metadata=meta("value", required=True))
    type: str = field(default="number", init=False, metadata=meta("type", required=True, fixed="number"))


@register("script.BooleanValue")
@dataclass(frozen=True)
class BooleanValue(Record):
    """script.BooleanValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptbooleanvalue
    """

    value: bool = field(metadata=meta("value", required=True, primitive="bool"))
    type: str = field(default="boolean", init=False, metadata=meta("type", required=True, fixed="boolean"))


@register("script.BigIntValue")
@dataclass(frozen=True)
class BigIntValue(Record):
    """script.BigIntValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptbigintvalue
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="bigint", init=False, metadata=meta("type", required=True, fixed="bigint"))


@register("script.BaseRealmInfo")
@dataclass(frozen=True)
class BaseRealmInfo(Record):
    """script.BaseRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptbaserealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))


@register("script.WindowRealmInfo")
@dataclass(frozen=True)
class WindowRealmInfo(Record):
    """script.WindowRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptwindowrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    type: str = field(default="window", init=False, metadata=meta("type", required=True, fixed="window"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    sandbox: str | UnsetType = field(default=UNSET, metadata=meta("sandbox", primitive="str"))


@register("script.DedicatedWorkerRealmInfo")
@dataclass(frozen=True)
class DedicatedWorkerRealmInfo(Record):
    """script.DedicatedWorkerRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptdedicatedworkerrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    owners: list[str] = field(metadata=meta("owners", required=True, is_list=True, primitive="str"))
    type: str = field(
        default="dedicated-worker",
        init=False,
        metadata=meta("type", required=True, fixed="dedicated-worker"),
    )


@register("script.SharedWorkerRealmInfo")
@dataclass(frozen=True)
class SharedWorkerRealmInfo(Record):
    """script.SharedWorkerRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptsharedworkerrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(
        default="shared-worker",
        init=False,
        metadata=meta("type", required=True, fixed="shared-worker"),
    )


@register("script.ServiceWorkerRealmInfo")
@dataclass(frozen=True)
class ServiceWorkerRealmInfo(Record):
    """script.ServiceWorkerRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptserviceworkerrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(
        default="service-worker",
        init=False,
        metadata=meta("type", required=True, fixed="service-worker"),
    )


@register("script.WorkerRealmInfo")
@dataclass(frozen=True)
class WorkerRealmInfo(Record):
    """script.WorkerRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptworkerrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(default="worker", init=False, metadata=meta("type", required=True, fixed="worker"))


@register("script.PaintWorkletRealmInfo")
@dataclass(frozen=True)
class PaintWorkletRealmInfo(Record):
    """script.PaintWorkletRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptpaintworkletrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(
        default="paint-worklet",
        init=False,
        metadata=meta("type", required=True, fixed="paint-worklet"),
    )


@register("script.AudioWorkletRealmInfo")
@dataclass(frozen=True)
class AudioWorkletRealmInfo(Record):
    """script.AudioWorkletRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptaudioworkletrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(
        default="audio-worklet",
        init=False,
        metadata=meta("type", required=True, fixed="audio-worklet"),
    )


@register("script.WorkletRealmInfo")
@dataclass(frozen=True)
class WorkletRealmInfo(Record):
    """script.WorkletRealmInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptworkletrealminfo
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    origin: str = field(metadata=meta("origin", required=True, primitive="str"))
    type: str = field(default="worklet", init=False, metadata=meta("type", required=True, fixed="worklet"))


@register("script.SharedReference")
@dataclass(frozen=True)
class SharedReference(Record):
    """script.SharedReference.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptsharedreference
    """

    _EXTENSIBLE = True
    shared_id: str = field(metadata=meta("sharedId", required=True, primitive="str"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("script.RemoteObjectReference")
@dataclass(frozen=True)
class RemoteObjectReference(Record):
    """script.RemoteObjectReference.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptremoteobjectreference
    """

    _EXTENSIBLE = True
    handle: str = field(metadata=meta("handle", required=True, primitive="str"))
    shared_id: str | UnsetType = field(default=UNSET, metadata=meta("sharedId", primitive="str"))
    extensions: dict[str, Any] | UnsetType = field(default=UNSET, metadata=meta("extensions"))


@register("script.SymbolRemoteValue")
@dataclass(frozen=True)
class SymbolRemoteValue(Record):
    """script.SymbolRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptsymbolremotevalue
    """

    type: str = field(default="symbol", init=False, metadata=meta("type", required=True, fixed="symbol"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.ArrayRemoteValue")
@dataclass(frozen=True)
class ArrayRemoteValue(Record):
    """script.ArrayRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptarrayremotevalue
    """

    type: str = field(default="array", init=False, metadata=meta("type", required=True, fixed="array"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[RemoteValueValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True),
    )


@register("script.ObjectRemoteValue")
@dataclass(frozen=True)
class ObjectRemoteValue(Record):
    """script.ObjectRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptobjectremotevalue
    """

    type: str = field(default="object", init=False, metadata=meta("type", required=True, fixed="object"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[list[Any]] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True, scalar="str"),
    )


@register("script.FunctionRemoteValue")
@dataclass(frozen=True)
class FunctionRemoteValue(Record):
    """script.FunctionRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptfunctionremotevalue
    """

    type: str = field(default="function", init=False, metadata=meta("type", required=True, fixed="function"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.RegExpRemoteValue")
@dataclass(frozen=True)
class RegExpRemoteValue(Record):
    """script.RegExpRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptregexpremotevalue
    """

    value: RegExpValue = field(metadata=meta("value", required=True, ref="script.RegExpValue"))
    type: str = field(default="regexp", init=False, metadata=meta("type", required=True, fixed="regexp"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.DateRemoteValue")
@dataclass(frozen=True)
class DateRemoteValue(Record):
    """script.DateRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptdateremotevalue
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="date", init=False, metadata=meta("type", required=True, fixed="date"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.MapRemoteValue")
@dataclass(frozen=True)
class MapRemoteValue(Record):
    """script.MapRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptmapremotevalue
    """

    type: str = field(default="map", init=False, metadata=meta("type", required=True, fixed="map"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[list[Any]] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True, scalar="str"),
    )


@register("script.SetRemoteValue")
@dataclass(frozen=True)
class SetRemoteValue(Record):
    """script.SetRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptsetremotevalue
    """

    type: str = field(default="set", init=False, metadata=meta("type", required=True, fixed="set"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[RemoteValueValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True),
    )


@register("script.WeakMapRemoteValue")
@dataclass(frozen=True)
class WeakMapRemoteValue(Record):
    """script.WeakMapRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptweakmapremotevalue
    """

    type: str = field(default="weakmap", init=False, metadata=meta("type", required=True, fixed="weakmap"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.WeakSetRemoteValue")
@dataclass(frozen=True)
class WeakSetRemoteValue(Record):
    """script.WeakSetRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptweaksetremotevalue
    """

    type: str = field(default="weakset", init=False, metadata=meta("type", required=True, fixed="weakset"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.GeneratorRemoteValue")
@dataclass(frozen=True)
class GeneratorRemoteValue(Record):
    """script.GeneratorRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptgeneratorremotevalue
    """

    type: str = field(default="generator", init=False, metadata=meta("type", required=True, fixed="generator"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.ErrorRemoteValue")
@dataclass(frozen=True)
class ErrorRemoteValue(Record):
    """script.ErrorRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scripterrorremotevalue
    """

    type: str = field(default="error", init=False, metadata=meta("type", required=True, fixed="error"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.ProxyRemoteValue")
@dataclass(frozen=True)
class ProxyRemoteValue(Record):
    """script.ProxyRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptproxyremotevalue
    """

    type: str = field(default="proxy", init=False, metadata=meta("type", required=True, fixed="proxy"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.PromiseRemoteValue")
@dataclass(frozen=True)
class PromiseRemoteValue(Record):
    """script.PromiseRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptpromiseremotevalue
    """

    type: str = field(default="promise", init=False, metadata=meta("type", required=True, fixed="promise"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.TypedArrayRemoteValue")
@dataclass(frozen=True)
class TypedArrayRemoteValue(Record):
    """script.TypedArrayRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scripttypedarrayremotevalue
    """

    type: str = field(default="typedarray", init=False, metadata=meta("type", required=True, fixed="typedarray"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.ArrayBufferRemoteValue")
@dataclass(frozen=True)
class ArrayBufferRemoteValue(Record):
    """script.ArrayBufferRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptarraybufferremotevalue
    """

    type: str = field(default="arraybuffer", init=False, metadata=meta("type", required=True, fixed="arraybuffer"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.NodeListRemoteValue")
@dataclass(frozen=True)
class NodeListRemoteValue(Record):
    """script.NodeListRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptnodelistremotevalue
    """

    type: str = field(default="nodelist", init=False, metadata=meta("type", required=True, fixed="nodelist"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[RemoteValueValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True),
    )


@register("script.HTMLCollectionRemoteValue")
@dataclass(frozen=True)
class HTMLCollectionRemoteValue(Record):
    """script.HTMLCollectionRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scripthtmlcollectionremotevalue
    """

    type: str = field(
        default="htmlcollection",
        init=False,
        metadata=meta("type", required=True, fixed="htmlcollection"),
    )
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: list[RemoteValueValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("value", ref="script.RemoteValue", is_list=True),
    )


@register("script.NodeRemoteValue")
@dataclass(frozen=True)
class NodeRemoteValue(Record):
    """script.NodeRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptnoderemotevalue
    """

    type: str = field(default="node", init=False, metadata=meta("type", required=True, fixed="node"))
    shared_id: str | UnsetType = field(default=UNSET, metadata=meta("sharedId", primitive="str"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))
    value: NodeProperties | UnsetType = field(default=UNSET, metadata=meta("value", ref="script.NodeProperties"))


@register("script.NodeProperties")
@dataclass(frozen=True)
class NodeProperties(Record):
    """script.NodeProperties.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptnodeproperties
    """

    node_type: int = field(metadata=meta("nodeType", required=True, primitive="int"))
    child_node_count: int = field(metadata=meta("childNodeCount", required=True, primitive="int"))
    attributes: Any | UnsetType = field(default=UNSET, metadata=meta("attributes"))
    children: list[NodeRemoteValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("children", ref="script.NodeRemoteValue", is_list=True),
    )
    local_name: str | UnsetType = field(default=UNSET, metadata=meta("localName", primitive="str"))
    mode: NodePropertiesMode | UnsetType = field(
        default=UNSET,
        metadata=meta("mode", enum="script.NodePropertiesMode"),
    )
    namespace_uri: str | UnsetType = field(default=UNSET, metadata=meta("namespaceURI", primitive="str"))
    node_value: str | UnsetType = field(default=UNSET, metadata=meta("nodeValue", primitive="str"))
    shadow_root: NodeRemoteValue | None | UnsetType = field(
        default=UNSET,
        metadata=meta("shadowRoot", nullable=True, ref="script.NodeRemoteValue"),
    )


@register("script.WindowProxyRemoteValue")
@dataclass(frozen=True)
class WindowProxyRemoteValue(Record):
    """script.WindowProxyRemoteValue.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptwindowproxyremotevalue
    """

    value: WindowProxyProperties = field(metadata=meta("value", required=True, ref="script.WindowProxyProperties"))
    type: str = field(default="window", init=False, metadata=meta("type", required=True, fixed="window"))
    handle: str | UnsetType = field(default=UNSET, metadata=meta("handle", primitive="str"))
    internal_id: str | UnsetType = field(default=UNSET, metadata=meta("internalId", primitive="str"))


@register("script.WindowProxyProperties")
@dataclass(frozen=True)
class WindowProxyProperties(Record):
    """script.WindowProxyProperties.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptwindowproxyproperties
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))


@register("script.SerializationOptions")
@dataclass(frozen=True)
class SerializationOptions(Record):
    """script.SerializationOptions.

    See https://w3c.github.io/webdriver-bidi/#type-script-SerializationOptions
    """

    max_dom_depth: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("maxDomDepth", nullable=True, primitive="int"),
    )
    max_object_depth: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("maxObjectDepth", nullable=True, primitive="int"),
    )
    include_shadow_tree: SerializationOptionsIncludeShadowTree | UnsetType = field(
        default=UNSET,
        metadata=meta("includeShadowTree", enum="script.SerializationOptionsIncludeShadowTree"),
    )


@register("script.StackFrame")
@dataclass(frozen=True)
class StackFrame(Record):
    """script.StackFrame.

    See https://w3c.github.io/webdriver-bidi/#type-script-StackFrame
    """

    column_number: int = field(metadata=meta("columnNumber", required=True, primitive="int"))
    function_name: str = field(metadata=meta("functionName", required=True, primitive="str"))
    line_number: int = field(metadata=meta("lineNumber", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))


@register("script.StackTrace")
@dataclass(frozen=True)
class StackTrace(Record):
    """script.StackTrace.

    See https://w3c.github.io/webdriver-bidi/#type-script-StackTrace
    """

    call_frames: list[StackFrame] = field(
        metadata=meta("callFrames", required=True, ref="script.StackFrame", is_list=True),
    )


@register("script.Source")
@dataclass(frozen=True)
class Source(Record):
    """script.Source.

    See https://w3c.github.io/webdriver-bidi/#type-script-Source
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))
    context: str | UnsetType = field(default=UNSET, metadata=meta("context", primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("script.RealmTarget")
@dataclass(frozen=True)
class RealmTarget(Record):
    """script.RealmTarget.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptrealmtarget
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))


@register("script.ContextTarget")
@dataclass(frozen=True)
class ContextTarget(Record):
    """script.ContextTarget.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptcontexttarget
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    sandbox: str | UnsetType = field(default=UNSET, metadata=meta("sandbox", primitive="str"))


@register("script.AddPreloadScriptParameters")
@dataclass(frozen=True)
class AddPreloadScriptParameters(Record):
    """script.AddPreloadScriptParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptaddpreloadscriptparameters
    """

    function_declaration: str = field(metadata=meta("functionDeclaration", required=True, primitive="str"))
    arguments: list[ChannelValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("arguments", ref="script.ChannelValue", is_list=True),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )
    sandbox: str | UnsetType = field(default=UNSET, metadata=meta("sandbox", primitive="str"))


@register("script.AddPreloadScriptResult")
@dataclass(frozen=True)
class AddPreloadScriptResult(Record):
    """script.AddPreloadScriptResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptaddpreloadscriptresult
    """

    script: str = field(metadata=meta("script", required=True, primitive="str"))


@register("script.DisownParameters")
@dataclass(frozen=True)
class DisownParameters(Record):
    """script.DisownParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptdisownparameters
    """

    handles: list[str] = field(metadata=meta("handles", required=True, is_list=True, primitive="str"))
    target: TargetValue = field(metadata=meta("target", required=True, ref="script.Target"))


@register("script.CallFunctionParameters")
@dataclass(frozen=True)
class CallFunctionParameters(Record):
    """script.CallFunctionParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptcallfunctionparameters
    """

    function_declaration: str = field(metadata=meta("functionDeclaration", required=True, primitive="str"))
    await_promise: bool = field(metadata=meta("awaitPromise", required=True, primitive="bool"))
    target: TargetValue = field(metadata=meta("target", required=True, ref="script.Target"))
    arguments: list[LocalValueValue] | UnsetType = field(
        default=UNSET,
        metadata=meta("arguments", ref="script.LocalValue", is_list=True),
    )
    result_ownership: ResultOwnership | UnsetType = field(
        default=UNSET,
        metadata=meta("resultOwnership", enum="script.ResultOwnership"),
    )
    serialization_options: SerializationOptions | UnsetType = field(
        default=UNSET,
        metadata=meta("serializationOptions", ref="script.SerializationOptions"),
    )
    this: LocalValueValue | UnsetType = field(default=UNSET, metadata=meta("this", ref="script.LocalValue"))
    user_activation: bool | UnsetType = field(default=UNSET, metadata=meta("userActivation", primitive="bool"))


@register("script.EvaluateParameters")
@dataclass(frozen=True)
class EvaluateParameters(Record):
    """script.EvaluateParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptevaluateparameters
    """

    expression: str = field(metadata=meta("expression", required=True, primitive="str"))
    target: TargetValue = field(metadata=meta("target", required=True, ref="script.Target"))
    await_promise: bool = field(metadata=meta("awaitPromise", required=True, primitive="bool"))
    result_ownership: ResultOwnership | UnsetType = field(
        default=UNSET,
        metadata=meta("resultOwnership", enum="script.ResultOwnership"),
    )
    serialization_options: SerializationOptions | UnsetType = field(
        default=UNSET,
        metadata=meta("serializationOptions", ref="script.SerializationOptions"),
    )
    user_activation: bool | UnsetType = field(default=UNSET, metadata=meta("userActivation", primitive="bool"))


@register("script.GetRealmsParameters")
@dataclass(frozen=True)
class GetRealmsParameters(Record):
    """script.GetRealmsParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptgetrealmsparameters
    """

    context: str | UnsetType = field(default=UNSET, metadata=meta("context", primitive="str"))
    type: RealmType | UnsetType = field(default=UNSET, metadata=meta("type", enum="script.RealmType"))


@register("script.GetRealmsResult")
@dataclass(frozen=True)
class GetRealmsResult(Record):
    """script.GetRealmsResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptgetrealmsresult
    """

    realms: list[RealmInfoValue] = field(
        metadata=meta("realms", required=True, ref="script.RealmInfo", is_list=True),
    )


@register("script.RemovePreloadScriptParameters")
@dataclass(frozen=True)
class RemovePreloadScriptParameters(Record):
    """script.RemovePreloadScriptParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptremovepreloadscriptparameters
    """

    script: str = field(metadata=meta("script", required=True, primitive="str"))


@register("script.MessageParameters")
@dataclass(frozen=True)
class MessageParameters(Record):
    """script.MessageParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptmessageparameters
    """

    channel: str = field(metadata=meta("channel", required=True, primitive="str"))
    data: RemoteValueValue = field(metadata=meta("data", required=True, ref="script.RemoteValue"))
    source: Source = field(metadata=meta("source", required=True, ref="script.Source"))


@register("script.RealmDestroyedParameters")
@dataclass(frozen=True)
class RealmDestroyedParameters(Record):
    """script.RealmDestroyedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-scriptrealmdestroyedparameters
    """

    realm: str = field(metadata=meta("realm", required=True, primitive="str"))


@register("script.EvaluateResult")
class EvaluateResult(Union):
    """script.EvaluateResult.

    See https://w3c.github.io/webdriver-bidi/#type-script-EvaluateResult
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "success": "script.EvaluateResultSuccess",
        "exception": "script.EvaluateResultException",
    }
    _DISCRIMINATOR_VALUES = frozenset({"success", "exception"})
    _OBJECT_ONLY = True


EvaluateResultValue: TypeAlias = "EvaluateResultSuccess | EvaluateResultException"


@register("script.LocalValue")
class LocalValue(Union):
    """script.LocalValue.

    See https://w3c.github.io/webdriver-bidi/#type-script-LocalValue
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "undefined": "script.UndefinedValue",
        "null": "script.NullValue",
        "string": "script.StringValue",
        "number": "script.NumberValue",
        "boolean": "script.BooleanValue",
        "bigint": "script.BigIntValue",
        "channel": "script.ChannelValue",
        "array": "script.ArrayLocalValue",
        "date": "script.DateLocalValue",
        "map": "script.MapLocalValue",
        "object": "script.ObjectLocalValue",
        "regexp": "script.RegExpLocalValue",
        "set": "script.SetLocalValue",
    }
    _FALLBACK = "script.RemoteReference"
    _DISCRIMINATOR_VALUES = frozenset(
        {
            "undefined",
            "null",
            "string",
            "number",
            "boolean",
            "bigint",
            "channel",
            "array",
            "date",
            "map",
            "object",
            "regexp",
            "set",
        }
    )
    _OBJECT_ONLY = True


LocalValueValue: TypeAlias = (
    "UndefinedValue | NullValue | StringValue | NumberValue | BooleanValue | BigIntValue | ChannelValue"
    " | ArrayLocalValue | DateLocalValue | MapLocalValue | ObjectLocalValue | RegExpLocalValue | SetLocalValue"
    " | RemoteReferenceValue"
)


@register("script.PrimitiveProtocolValue")
class PrimitiveProtocolValue(Union):
    """script.PrimitiveProtocolValue.

    See https://w3c.github.io/webdriver-bidi/#type-script-PrimitiveProtocolValue
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "undefined": "script.UndefinedValue",
        "null": "script.NullValue",
        "string": "script.StringValue",
        "number": "script.NumberValue",
        "boolean": "script.BooleanValue",
        "bigint": "script.BigIntValue",
    }
    _DISCRIMINATOR_VALUES = frozenset({"undefined", "null", "string", "number", "boolean", "bigint"})
    _OBJECT_ONLY = True


PrimitiveProtocolValueValue: TypeAlias = (
    "UndefinedValue | NullValue | StringValue | NumberValue | BooleanValue | BigIntValue"
)


@register("script.RealmInfo")
class RealmInfo(Union):
    """script.RealmInfo.

    See https://w3c.github.io/webdriver-bidi/#type-script-RealmInfo
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "window": "script.WindowRealmInfo",
        "dedicated-worker": "script.DedicatedWorkerRealmInfo",
        "shared-worker": "script.SharedWorkerRealmInfo",
        "service-worker": "script.ServiceWorkerRealmInfo",
        "worker": "script.WorkerRealmInfo",
        "paint-worklet": "script.PaintWorkletRealmInfo",
        "audio-worklet": "script.AudioWorkletRealmInfo",
        "worklet": "script.WorkletRealmInfo",
    }
    _DISCRIMINATOR_VALUES = frozenset(
        {
            "window",
            "dedicated-worker",
            "shared-worker",
            "service-worker",
            "worker",
            "paint-worklet",
            "audio-worklet",
            "worklet",
        }
    )
    _OBJECT_ONLY = True


RealmInfoValue: TypeAlias = (
    "WindowRealmInfo | DedicatedWorkerRealmInfo | SharedWorkerRealmInfo | ServiceWorkerRealmInfo | WorkerRealmInfo"
    " | PaintWorkletRealmInfo | AudioWorkletRealmInfo | WorkletRealmInfo"
)


@register("script.RemoteReference")
class RemoteReference(Union):
    """script.RemoteReference.

    See https://w3c.github.io/webdriver-bidi/#type-script-RemoteReference
    """

    _PRESENCE = (("script.SharedReference", ("sharedId",)), ("script.RemoteObjectReference", ("handle",)))
    _OBJECT_ONLY = True


RemoteReferenceValue: TypeAlias = "SharedReference | RemoteObjectReference"


@register("script.RemoteValue")
class RemoteValue(Union):
    """script.RemoteValue.

    See https://w3c.github.io/webdriver-bidi/#type-script-RemoteValue
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "undefined": "script.UndefinedValue",
        "null": "script.NullValue",
        "string": "script.StringValue",
        "number": "script.NumberValue",
        "boolean": "script.BooleanValue",
        "bigint": "script.BigIntValue",
        "symbol": "script.SymbolRemoteValue",
        "array": "script.ArrayRemoteValue",
        "object": "script.ObjectRemoteValue",
        "function": "script.FunctionRemoteValue",
        "regexp": "script.RegExpRemoteValue",
        "date": "script.DateRemoteValue",
        "map": "script.MapRemoteValue",
        "set": "script.SetRemoteValue",
        "weakmap": "script.WeakMapRemoteValue",
        "weakset": "script.WeakSetRemoteValue",
        "generator": "script.GeneratorRemoteValue",
        "error": "script.ErrorRemoteValue",
        "proxy": "script.ProxyRemoteValue",
        "promise": "script.PromiseRemoteValue",
        "typedarray": "script.TypedArrayRemoteValue",
        "arraybuffer": "script.ArrayBufferRemoteValue",
        "nodelist": "script.NodeListRemoteValue",
        "htmlcollection": "script.HTMLCollectionRemoteValue",
        "node": "script.NodeRemoteValue",
        "window": "script.WindowProxyRemoteValue",
    }
    _DISCRIMINATOR_VALUES = frozenset(
        {
            "undefined",
            "null",
            "string",
            "number",
            "boolean",
            "bigint",
            "symbol",
            "array",
            "object",
            "function",
            "regexp",
            "date",
            "map",
            "set",
            "weakmap",
            "weakset",
            "generator",
            "error",
            "proxy",
            "promise",
            "typedarray",
            "arraybuffer",
            "nodelist",
            "htmlcollection",
            "node",
            "window",
        }
    )
    _OBJECT_ONLY = True


RemoteValueValue: TypeAlias = (
    "UndefinedValue | NullValue | StringValue | NumberValue | BooleanValue | BigIntValue | SymbolRemoteValue"
    " | ArrayRemoteValue | ObjectRemoteValue | FunctionRemoteValue | RegExpRemoteValue | DateRemoteValue"
    " | MapRemoteValue | SetRemoteValue | WeakMapRemoteValue | WeakSetRemoteValue | GeneratorRemoteValue"
    " | ErrorRemoteValue | ProxyRemoteValue | PromiseRemoteValue | TypedArrayRemoteValue | ArrayBufferRemoteValue"
    " | NodeListRemoteValue | HTMLCollectionRemoteValue | NodeRemoteValue | WindowProxyRemoteValue"
)


@register("script.Target")
class Target(Union):
    """script.Target.

    See https://w3c.github.io/webdriver-bidi/#type-script-Target
    """

    _PRESENCE = (("script.ContextTarget", ("context",)), ("script.RealmTarget", ("realm",)))
    _OBJECT_ONLY = True


TargetValue: TypeAlias = "ContextTarget | RealmTarget"


class Script(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-script
    """

    EVENTS = {
        "message": "script.message",
        "realm_created": "script.realmCreated",
        "realm_destroyed": "script.realmDestroyed",
    }
    EVENT_TYPES = {
        "script.message": "script.MessageParameters",
        "script.realmCreated": "script.RealmInfo",
        "script.realmDestroyed": "script.RealmDestroyedParameters",
    }

    def add_preload_script(
        self,
        function_declaration: str,
        arguments: list[ChannelValue] | UnsetType = UNSET,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
        sandbox: str | UnsetType = UNSET,
    ) -> AddPreloadScriptResult:
        """Execute script.addPreloadScript (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-addPreloadScript
        """
        params = AddPreloadScriptParameters(
            function_declaration=function_declaration,
            arguments=arguments,
            contexts=contexts,
            user_contexts=user_contexts,
            sandbox=sandbox,
        )
        return self._execute("script.addPreloadScript", params=params, result=AddPreloadScriptResult)

    def call_function(
        self,
        function_declaration: str,
        await_promise: bool,
        target: TargetValue,
        arguments: list[LocalValueValue] | UnsetType = UNSET,
        result_ownership: ResultOwnership | UnsetType = UNSET,
        serialization_options: SerializationOptions | UnsetType = UNSET,
        this: LocalValueValue | UnsetType = UNSET,
        user_activation: bool | UnsetType = UNSET,
    ) -> EvaluateResultValue:
        """Execute script.callFunction (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-callFunction
        """
        params = CallFunctionParameters(
            function_declaration=function_declaration,
            await_promise=await_promise,
            target=target,
            arguments=arguments,
            result_ownership=result_ownership,
            serialization_options=serialization_options,
            this=this,
            user_activation=user_activation,
        )
        return self._execute("script.callFunction", params=params, result=EvaluateResult)

    def disown(self, handles: list[str], target: TargetValue) -> Any:
        """Execute script.disown (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-disown
        """
        params = DisownParameters(handles=handles, target=target)
        return self._execute("script.disown", params=params, result=None)

    def evaluate(
        self,
        expression: str,
        target: TargetValue,
        await_promise: bool,
        result_ownership: ResultOwnership | UnsetType = UNSET,
        serialization_options: SerializationOptions | UnsetType = UNSET,
        user_activation: bool | UnsetType = UNSET,
    ) -> EvaluateResultValue:
        """Execute script.evaluate (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-evaluate
        """
        params = EvaluateParameters(
            expression=expression,
            target=target,
            await_promise=await_promise,
            result_ownership=result_ownership,
            serialization_options=serialization_options,
            user_activation=user_activation,
        )
        return self._execute("script.evaluate", params=params, result=EvaluateResult)

    def get_realms(self, context: str | UnsetType = UNSET, type: RealmType | UnsetType = UNSET) -> GetRealmsResult:
        """Execute script.getRealms (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-getRealms
        """
        params = GetRealmsParameters(context=context, type=type)
        return self._execute("script.getRealms", params=params, result=GetRealmsResult)

    def remove_preload_script(self, script: str) -> Any:
        """Execute script.removePreloadScript (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-script-removePreloadScript
        """
        params = RemovePreloadScriptParameters(script=script)
        return self._execute("script.removePreloadScript", params=params, result=None)
