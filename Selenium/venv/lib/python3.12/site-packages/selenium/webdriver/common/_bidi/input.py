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
from typing import TYPE_CHECKING, Any, Literal, TypeAlias

from selenium.webdriver.common._bidi.domain import Domain
from selenium.webdriver.common._bidi.serialization import UNSET, Record, Union, UnsetType, meta, register

if TYPE_CHECKING:
    from selenium.webdriver.common._bidi.script import SharedReference


@register("input.PointerType")
class PointerType(str, Enum):
    """input.PointerType.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointertype
    """

    MOUSE = "mouse"
    PEN = "pen"
    TOUCH = "touch"


@register("input.ElementOrigin")
@dataclass(frozen=True)
class ElementOrigin(Record):
    """input.ElementOrigin.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputelementorigin
    """

    element: SharedReference = field(metadata=meta("element", required=True, ref="script.SharedReference"))
    type: str = field(default="element", init=False, metadata=meta("type", required=True, fixed="element"))


@register("input.PerformActionsParameters")
@dataclass(frozen=True)
class PerformActionsParameters(Record):
    """input.PerformActionsParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputperformactionsparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    actions: list[SourceActionsValue] = field(
        metadata=meta("actions", required=True, ref="input.SourceActions", is_list=True),
    )


@register("input.NoneSourceActions")
@dataclass(frozen=True)
class NoneSourceActions(Record):
    """input.NoneSourceActions.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputnonesourceactions
    """

    id: str = field(metadata=meta("id", required=True, primitive="str"))
    actions: list[PauseAction] = field(
        metadata=meta("actions", required=True, ref="input.PauseAction", is_list=True),
    )
    type: str = field(default="none", init=False, metadata=meta("type", required=True, fixed="none"))


@register("input.KeySourceActions")
@dataclass(frozen=True)
class KeySourceActions(Record):
    """input.KeySourceActions.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputkeysourceactions
    """

    id: str = field(metadata=meta("id", required=True, primitive="str"))
    actions: list[KeySourceActionValue] = field(
        metadata=meta("actions", required=True, ref="input.KeySourceAction", is_list=True),
    )
    type: str = field(default="key", init=False, metadata=meta("type", required=True, fixed="key"))


@register("input.PointerSourceActions")
@dataclass(frozen=True)
class PointerSourceActions(Record):
    """input.PointerSourceActions.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointersourceactions
    """

    id: str = field(metadata=meta("id", required=True, primitive="str"))
    actions: list[PointerSourceActionValue] = field(
        metadata=meta("actions", required=True, ref="input.PointerSourceAction", is_list=True),
    )
    type: str = field(default="pointer", init=False, metadata=meta("type", required=True, fixed="pointer"))
    parameters: PointerParameters | UnsetType = field(
        default=UNSET,
        metadata=meta("parameters", ref="input.PointerParameters"),
    )


@register("input.PointerParameters")
@dataclass(frozen=True)
class PointerParameters(Record):
    """input.PointerParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointerparameters
    """

    pointer_type: PointerType | UnsetType = field(
        default=UNSET,
        metadata=meta("pointerType", enum="input.PointerType"),
    )


@register("input.WheelSourceActions")
@dataclass(frozen=True)
class WheelSourceActions(Record):
    """input.WheelSourceActions.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputwheelsourceactions
    """

    id: str = field(metadata=meta("id", required=True, primitive="str"))
    actions: list[WheelSourceActionValue] = field(
        metadata=meta("actions", required=True, ref="input.WheelSourceAction", is_list=True),
    )
    type: str = field(default="wheel", init=False, metadata=meta("type", required=True, fixed="wheel"))


@register("input.PauseAction")
@dataclass(frozen=True)
class PauseAction(Record):
    """input.PauseAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpauseaction
    """

    type: str = field(default="pause", init=False, metadata=meta("type", required=True, fixed="pause"))
    duration: int | UnsetType = field(default=UNSET, metadata=meta("duration", primitive="int"))


@register("input.KeyDownAction")
@dataclass(frozen=True)
class KeyDownAction(Record):
    """input.KeyDownAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputkeydownaction
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="keyDown", init=False, metadata=meta("type", required=True, fixed="keyDown"))


@register("input.KeyUpAction")
@dataclass(frozen=True)
class KeyUpAction(Record):
    """input.KeyUpAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputkeyupaction
    """

    value: str = field(metadata=meta("value", required=True, primitive="str"))
    type: str = field(default="keyUp", init=False, metadata=meta("type", required=True, fixed="keyUp"))


