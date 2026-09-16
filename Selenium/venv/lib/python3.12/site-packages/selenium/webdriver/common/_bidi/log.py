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
from typing import TYPE_CHECKING, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register

if TYPE_CHECKING:
    from selenium.webdriver.common._bidi.script import RemoteValueValue, Source, StackTrace


@register("log.Level")
class Level(str, Enum):
    """log.Level.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-loglevel
    """

    DEBUG = "debug"
    INFO = "info"
    WARN = "warn"
    ERROR = "error"


@register("log.BaseLogEntry")
@dataclass(frozen=True)
class BaseLogEntry(Record):
    """log.BaseLogEntry.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-logbaselogentry
    """

    level: Level = field(metadata=meta("level", required=True, enum="log.Level"))
    source: Source = field(metadata=meta("source", required=True, ref="script.Source"))
    text: str | None = field(metadata=meta("text", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    stack_trace: StackTrace | UnsetType = field(default=UNSET, metadata=meta("stackTrace", ref="script.StackTrace"))


@register("log.GenericLogEntry")
@dataclass(frozen=True)
class GenericLogEntry(Record):
    """log.GenericLogEntry.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-loggenericlogentry
    """

    level: Level = field(metadata=meta("level", required=True, enum="log.Level"))
    source: Source = field(metadata=meta("source", required=True, ref="script.Source"))
    text: str | None = field(metadata=meta("text", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    type: str = field(metadata=meta("type", required=True, primitive="str"))
    stack_trace: StackTrace | UnsetType = field(default=UNSET, metadata=meta("stackTrace", ref="script.StackTrace"))


@register("log.ConsoleLogEntry")
@dataclass(frozen=True)
class ConsoleLogEntry(Record):
    """log.ConsoleLogEntry.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-logconsolelogentry
    """

    level: Level = field(metadata=meta("level", required=True, enum="log.Level"))
    source: Source = field(metadata=meta("source", required=True, ref="script.Source"))
    text: str | None = field(metadata=meta("text", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    method: str = field(metadata=meta("method", required=True, primitive="str"))
    args: list[RemoteValueValue] = field(
        metadata=meta("args", required=True, ref="script.RemoteValue", is_list=True),
    )
    type: str = field(default="console", init=False, metadata=meta("type", required=True, fixed="console"))
    stack_trace: StackTrace | UnsetType = field(default=UNSET, metadata=meta("stackTrace", ref="script.StackTrace"))


@register("log.JavascriptLogEntry")
@dataclass(frozen=True)
class JavascriptLogEntry(Record):
    """log.JavascriptLogEntry.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-logjavascriptlogentry
    """

    level: Level = field(metadata=meta("level", required=True, enum="log.Level"))
    source: Source = field(metadata=meta("source", required=True, ref="script.Source"))
    text: str | None = field(metadata=meta("text", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    type: str = field(default="javascript", init=False, metadata=meta("type", required=True, fixed="javascript"))
    stack_trace: StackTrace | UnsetType = field(default=UNSET, metadata=meta("stackTrace", ref="script.StackTrace"))


@register("log.Entry")
class Entry(Union):
    """log.Entry.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-logentry
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "console": "log.ConsoleLogEntry",
        "javascript": "log.JavascriptLogEntry",
    }
    _FALLBACK = "log.GenericLogEntry"
    _DISCRIMINATOR_VALUES = frozenset({"console", "javascript"})
    _OBJECT_ONLY = True


EntryValue: TypeAlias = "ConsoleLogEntry | JavascriptLogEntry | GenericLogEntry"


class Log(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-log
    """

    EVENTS = {
        "entry_added": "log.entryAdded",
    }
    EVENT_TYPES = {
        "log.entryAdded": "log.Entry",
    }
