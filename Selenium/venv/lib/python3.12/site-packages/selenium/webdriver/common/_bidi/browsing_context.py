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
    from selenium.webdriver.common._bidi.script import NodeRemoteValue, SerializationOptions, SharedReference
    from selenium.webdriver.common._bidi.session import UserPromptHandlerType


@register("browsingContext.ReadinessState")
class ReadinessState(str, Enum):
    """browsingContext.ReadinessState.

    See https://w3c.github.io/webdriver-bidi/#type-browsingContext-ReadinessState
    """

    NONE = "none"
    INTERACTIVE = "interactive"
    COMPLETE = "complete"


@register("browsingContext.UserPromptType")
class UserPromptType(str, Enum):
    """browsingContext.UserPromptType.

    See https://w3c.github.io/webdriver-bidi/#type-browsingContext-UserPromptType
    """

    ALERT = "alert"
    BEFOREUNLOAD = "beforeunload"
    CONFIRM = "confirm"
    PROMPT = "prompt"


@register("browsingContext.CreateType")
class CreateType(str, Enum):
    """browsingContext.CreateType.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcreatetype
    """

    TAB = "tab"
    WINDOW = "window"


@register("browsingContext.InnerTextLocatorMatchType")
class InnerTextLocatorMatchType(str, Enum):
    FULL = "full"
    PARTIAL = "partial"


@register("browsingContext.CaptureScreenshotParametersOrigin")
class CaptureScreenshotParametersOrigin(str, Enum):
    VIEWPORT = "viewport"
    DOCUMENT = "document"


@register("browsingContext.PrintParametersOrientation")
class PrintParametersOrientation(str, Enum):
    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"


@register("browsingContext.Info")
@dataclass(frozen=True)
class Info(Record):
    """browsingContext.Info.

    See https://w3c.github.io/webdriver-bidi/#type-browsingContext-Info
    """

    children: list[Info] | None = field(
        metadata=meta("children", required=True, nullable=True, ref="browsingContext.Info", is_list=True),
    )
    client_window: str = field(metadata=meta("clientWindow", required=True, primitive="str"))
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    original_opener: str | None = field(
        metadata=meta("originalOpener", required=True, nullable=True, primitive="str"),
    )
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    user_context: str = field(metadata=meta("userContext", required=True, primitive="str"))
    parent: str | None | UnsetType = field(default=UNSET, metadata=meta("parent", nullable=True, primitive="str"))


@register("browsingContext.AccessibilityLocator")
@dataclass(frozen=True)
class AccessibilityLocator(Record):
    """browsingContext.AccessibilityLocator.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextaccessibilitylocator
    """

    value: AccessibilityLocatorValue = field(
        metadata=meta("value", required=True, ref="browsingContext.AccessibilityLocatorValue"),
    )
    type: str = field(
        default="accessibility",
        init=False,
        metadata=meta("type", required=True, fixed="accessibility"),
    )


@register("browsingContext.CssLocator")
@dataclass(frozen=True)
class CssLocator(Record):
    """browsingContext.CssLocator.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcsslocator
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="css", init=False, metadata=meta("type", required=True, fixed="css"))


@register("browsingContext.ContextLocator")
@dataclass(frozen=True)
class ContextLocator(Record):
    """browsingContext.ContextLocator.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcontextlocator
    """

    value: ContextLocatorValue = field(
        metadata=meta("value", required=True, ref="browsingContext.ContextLocatorValue"),
    )
    type: str = field(default="context", init=False, metadata=meta("type", required=True, fixed="context"))


@register("browsingContext.InnerTextLocator")
@dataclass(frozen=True)
class InnerTextLocator(Record):
    """browsingContext.InnerTextLocator.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextinnertextlocator
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="innerText", init=False, metadata=meta("type", required=True, fixed="innerText"))
    ignore_case: bool | UnsetType = field(default=UNSET, metadata=meta("ignoreCase", primitive="bool"))
    match_type: InnerTextLocatorMatchType | UnsetType = field(
        default=UNSET,
        metadata=meta("matchType", enum="browsingContext.InnerTextLocatorMatchType"),
    )
    max_depth: int | UnsetType = field(default=UNSET, metadata=meta("maxDepth", primitive="int"))


