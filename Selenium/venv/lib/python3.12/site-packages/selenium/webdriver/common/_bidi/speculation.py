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

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import Record, meta, register


@register("speculation.PreloadingStatus")
class PreloadingStatus(str, Enum):
    """speculation.PreloadingStatus.

    See https://wicg.github.io/nav-speculation/prefetch.html#cddl-type-speculationpreloadingstatus
    """

    PENDING = "pending"
    READY = "ready"
    SUCCESS = "success"
    FAILURE = "failure"


@register("speculation.PrefetchStatusUpdatedParameters")
@dataclass(frozen=True)
class PrefetchStatusUpdatedParameters(Record):
    """speculation.PrefetchStatusUpdatedParameters.

    See https://wicg.github.io/nav-speculation/prefetch.html#cddl-type-speculationprefetchstatusupdatedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    status: PreloadingStatus = field(metadata=meta("status", required=True, enum="speculation.PreloadingStatus"))


class Speculation(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    """

    EVENTS = {
        "prefetch_status_updated": "speculation.prefetchStatusUpdated",
    }
    EVENT_TYPES = {
        "speculation.prefetchStatusUpdated": "speculation.PrefetchStatusUpdatedParameters",
    }