@register("input.PointerUpAction")
@dataclass(frozen=True)
class PointerUpAction(Record):
    """input.PointerUpAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointerupaction
    """

    button: int = field(metadata=meta("button", required=True, primitive="int"))
    type: str = field(default="pointerUp", init=False, metadata=meta("type", required=True, fixed="pointerUp"))


@register("input.PointerDownAction")
@dataclass(frozen=True)
class PointerDownAction(Record):
    """input.PointerDownAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointerdownaction
    """

    button: int = field(metadata=meta("button", required=True, primitive="int"))
    type: str = field(default="pointerDown", init=False, metadata=meta("type", required=True, fixed="pointerDown"))
    width: int | UnsetType = field(default=UNSET, metadata=meta("width", primitive="int"))
    height: int | UnsetType = field(default=UNSET, metadata=meta("height", primitive="int"))
    pressure: float | UnsetType = field(default=UNSET, metadata=meta("pressure", primitive="float"))
    tangential_pressure: float | UnsetType = field(
        default=UNSET,
        metadata=meta("tangentialPressure", primitive="float"),
    )
    twist: int | UnsetType = field(default=UNSET, metadata=meta("twist", primitive="int"))
    altitude_angle: float | UnsetType = field(default=UNSET, metadata=meta("altitudeAngle", primitive="float"))
    azimuth_angle: float | UnsetType = field(default=UNSET, metadata=meta("azimuthAngle", primitive="float"))


@register("input.PointerMoveAction")
@dataclass(frozen=True)
class PointerMoveAction(Record):
    """input.PointerMoveAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointermoveaction
    """

    x: float = field(metadata=meta("x", required=True, primitive="float"))
    y: float = field(metadata=meta("y", required=True, primitive="float"))
    type: str = field(default="pointerMove", init=False, metadata=meta("type", required=True, fixed="pointerMove"))
    duration: int | UnsetType = field(default=UNSET, metadata=meta("duration", primitive="int"))
    origin: OriginValue | UnsetType = field(default=UNSET, metadata=meta("origin", ref="input.Origin"))
    width: int | UnsetType = field(default=UNSET, metadata=meta("width", primitive="int"))
    height: int | UnsetType = field(default=UNSET, metadata=meta("height", primitive="int"))
    pressure: float | UnsetType = field(default=UNSET, metadata=meta("pressure", primitive="float"))
    tangential_pressure: float | UnsetType = field(
        default=UNSET,
        metadata=meta("tangentialPressure", primitive="float"),
    )
    twist: int | UnsetType = field(default=UNSET, metadata=meta("twist", primitive="int"))
    altitude_angle: float | UnsetType = field(default=UNSET, metadata=meta("altitudeAngle", primitive="float"))
    azimuth_angle: float | UnsetType = field(default=UNSET, metadata=meta("azimuthAngle", primitive="float"))


@register("input.WheelScrollAction")
@dataclass(frozen=True)
class WheelScrollAction(Record):
    """input.WheelScrollAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputwheelscrollaction
    """

    x: int = field(metadata=meta("x", required=True, primitive="int"))
    y: int = field(metadata=meta("y", required=True, primitive="int"))
    delta_x: int = field(metadata=meta("deltaX", required=True, primitive="int"))
    delta_y: int = field(metadata=meta("deltaY", required=True, primitive="int"))
    type: str = field(default="scroll", init=False, metadata=meta("type", required=True, fixed="scroll"))
    duration: int | UnsetType = field(default=UNSET, metadata=meta("duration", primitive="int"))
    origin: OriginValue | UnsetType = field(default=UNSET, metadata=meta("origin", ref="input.Origin"))


@register("input.PointerCommonProperties")
@dataclass(frozen=True)
class PointerCommonProperties(Record):
    """input.PointerCommonProperties.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointercommonproperties
    """

    width: int | UnsetType = field(default=UNSET, metadata=meta("width", primitive="int"))
    height: int | UnsetType = field(default=UNSET, metadata=meta("height", primitive="int"))
    pressure: float | UnsetType = field(default=UNSET, metadata=meta("pressure", primitive="float"))
    tangential_pressure: float | UnsetType = field(
        default=UNSET,
        metadata=meta("tangentialPressure", primitive="float"),
    )
    twist: int | UnsetType = field(default=UNSET, metadata=meta("twist", primitive="int"))
    altitude_angle: float | UnsetType = field(default=UNSET, metadata=meta("altitudeAngle", primitive="float"))
    azimuth_angle: float | UnsetType = field(default=UNSET, metadata=meta("azimuthAngle", primitive="float"))