@register("browsingContext.XPathLocator")
@dataclass(frozen=True)
class XPathLocator(Record):
    """browsingContext.XPathLocator.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextxpathlocator
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="xpath", init=False, metadata=meta("type", required=True, fixed="xpath"))


@register("browsingContext.BaseNavigationInfo")
@dataclass(frozen=True)
class BaseNavigationInfo(Record):
    """browsingContext.BaseNavigationInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextbasenavigationinfo
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.NavigationInfo")
@dataclass(frozen=True)
class NavigationInfo(Record):
    """browsingContext.NavigationInfo.

    See https://w3c.github.io/webdriver-bidi/#type-browsingContext-NavigationInfo
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.ActivateParameters")
@dataclass(frozen=True)
class ActivateParameters(Record):
    """browsingContext.ActivateParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextactivateparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))


@register("browsingContext.CaptureScreenshotParameters")
@dataclass(frozen=True)
class CaptureScreenshotParameters(Record):
    """browsingContext.CaptureScreenshotParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcapturescreenshotparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    origin: CaptureScreenshotParametersOrigin | UnsetType = field(
        default=UNSET,
        metadata=meta("origin", enum="browsingContext.CaptureScreenshotParametersOrigin"),
    )
    format: ImageFormat | UnsetType = field(
        default=UNSET,
        metadata=meta("format", ref="browsingContext.ImageFormat"),
    )
    clip: ClipRectangleValue | UnsetType = field(
        default=UNSET,
        metadata=meta("clip", ref="browsingContext.ClipRectangle"),
    )
    image_size: ImageSize | UnsetType = field(
        default=UNSET,
        metadata=meta("imageSize", ref="browsingContext.ImageSize"),
    )


@register("browsingContext.ImageFormat")
@dataclass(frozen=True)
class ImageFormat(Record):
    """browsingContext.ImageFormat.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextimageformat
    """

    type: str = field(metadata=meta("type", required=True, primitive="str"))
    quality: float | UnsetType = field(default=UNSET, metadata=meta("quality", primitive="float"))


@register("browsingContext.ImageSize")
@dataclass(frozen=True)
class ImageSize(Record):
    """browsingContext.ImageSize.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextimagesize
    """

    max_width: int | UnsetType = field(default=UNSET, metadata=meta("maxWidth", primitive="int"))
    max_height: int | UnsetType = field(default=UNSET, metadata=meta("maxHeight", primitive="int"))


@register("browsingContext.ElementClipRectangle")
@dataclass(frozen=True)
class ElementClipRectangle(Record):
    """browsingContext.ElementClipRectangle.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextelementcliprectangle
    """

    element: SharedReference = field(metadata=meta("element", required=True, ref="script.SharedReference"))
    type: str = field(default="element", init=False, metadata=meta("type", required=True, fixed="element"))


@register("browsingContext.BoxClipRectangle")
@dataclass(frozen=True)
class BoxClipRectangle(Record):
    """browsingContext.BoxClipRectangle.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextboxcliprectangle
    """

    x: float = field(metadata=meta("x", required=True, primitive="float"))
    y: float = field(metadata=meta("y", required=True, primitive="float"))
    width: float = field(metadata=meta("width", required=True, primitive="float"))
    height: float = field(metadata=meta("height", required=True, primitive="float"))
    type: str = field(default="box", init=False, metadata=meta("type", required=True, fixed="box"))


@register("browsingContext.CaptureScreenshotResult")
@dataclass(frozen=True)
class CaptureScreenshotResult(Record):
    """browsingContext.CaptureScreenshotResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcapturescreenshotresult
    """

    data: str = field(metadata=meta("data", required=True, primitive="str"))


@register("browsingContext.CloseParameters")
@dataclass(frozen=True)
class CloseParameters(Record):
    """browsingContext.CloseParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcloseparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    prompt_unload: bool | UnsetType = field(default=UNSET, metadata=meta("promptUnload", primitive="bool"))


@register("browsingContext.CreateParameters")
@dataclass(frozen=True)
class CreateParameters(Record):
    """browsingContext.CreateParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcreateparameters
    """

    type: CreateType = field(metadata=meta("type", required=True, enum="browsingContext.CreateType"))
    reference_context: str | UnsetType = field(default=UNSET, metadata=meta("referenceContext", primitive="str"))
    background: bool | UnsetType = field(default=UNSET, metadata=meta("background", primitive="bool"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.CreateResult")
@dataclass(frozen=True)
class CreateResult(Record):
    """browsingContext.CreateResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcreateresult
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.GetTreeParameters")
@dataclass(frozen=True)
class GetTreeParameters(Record):
    """browsingContext.GetTreeParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextgettreeparameters
    """

    max_depth: int | UnsetType = field(default=UNSET, metadata=meta("maxDepth", primitive="int"))
    root: str | UnsetType = field(default=UNSET, metadata=meta("root", primitive="str"))


@register("browsingContext.GetTreeResult")
@dataclass(frozen=True)
class GetTreeResult(Record):
    """browsingContext.GetTreeResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextgettreeresult
    """

    contexts: list[Info] = field(metadata=meta("contexts", required=True, ref="browsingContext.Info", is_list=True))


@register("browsingContext.HandleUserPromptParameters")
@dataclass(frozen=True)
class HandleUserPromptParameters(Record):
    """browsingContext.HandleUserPromptParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontexthandleuserpromptparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    accept: bool | UnsetType = field(default=UNSET, metadata=meta("accept", primitive="bool"))
    user_text: str | UnsetType = field(default=UNSET, metadata=meta("userText", primitive="str"))


@register("browsingContext.LocateNodesParameters")
@dataclass(frozen=True)
class LocateNodesParameters(Record):
    """browsingContext.LocateNodesParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextlocatenodesparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    locator: LocatorValue = field(metadata=meta("locator", required=True, ref="browsingContext.Locator"))
    max_node_count: int | UnsetType = field(default=UNSET, metadata=meta("maxNodeCount", primitive="int"))
    serialization_options: SerializationOptions | UnsetType = field(
        default=UNSET,
        metadata=meta("serializationOptions", ref="script.SerializationOptions"),
    )
    start_nodes: list[SharedReference] | UnsetType = field(
        default=UNSET,
        metadata=meta("startNodes", ref="script.SharedReference", is_list=True),
    )


@register("browsingContext.LocateNodesResult")
@dataclass(frozen=True)
class LocateNodesResult(Record):
    """browsingContext.LocateNodesResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextlocatenodesresult
    """

    nodes: list[NodeRemoteValue] = field(
        metadata=meta("nodes", required=True, ref="script.NodeRemoteValue", is_list=True),
    )


@register("browsingContext.NavigateParameters")
@dataclass(frozen=True)
class NavigateParameters(Record):
    """browsingContext.NavigateParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextnavigateparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    wait: ReadinessState | UnsetType = field(
        default=UNSET,
        metadata=meta("wait", enum="browsingContext.ReadinessState"),
    )


@register("browsingContext.NavigateResult")
@dataclass(frozen=True)
class NavigateResult(Record):
    """browsingContext.NavigateResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextnavigateresult
    """

    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))