@register("input.ReleaseActionsParameters")
@dataclass(frozen=True)
class ReleaseActionsParameters(Record):
    """input.ReleaseActionsParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputreleaseactionsparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))


@register("input.SetFilesParameters")
@dataclass(frozen=True)
class SetFilesParameters(Record):
    """input.SetFilesParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputsetfilesparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    element: SharedReference = field(metadata=meta("element", required=True, ref="script.SharedReference"))
    files: list[str] = field(metadata=meta("files", required=True, is_list=True, primitive="str"))


@register("input.FileDialogInfo")
@dataclass(frozen=True)
class FileDialogInfo(Record):
    """input.FileDialogInfo.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputfiledialoginfo
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    multiple: bool = field(metadata=meta("multiple", required=True, primitive="bool"))
    user_context: str | UnsetType = field(default=UNSET, metadata=meta("userContext", primitive="str"))
    element: SharedReference | UnsetType = field(
        default=UNSET,
        metadata=meta("element", ref="script.SharedReference"),
    )


@register("input.SourceActions")
class SourceActions(Union):
    """input.SourceActions.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputsourceactions
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "none": "input.NoneSourceActions",
        "key": "input.KeySourceActions",
        "pointer": "input.PointerSourceActions",
        "wheel": "input.WheelSourceActions",
    }
    _DISCRIMINATOR_VALUES = frozenset({"none", "key", "pointer", "wheel"})
    _OBJECT_ONLY = True


SourceActionsValue: TypeAlias = "NoneSourceActions | KeySourceActions | PointerSourceActions | WheelSourceActions"


@register("input.KeySourceAction")
class KeySourceAction(Union):
    """input.KeySourceAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputkeysourceaction
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "pause": "input.PauseAction",
        "keyDown": "input.KeyDownAction",
        "keyUp": "input.KeyUpAction",
    }
    _DISCRIMINATOR_VALUES = frozenset({"pause", "keyDown", "keyUp"})
    _OBJECT_ONLY = True


KeySourceActionValue: TypeAlias = "PauseAction | KeyDownAction | KeyUpAction"


@register("input.PointerSourceAction")
class PointerSourceAction(Union):
    """input.PointerSourceAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputpointersourceaction
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "pause": "input.PauseAction",
        "pointerDown": "input.PointerDownAction",
        "pointerUp": "input.PointerUpAction",
        "pointerMove": "input.PointerMoveAction",
    }
    _DISCRIMINATOR_VALUES = frozenset({"pause", "pointerDown", "pointerUp", "pointerMove"})
    _OBJECT_ONLY = True


PointerSourceActionValue: TypeAlias = "PauseAction | PointerDownAction | PointerUpAction | PointerMoveAction"


@register("input.WheelSourceAction")
class WheelSourceAction(Union):
    """input.WheelSourceAction.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-inputwheelsourceaction
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "pause": "input.PauseAction",
        "scroll": "input.WheelScrollAction",
    }
    _DISCRIMINATOR_VALUES = frozenset({"pause", "scroll"})
    _OBJECT_ONLY = True


WheelSourceActionValue: TypeAlias = "PauseAction | WheelScrollAction"


@register("input.Origin")
class Origin(Union):
    """input.Origin.

    See https://w3c.github.io/webdriver-bidi/#type-input-origin
    """

    _DISCRIMINATOR = "type"
    _VARIANTS = {
        "element": "input.ElementOrigin",
    }
    _DISCRIMINATOR_VALUES = frozenset({"element"})
    _SCALAR_VALUES = frozenset({"viewport", "pointer"})


OriginValue: TypeAlias = "ElementOrigin | Literal['viewport', 'pointer']"


class Input(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-input
    """

    EVENTS = {
        "file_dialog_opened": "input.fileDialogOpened",
    }
    EVENT_TYPES = {
        "input.fileDialogOpened": "input.FileDialogInfo",
    }

    def perform_actions(self, context: str, actions: list[SourceActionsValue]) -> Any:
        """Execute input.performActions (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-input-performActions
        """
        params = PerformActionsParameters(context=context, actions=actions)
        return self._execute("input.performActions", params=params, result=None)

    def release_actions(self, context: str) -> Any:
        """Execute input.releaseActions (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-input-releaseActions
        """
        params = ReleaseActionsParameters(context=context)
        return self._execute("input.releaseActions", params=params, result=None)

    def set_files(self, context: str, element: SharedReference, files: list[str]) -> Any:
        """Execute input.setFiles (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-input-setFiles
        """
        params = SetFilesParameters(context=context, element=element, files=files)
        return self._execute("input.setFiles", params=params, result=None)