@register("browsingContext.PrintParameters")
@dataclass(frozen=True)
class PrintParameters(Record):
    """browsingContext.PrintParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextprintparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    background: bool | UnsetType = field(default=UNSET, metadata=meta("background", primitive="bool"))
    margin: PrintMarginParameters | UnsetType = field(
        default=UNSET,
        metadata=meta("margin", ref="browsingContext.PrintMarginParameters"),
    )
    orientation: PrintParametersOrientation | UnsetType = field(
        default=UNSET,
        metadata=meta("orientation", enum="browsingContext.PrintParametersOrientation"),
    )
    page: PrintPageParameters | UnsetType = field(
        default=UNSET,
        metadata=meta("page", ref="browsingContext.PrintPageParameters"),
    )
    page_ranges: list[Any] | UnsetType = field(default=UNSET, metadata=meta("pageRanges", is_list=True))
    scale: float | UnsetType = field(default=UNSET, metadata=meta("scale", primitive="float"))
    shrink_to_fit: bool | UnsetType = field(default=UNSET, metadata=meta("shrinkToFit", primitive="bool"))


@register("browsingContext.PrintMarginParameters")
@dataclass(frozen=True)
class PrintMarginParameters(Record):
    """browsingContext.PrintMarginParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextprintmarginparameters
    """

    bottom: float | UnsetType = field(default=UNSET, metadata=meta("bottom", primitive="float"))
    left: float | UnsetType = field(default=UNSET, metadata=meta("left", primitive="float"))
    right: float | UnsetType = field(default=UNSET, metadata=meta("right", primitive="float"))
    top: float | UnsetType = field(default=UNSET, metadata=meta("top", primitive="float"))


@register("browsingContext.PrintPageParameters")
@dataclass(frozen=True)
class PrintPageParameters(Record):
    """browsingContext.PrintPageParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextprintpageparameters
    """

    height: float | UnsetType = field(default=UNSET, metadata=meta("height", primitive="float"))
    width: float | UnsetType = field(default=UNSET, metadata=meta("width", primitive="float"))


@register("browsingContext.PrintResult")
@dataclass(frozen=True)
class PrintResult(Record):
    """browsingContext.PrintResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextprintresult
    """

    data: str = field(metadata=meta("data", required=True, primitive="str"))


@register("browsingContext.ReloadParameters")
@dataclass(frozen=True)
class ReloadParameters(Record):
    """browsingContext.ReloadParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextreloadparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    ignore_cache: bool | UnsetType = field(default=UNSET, metadata=meta("ignoreCache", primitive="bool"))
    wait: ReadinessState | UnsetType = field(
        default=UNSET,
        metadata=meta("wait", enum="browsingContext.ReadinessState"),
    )


@register("browsingContext.SetBypassCSPParameters")
@dataclass(frozen=True)
class SetBypassCSPParameters(Record):
    """browsingContext.SetBypassCSPParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextsetbypasscspparameters
    """

    bypass: bool | None = field(metadata=meta("bypass", required=True, nullable=True, fixed=True))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("browsingContext.SetViewportParameters")
@dataclass(frozen=True)
class SetViewportParameters(Record):
    """browsingContext.SetViewportParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextsetviewportparameters
    """

    context: str | UnsetType = field(default=UNSET, metadata=meta("context", primitive="str"))
    viewport: Viewport | None | UnsetType = field(
        default=UNSET,
        metadata=meta("viewport", nullable=True, ref="browsingContext.Viewport"),
    )
    device_pixel_ratio: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("devicePixelRatio", nullable=True, primitive="float"),
    )
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("browsingContext.Viewport")
@dataclass(frozen=True)
class Viewport(Record):
    """browsingContext.Viewport.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextviewport
    """

    width: int = field(metadata=meta("width", required=True, primitive="int"))
    height: int = field(metadata=meta("height", required=True, primitive="int"))


@register("browsingContext.StartScreencastParameters")
@dataclass(frozen=True)
class StartScreencastParameters(Record):
    """browsingContext.StartScreencastParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextstartscreencastparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    mime_type: str | UnsetType = field(default=UNSET, metadata=meta("mimeType", primitive="str"))
    video: MediaTrackConstraints | UnsetType = field(
        default=UNSET,
        metadata=meta("video", ref="browsingContext.MediaTrackConstraints"),
    )
    audio: bool | UnsetType = field(default=UNSET, metadata=meta("audio", primitive="bool"))


@register("browsingContext.MediaTrackConstraints")
@dataclass(frozen=True)
class MediaTrackConstraints(Record):
    """browsingContext.MediaTrackConstraints.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextmediatrackconstraints
    """

    width: int | UnsetType = field(default=UNSET, metadata=meta("width", primitive="int"))
    height: int | UnsetType = field(default=UNSET, metadata=meta("height", primitive="int"))
    frame_rate: int | UnsetType = field(default=UNSET, metadata=meta("frameRate", primitive="int"))


@register("browsingContext.StartScreencastResult")
@dataclass(frozen=True)
class StartScreencastResult(Record):
    """browsingContext.StartScreencastResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextstartscreencastresult
    """

    screencast: str = field(metadata=meta("screencast", required=True, primitive="str"))
    path: str = field(metadata=meta("path", required=True, primitive="str"))


@register("browsingContext.StopScreencastParameters")
@dataclass(frozen=True)
class StopScreencastParameters(Record):
    """browsingContext.StopScreencastParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextstopscreencastparameters
    """

    screencast: str = field(metadata=meta("screencast", required=True, primitive="str"))


@register("browsingContext.StopScreencastResult")
@dataclass(frozen=True)
class StopScreencastResult(Record):
    """browsingContext.StopScreencastResult.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextstopscreencastresult
    """

    path: str = field(metadata=meta("path", required=True, primitive="str"))
    error: str | UnsetType = field(default=UNSET, metadata=meta("error", primitive="str"))


@register("browsingContext.TraverseHistoryParameters")
@dataclass(frozen=True)
class TraverseHistoryParameters(Record):
    """browsingContext.TraverseHistoryParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontexttraversehistoryparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    delta: int = field(metadata=meta("delta", required=True, primitive="int"))


@register("browsingContext.HistoryUpdatedParameters")
@dataclass(frozen=True)
class HistoryUpdatedParameters(Record):
    """browsingContext.HistoryUpdatedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontexthistoryupdatedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.DownloadWillBeginParams")
@dataclass(frozen=True)
class DownloadWillBeginParams(Record):
    """browsingContext.DownloadWillBeginParams.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextdownloadwillbeginparams
    """

    download: str = field(metadata=meta("download", required=True, primitive="str"))
    suggested_filename: str = field(metadata=meta("suggestedFilename", required=True, primitive="str"))
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.UserPromptClosedParameters")
@dataclass(frozen=True)
class UserPromptClosedParameters(Record):
    """browsingContext.UserPromptClosedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextuserpromptclosedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    accepted: bool = field(metadata=meta("accepted", required=True, primitive="bool"))
    type: UserPromptType = field(metadata=meta("type", required=True, enum="browsingContext.UserPromptType"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    user_text: str | UnsetType = field(default=UNSET, metadata=meta("userText", primitive="str"))


@register("browsingContext.UserPromptOpenedParameters")
@dataclass(frozen=True)
class UserPromptOpenedParameters(Record):
    """browsingContext.UserPromptOpenedParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextuserpromptopenedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    handler: UserPromptHandlerType = field(
        metadata=meta("handler", required=True, enum="session.UserPromptHandlerType"),
    )
    message: str = field(metadata=meta("message", required=True, primitive="str"))
    type: UserPromptType = field(metadata=meta("type", required=True, enum="browsingContext.UserPromptType"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    default_value: str | UnsetType = field(default=UNSET, metadata=meta("defaultValue", primitive="str"))


@register("browsingContext.DownloadEndParams_CanceledParams")
@dataclass(frozen=True)
class DownloadEndParamsCanceledParams(Record):
    download: str = field(metadata=meta("download", required=True, primitive="str"))
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    status: str = field(default="canceled", init=False, metadata=meta("status", required=True, fixed="canceled"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.DownloadEndParams_CompleteParams")
@dataclass(frozen=True)
class DownloadEndParamsCompleteParams(Record):
    download: str = field(metadata=meta("download", required=True, primitive="str"))
    filepath: str | None = field(metadata=meta("filepath", required=True, nullable=True, primitive="str"))
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    navigation: str | None = field(metadata=meta("navigation", required=True, nullable=True, primitive="str"))
    timestamp: int = field(metadata=meta("timestamp", required=True, primitive="int"))
    url: str = field(metadata=meta("url", required=True, primitive="str"))
    status: str = field(default="complete", init=False, metadata=meta("status", required=True, fixed="complete"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))


@register("browsingContext.AccessibilityLocatorValue")
@dataclass(frozen=True)
class AccessibilityLocatorValue(Record):
    name: str | UnsetType = field(default=UNSET, metadata=meta("name", primitive="str"))
    role: str | UnsetType = field(default=UNSET, metadata=meta("role", primitive="str"))


@register("browsingContext.ContextLocatorValue")
@dataclass(frozen=True)
class ContextLocatorValue(Record):
    context: str = field(metadata=meta("context", required=True, primitive="str"))


@register("browsingContext.Locator")
class Locator(Union):
    """browsingContext.Locator.

    See https://w3c.github.io/webdriver-bidi/#type-browsingContext-Locator
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "accessibility": "browsingContext.AccessibilityLocator",
        "css": "browsingContext.CssLocator",
        "context": "browsingContext.ContextLocator",
        "innerText": "browsingContext.InnerTextLocator",
        "xpath": "browsingContext.XPathLocator",
    }
    _DISCRIMINATOR_VALUES = frozenset({"accessibility", "css", "context", "innerText", "xpath"})
    _OBJECT_ONLY = True


LocatorValue: TypeAlias = "AccessibilityLocator | CssLocator | ContextLocator | InnerTextLocator | XPathLocator"


@register("browsingContext.ClipRectangle")
class ClipRectangle(Union):
    """browsingContext.ClipRectangle.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextcliprectangle
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "box": "browsingContext.BoxClipRectangle",
        "element": "browsingContext.ElementClipRectangle",
    }
    _DISCRIMINATOR_VALUES = frozenset({"box", "element"})
    _OBJECT_ONLY = True


ClipRectangleValue: TypeAlias = "BoxClipRectangle | ElementClipRectangle"


@register("browsingContext.DownloadEndParams")
class DownloadEndParams(Union):
    """browsingContext.DownloadEndParams.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-browsingcontextdownloadendparams
    """

    _DISCRIMINATOR = "status"
    _VARIANTS = {
        "canceled": "browsingContext.DownloadEndParams_CanceledParams",
        "complete": "browsingContext.DownloadEndParams_CompleteParams",
    }
    _DISCRIMINATOR_VALUES = frozenset({"canceled", "complete"})
    _OBJECT_ONLY = True


DownloadEndParamsValue: TypeAlias = "DownloadEndParamsCanceledParams | DownloadEndParamsCompleteParams"


class BrowsingContext(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-browsingContext
    """

    EVENTS = {
        "context_created": "browsingContext.contextCreated",
        "context_destroyed": "browsingContext.contextDestroyed",
        "dom_content_loaded": "browsingContext.domContentLoaded",
        "download_end": "browsingContext.downloadEnd",
        "download_will_begin": "browsingContext.downloadWillBegin",
        "fragment_navigated": "browsingContext.fragmentNavigated",
        "history_updated": "browsingContext.historyUpdated",
        "load": "browsingContext.load",
        "navigation_aborted": "browsingContext.navigationAborted",
        "navigation_committed": "browsingContext.navigationCommitted",
        "navigation_failed": "browsingContext.navigationFailed",
        "navigation_started": "browsingContext.navigationStarted",
        "user_prompt_closed": "browsingContext.userPromptClosed",
        "user_prompt_opened": "browsingContext.userPromptOpened",
    }
    EVENT_TYPES = {
        "browsingContext.contextCreated": "browsingContext.Info",
        "browsingContext.contextDestroyed": "browsingContext.Info",
        "browsingContext.domContentLoaded": "browsingContext.NavigationInfo",
        "browsingContext.downloadEnd": "browsingContext.DownloadEndParams",
        "browsingContext.downloadWillBegin": "browsingContext.DownloadWillBeginParams",
        "browsingContext.fragmentNavigated": "browsingContext.NavigationInfo",
        "browsingContext.historyUpdated": "browsingContext.HistoryUpdatedParameters",
        "browsingContext.load": "browsingContext.NavigationInfo",
        "browsingContext.navigationAborted": "browsingContext.NavigationInfo",
        "browsingContext.navigationCommitted": "browsingContext.NavigationInfo",
        "browsingContext.navigationFailed": "browsingContext.NavigationInfo",
        "browsingContext.navigationStarted": "browsingContext.NavigationInfo",
        "browsingContext.userPromptClosed": "browsingContext.UserPromptClosedParameters",
        "browsingContext.userPromptOpened": "browsingContext.UserPromptOpenedParameters",
    }

    def activate(self, context: str) -> Any:
        """Execute browsingContext.activate (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-activate
        """
        params = ActivateParameters(context=context)
        return self._execute("browsingContext.activate", params=params, result=None)

    def capture_screenshot(
        self,
        context: str,
        origin: CaptureScreenshotParametersOrigin | UnsetType = UNSET,
        format: ImageFormat | UnsetType = UNSET,
        clip: ClipRectangleValue | UnsetType = UNSET,
        image_size: ImageSize | UnsetType = UNSET,
    ) -> CaptureScreenshotResult:
        """Execute browsingContext.captureScreenshot (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-captureScreenshot
        """
        params = CaptureScreenshotParameters(
            context=context,
            origin=origin,
            format=format,
            clip=clip,
            image_size=image_size,
        )
        return self._execute("browsingContext.captureScreenshot", params=params, result=CaptureScreenshotResult)

    def close(self, context: str, prompt_unload: bool | UnsetType = UNSET) -> Any:
        """Execute browsingContext.close (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-close
        """
        params = CloseParameters(context=context, prompt_unload=prompt_unload)
        return self._execute("browsingContext.close", params=params, result=None)

    def create(
        self,
        type: CreateType,
        reference_context: str | UnsetType = UNSET,
        background: bool | UnsetType = UNSET,
        user_context: str | UnsetType = UNSET,
    ) -> CreateResult:
        """Execute browsingContext.create (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-create
        """
        params = CreateParameters(
            type=type,
            reference_context=reference_context,
            background=background,
            user_context=user_context,
        )
        return self._execute("browsingContext.create", params=params, result=CreateResult)

    def get_tree(self, max_depth: int | UnsetType = UNSET, root: str | UnsetType = UNSET) -> GetTreeResult:
        """Execute browsingContext.getTree (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-getTree
        """
        params = GetTreeParameters(max_depth=max_depth, root=root)
        return self._execute("browsingContext.getTree", params=params, result=GetTreeResult)

    def handle_user_prompt(
        self,
        context: str,
        accept: bool | UnsetType = UNSET,
        user_text: str | UnsetType = UNSET,
    ) -> Any:
        """Execute browsingContext.handleUserPrompt (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-handleUserPrompt
        """
        params = HandleUserPromptParameters(context=context, accept=accept, user_text=user_text)
        return self._execute("browsingContext.handleUserPrompt", params=params, result=None)

    def locate_nodes(
        self,
        context: str,
        locator: LocatorValue,
        max_node_count: int | UnsetType = UNSET,
        serialization_options: SerializationOptions | UnsetType = UNSET,
        start_nodes: list[SharedReference] | UnsetType = UNSET,
    ) -> LocateNodesResult:
        """Execute browsingContext.locateNodes (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-locateNodes
        """
        params = LocateNodesParameters(
            context=context,
            locator=locator,
            max_node_count=max_node_count,
            serialization_options=serialization_options,
            start_nodes=start_nodes,
        )
        return self._execute("browsingContext.locateNodes", params=params, result=LocateNodesResult)

    def navigate(self, context: str, url: str, wait: ReadinessState | UnsetType = UNSET) -> NavigateResult:
        """Execute browsingContext.navigate (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-navigate
        """
        params = NavigateParameters(context=context, url=url, wait=wait)
        return self._execute("browsingContext.navigate", params=params, result=NavigateResult)

    def print(
        self,
        context: str,
        background: bool | UnsetType = UNSET,
        margin: PrintMarginParameters | UnsetType = UNSET,
        orientation: PrintParametersOrientation | UnsetType = UNSET,
        page: PrintPageParameters | UnsetType = UNSET,
        page_ranges: list[Any] | UnsetType = UNSET,
        scale: float | UnsetType = UNSET,
        shrink_to_fit: bool | UnsetType = UNSET,
    ) -> PrintResult:
        """Execute browsingContext.print (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-print
        """
        params = PrintParameters(
            context=context,
            background=background,
            margin=margin,
            orientation=orientation,
            page=page,
            page_ranges=page_ranges,
            scale=scale,
            shrink_to_fit=shrink_to_fit,
        )
        return self._execute("browsingContext.print", params=params, result=PrintResult)

    def reload(
        self,
        context: str,
        ignore_cache: bool | UnsetType = UNSET,
        wait: ReadinessState | UnsetType = UNSET,
    ) -> NavigateResult:
        """Execute browsingContext.reload (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-reload
        """
        params = ReloadParameters(context=context, ignore_cache=ignore_cache, wait=wait)
        return self._execute("browsingContext.reload", params=params, result=NavigateResult)

    def set_bypass_csp(
        self,
        bypass: bool | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute browsingContext.setBypassCSP (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-setBypassCSP
        """
        params = SetBypassCSPParameters(bypass=bypass, contexts=contexts, user_contexts=user_contexts)
        return self._execute("browsingContext.setBypassCSP", params=params, result=None)

    def set_viewport(
        self,
        context: str | UnsetType = UNSET,
        viewport: Viewport | None | UnsetType = UNSET,
        device_pixel_ratio: float | None | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute browsingContext.setViewport (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-setViewport
        """
        params = SetViewportParameters(
            context=context,
            viewport=viewport,
            device_pixel_ratio=device_pixel_ratio,
            user_contexts=user_contexts,
        )
        return self._execute("browsingContext.setViewport", params=params, result=None)

    def start_screencast(
        self,
        context: str,
        mime_type: str | UnsetType = UNSET,
        video: MediaTrackConstraints | UnsetType = UNSET,
        audio: bool | UnsetType = UNSET,
    ) -> StartScreencastResult:
        """Execute browsingContext.startScreencast (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-startScreencast
        """
        params = StartScreencastParameters(context=context, mime_type=mime_type, video=video, audio=audio)
        return self._execute("browsingContext.startScreencast", params=params, result=StartScreencastResult)

    def stop_screencast(self, screencast: str) -> StopScreencastResult:
        """Execute browsingContext.stopScreencast (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-stopScreencast
        """
        params = StopScreencastParameters(screencast=screencast)
        return self._execute("browsingContext.stopScreencast", params=params, result=StopScreencastResult)

    def traverse_history(self, context: str, delta: int) -> Any:
        """Execute browsingContext.traverseHistory (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-browsingContext-traverseHistory
        """
        params = TraverseHistoryParameters(context=context, delta=delta)
        return self._execute("browsingContext.traverseHistory", params=params, result=None)
