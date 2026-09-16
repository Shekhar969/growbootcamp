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


@register("emulation.ForcedColorsModeTheme")
class ForcedColorsModeTheme(str, Enum):
    """emulation.ForcedColorsModeTheme.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationforcedcolorsmodetheme
    """

    LIGHT = "light"
    DARK = "dark"


@register("emulation.ScreenOrientationNatural")
class ScreenOrientationNatural(str, Enum):
    """emulation.ScreenOrientationNatural.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientationnatural
    """

    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"


@register("emulation.ScreenOrientationType")
class ScreenOrientationType(str, Enum):
    """emulation.ScreenOrientationType.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientationtype
    """

    PORTRAIT_PRIMARY = "portrait-primary"
    PORTRAIT_SECONDARY = "portrait-secondary"
    LANDSCAPE_PRIMARY = "landscape-primary"
    LANDSCAPE_SECONDARY = "landscape-secondary"


@register("emulation.MediaFeaturesAnyHover")
class MediaFeaturesAnyHover(str, Enum):
    NONE = "none"
    HOVER = "hover"


@register("emulation.MediaFeaturesAnyPointer")
class MediaFeaturesAnyPointer(str, Enum):
    NONE = "none"
    COARSE = "coarse"
    FINE = "fine"


@register("emulation.MediaFeaturesColorGamut")
class MediaFeaturesColorGamut(str, Enum):
    SRGB = "srgb"
    P3 = "p3"
    REC2020 = "rec2020"


@register("emulation.MediaFeaturesDisplayMode")
class MediaFeaturesDisplayMode(str, Enum):
    FULLSCREEN = "fullscreen"
    STANDALONE = "standalone"
    MINIMAL_UI = "minimal-ui"
    BROWSER = "browser"
    PICTURE_IN_PICTURE = "picture-in-picture"


@register("emulation.MediaFeaturesDynamicRange")
class MediaFeaturesDynamicRange(str, Enum):
    STANDARD = "standard"
    HIGH = "high"


@register("emulation.MediaFeaturesEnvironmentBlending")
class MediaFeaturesEnvironmentBlending(str, Enum):
    OPAQUE = "opaque"
    ADDITIVE = "additive"
    SUBTRACTIVE = "subtractive"


@register("emulation.MediaFeaturesForcedColors")
class MediaFeaturesForcedColors(str, Enum):
    NONE = "none"
    ACTIVE = "active"


@register("emulation.MediaFeaturesGrid")
class MediaFeaturesGrid(int, Enum):
    _0 = 0
    _1 = 1


@register("emulation.MediaFeaturesHover")
class MediaFeaturesHover(str, Enum):
    NONE = "none"
    HOVER = "hover"


@register("emulation.MediaFeaturesInvertedColors")
class MediaFeaturesInvertedColors(str, Enum):
    NONE = "none"
    INVERTED = "inverted"


@register("emulation.MediaFeaturesNavControls")
class MediaFeaturesNavControls(str, Enum):
    NONE = "none"
    BACK = "back"


@register("emulation.MediaFeaturesOverflowBlock")
class MediaFeaturesOverflowBlock(str, Enum):
    NONE = "none"
    SCROLL = "scroll"
    OPTIONAL_PAGED = "optional-paged"
    PAGED = "paged"


@register("emulation.MediaFeaturesOverflowInline")
class MediaFeaturesOverflowInline(str, Enum):
    NONE = "none"
    SCROLL = "scroll"


@register("emulation.MediaFeaturesPointer")
class MediaFeaturesPointer(str, Enum):
    NONE = "none"
    COARSE = "coarse"
    FINE = "fine"


@register("emulation.MediaFeaturesPrefersColorScheme")
class MediaFeaturesPrefersColorScheme(str, Enum):
    LIGHT = "light"
    DARK = "dark"


@register("emulation.MediaFeaturesPrefersContrast")
class MediaFeaturesPrefersContrast(str, Enum):
    NO_PREFERENCE = "no-preference"
    MORE = "more"
    LESS = "less"
    CUSTOM = "custom"


@register("emulation.MediaFeaturesPrefersReducedData")
class MediaFeaturesPrefersReducedData(str, Enum):
    NO_PREFERENCE = "no-preference"
    REDUCE = "reduce"


@register("emulation.MediaFeaturesPrefersReducedMotion")
class MediaFeaturesPrefersReducedMotion(str, Enum):
    NO_PREFERENCE = "no-preference"
    REDUCE = "reduce"


@register("emulation.MediaFeaturesPrefersReducedTransparency")
class MediaFeaturesPrefersReducedTransparency(str, Enum):
    NO_PREFERENCE = "no-preference"
    REDUCE = "reduce"


@register("emulation.MediaFeaturesScan")
class MediaFeaturesScan(str, Enum):
    INTERLACE = "interlace"
    PROGRESSIVE = "progressive"


@register("emulation.MediaFeaturesScripting")
class MediaFeaturesScripting(str, Enum):
    NONE = "none"
    INITIAL_ONLY = "initial-only"
    ENABLED = "enabled"


@register("emulation.MediaFeaturesUpdate")
class MediaFeaturesUpdate(str, Enum):
    NONE = "none"
    SLOW = "slow"
    FAST = "fast"


@register("emulation.MediaFeaturesVideoColorGamut")
class MediaFeaturesVideoColorGamut(str, Enum):
    SRGB = "srgb"
    P3 = "p3"
    REC2020 = "rec2020"


@register("emulation.MediaFeaturesVideoDynamicRange")
class MediaFeaturesVideoDynamicRange(str, Enum):
    STANDARD = "standard"
    HIGH = "high"


@register("emulation.SetScrollbarTypeOverrideParametersScrollbarType")
class SetScrollbarTypeOverrideParametersScrollbarType(str, Enum):
    CLASSIC = "classic"
    OVERLAY = "overlay"


@register("emulation.SetForcedColorsModeThemeOverrideParameters")
@dataclass(frozen=True)
class SetForcedColorsModeThemeOverrideParameters(Record):
    """emulation.SetForcedColorsModeThemeOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetforcedcolorsmodethemeoverrideparameters
    """

    theme: ForcedColorsModeTheme | None = field(
        metadata=meta("theme", required=True, nullable=True, enum="emulation.ForcedColorsModeTheme"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.GeolocationCoordinates")
@dataclass(frozen=True)
class GeolocationCoordinates(Record):
    """emulation.GeolocationCoordinates.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationgeolocationcoordinates
    """

    latitude: float = field(metadata=meta("latitude", required=True, primitive="float"))
    longitude: float = field(metadata=meta("longitude", required=True, primitive="float"))
    accuracy: float | UnsetType = field(default=UNSET, metadata=meta("accuracy", primitive="float"))
    altitude: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("altitude", nullable=True, primitive="float"),
    )
    altitude_accuracy: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("altitudeAccuracy", nullable=True, primitive="float"),
    )
    heading: float | None | UnsetType = field(
        default=UNSET,
        metadata=meta("heading", nullable=True, primitive="float"),
    )
    speed: float | None | UnsetType = field(default=UNSET, metadata=meta("speed", nullable=True, primitive="float"))


@register("emulation.GeolocationPositionError")
@dataclass(frozen=True)
class GeolocationPositionError(Record):
    """emulation.GeolocationPositionError.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationgeolocationpositionerror
    """

    type: str = field(
        default="positionUnavailable",
        init=False,
        metadata=meta("type", required=True, fixed="positionUnavailable"),
    )


@register("emulation.SetLocaleOverrideParameters")
@dataclass(frozen=True)
class SetLocaleOverrideParameters(Record):
    """emulation.SetLocaleOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetlocaleoverrideparameters
    """

    locale: str | None = field(metadata=meta("locale", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetMediaFeaturesOverrideParameters")
@dataclass(frozen=True)
class SetMediaFeaturesOverrideParameters(Record):
    """emulation.SetMediaFeaturesOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetmediafeaturesoverrideparameters
    """

    features: MediaFeatures | None = field(
        metadata=meta("features", required=True, nullable=True, ref="emulation.MediaFeatures"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.MediaFeatures")
@dataclass(frozen=True)
class MediaFeatures(Record):
    """emulation.MediaFeatures.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationmediafeatures
    """

    any_hover: MediaFeaturesAnyHover | None | UnsetType = field(
        default=UNSET,
        metadata=meta("any-hover", nullable=True, enum="emulation.MediaFeaturesAnyHover"),
    )
    any_pointer: MediaFeaturesAnyPointer | None | UnsetType = field(
        default=UNSET,
        metadata=meta("any-pointer", nullable=True, enum="emulation.MediaFeaturesAnyPointer"),
    )
    color: int | None | UnsetType = field(default=UNSET, metadata=meta("color", nullable=True, primitive="int"))
    color_gamut: MediaFeaturesColorGamut | None | UnsetType = field(
        default=UNSET,
        metadata=meta("color-gamut", nullable=True, enum="emulation.MediaFeaturesColorGamut"),
    )
    color_index: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("color-index", nullable=True, primitive="int"),
    )
    display_mode: MediaFeaturesDisplayMode | None | UnsetType = field(
        default=UNSET,
        metadata=meta("display-mode", nullable=True, enum="emulation.MediaFeaturesDisplayMode"),
    )
    dynamic_range: MediaFeaturesDynamicRange | None | UnsetType = field(
        default=UNSET,
        metadata=meta("dynamic-range", nullable=True, enum="emulation.MediaFeaturesDynamicRange"),
    )
    environment_blending: MediaFeaturesEnvironmentBlending | None | UnsetType = field(
        default=UNSET,
        metadata=meta("environment-blending", nullable=True, enum="emulation.MediaFeaturesEnvironmentBlending"),
    )
    forced_colors: MediaFeaturesForcedColors | None | UnsetType = field(
        default=UNSET,
        metadata=meta("forced-colors", nullable=True, enum="emulation.MediaFeaturesForcedColors"),
    )
    grid: MediaFeaturesGrid | None | UnsetType = field(
        default=UNSET,
        metadata=meta("grid", nullable=True, enum="emulation.MediaFeaturesGrid"),
    )
    horizontal_viewport_segments: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("horizontal-viewport-segments", nullable=True, primitive="int"),
    )
    hover: MediaFeaturesHover | None | UnsetType = field(
        default=UNSET,
        metadata=meta("hover", nullable=True, enum="emulation.MediaFeaturesHover"),
    )
    inverted_colors: MediaFeaturesInvertedColors | None | UnsetType = field(
        default=UNSET,
        metadata=meta("inverted-colors", nullable=True, enum="emulation.MediaFeaturesInvertedColors"),
    )
    monochrome: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("monochrome", nullable=True, primitive="int"),
    )
    nav_controls: MediaFeaturesNavControls | None | UnsetType = field(
        default=UNSET,
        metadata=meta("nav-controls", nullable=True, enum="emulation.MediaFeaturesNavControls"),
    )
    overflow_block: MediaFeaturesOverflowBlock | None | UnsetType = field(
        default=UNSET,
        metadata=meta("overflow-block", nullable=True, enum="emulation.MediaFeaturesOverflowBlock"),
    )
    overflow_inline: MediaFeaturesOverflowInline | None | UnsetType = field(
        default=UNSET,
        metadata=meta("overflow-inline", nullable=True, enum="emulation.MediaFeaturesOverflowInline"),
    )
    pointer: MediaFeaturesPointer | None | UnsetType = field(
        default=UNSET,
        metadata=meta("pointer", nullable=True, enum="emulation.MediaFeaturesPointer"),
    )
    prefers_color_scheme: MediaFeaturesPrefersColorScheme | None | UnsetType = field(
        default=UNSET,
        metadata=meta("prefers-color-scheme", nullable=True, enum="emulation.MediaFeaturesPrefersColorScheme"),
    )
    prefers_contrast: MediaFeaturesPrefersContrast | None | UnsetType = field(
        default=UNSET,
        metadata=meta("prefers-contrast", nullable=True, enum="emulation.MediaFeaturesPrefersContrast"),
    )
    prefers_reduced_data: MediaFeaturesPrefersReducedData | None | UnsetType = field(
        default=UNSET,
        metadata=meta("prefers-reduced-data", nullable=True, enum="emulation.MediaFeaturesPrefersReducedData"),
    )
    prefers_reduced_motion: MediaFeaturesPrefersReducedMotion | None | UnsetType = field(
        default=UNSET,
        metadata=meta("prefers-reduced-motion", nullable=True, enum="emulation.MediaFeaturesPrefersReducedMotion"),
    )
    prefers_reduced_transparency: MediaFeaturesPrefersReducedTransparency | None | UnsetType = field(
        default=UNSET,
        metadata=meta("prefers-reduced-transparency", nullable=True, enum="emulation.MediaFeaturesPrefersReducedTransparency"),
    )
    scan: MediaFeaturesScan | None | UnsetType = field(
        default=UNSET,
        metadata=meta("scan", nullable=True, enum="emulation.MediaFeaturesScan"),
    )
    scripting: MediaFeaturesScripting | None | UnsetType = field(
        default=UNSET,
        metadata=meta("scripting", nullable=True, enum="emulation.MediaFeaturesScripting"),
    )
    update: MediaFeaturesUpdate | None | UnsetType = field(
        default=UNSET,
        metadata=meta("update", nullable=True, enum="emulation.MediaFeaturesUpdate"),
    )
    vertical_viewport_segments: int | None | UnsetType = field(
        default=UNSET,
        metadata=meta("vertical-viewport-segments", nullable=True, primitive="int"),
    )
    video_color_gamut: MediaFeaturesVideoColorGamut | None | UnsetType = field(
        default=UNSET,
        metadata=meta("video-color-gamut", nullable=True, enum="emulation.MediaFeaturesVideoColorGamut"),
    )
    video_dynamic_range: MediaFeaturesVideoDynamicRange | None | UnsetType = field(
        default=UNSET,
        metadata=meta("video-dynamic-range", nullable=True, enum="emulation.MediaFeaturesVideoDynamicRange"),
    )


@register("emulation.SetNetworkConditionsParameters")
@dataclass(frozen=True)
class SetNetworkConditionsParameters(Record):
    """emulation.SetNetworkConditionsParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetnetworkconditionsparameters
    """

    network_conditions: NetworkConditionsOffline | None = field(
        metadata=meta("networkConditions", required=True, nullable=True, ref="emulation.NetworkConditionsOffline"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.NetworkConditionsOffline")
@dataclass(frozen=True)
class NetworkConditionsOffline(Record):
    """emulation.NetworkConditionsOffline.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationnetworkconditionsoffline
    """

    type: str = field(default="offline", init=False, metadata=meta("type", required=True, fixed="offline"))


@register("emulation.ScreenArea")
@dataclass(frozen=True)
class ScreenArea(Record):
    """emulation.ScreenArea.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenarea
    """

    width: int = field(metadata=meta("width", required=True, primitive="int"))
    height: int = field(metadata=meta("height", required=True, primitive="int"))


@register("emulation.SetScreenSettingsOverrideParameters")
@dataclass(frozen=True)
class SetScreenSettingsOverrideParameters(Record):
    """emulation.SetScreenSettingsOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscreensettingsoverrideparameters
    """

    screen_area: ScreenArea | None = field(
        metadata=meta("screenArea", required=True, nullable=True, ref="emulation.ScreenArea"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.ScreenOrientation")
@dataclass(frozen=True)
class ScreenOrientation(Record):
    """emulation.ScreenOrientation.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationscreenorientation
    """

    natural: ScreenOrientationNatural = field(
        metadata=meta("natural", required=True, enum="emulation.ScreenOrientationNatural"),
    )
    type: ScreenOrientationType = field(
        metadata=meta("type", required=True, enum="emulation.ScreenOrientationType"),
    )


@register("emulation.SetScreenOrientationOverrideParameters")
@dataclass(frozen=True)
class SetScreenOrientationOverrideParameters(Record):
    """emulation.SetScreenOrientationOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscreenorientationoverrideparameters
    """

    screen_orientation: ScreenOrientation | None = field(
        metadata=meta("screenOrientation", required=True, nullable=True, ref="emulation.ScreenOrientation"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetUserAgentOverrideParameters")
@dataclass(frozen=True)
class SetUserAgentOverrideParameters(Record):
    """emulation.SetUserAgentOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetuseragentoverrideparameters
    """

    user_agent: str | None = field(metadata=meta("userAgent", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetViewportMetaOverrideParameters")
@dataclass(frozen=True)
class SetViewportMetaOverrideParameters(Record):
    """emulation.SetViewportMetaOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetviewportmetaoverrideparameters
    """

    viewport_meta: bool | None = field(metadata=meta("viewportMeta", required=True, nullable=True, fixed=True))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetScriptingEnabledParameters")
@dataclass(frozen=True)
class SetScriptingEnabledParameters(Record):
    """emulation.SetScriptingEnabledParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscriptingenabledparameters
    """

    enabled: bool | None = field(metadata=meta("enabled", required=True, nullable=True, fixed=False))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetScrollbarTypeOverrideParameters")
@dataclass(frozen=True)
class SetScrollbarTypeOverrideParameters(Record):
    """emulation.SetScrollbarTypeOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetscrollbartypeoverrideparameters
    """

    scrollbar_type: SetScrollbarTypeOverrideParametersScrollbarType | None = field(
        metadata=meta("scrollbarType", required=True, nullable=True, enum="emulation.SetScrollbarTypeOverrideParametersScrollbarType"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetTimezoneOverrideParameters")
@dataclass(frozen=True)
class SetTimezoneOverrideParameters(Record):
    """emulation.SetTimezoneOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsettimezoneoverrideparameters
    """

    timezone: str | None = field(metadata=meta("timezone", required=True, nullable=True, primitive="str"))
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetTouchOverrideParameters")
@dataclass(frozen=True)
class SetTouchOverrideParameters(Record):
    """emulation.SetTouchOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsettouchoverrideparameters
    """

    max_touch_points: int | None = field(
        metadata=meta("maxTouchPoints", required=True, nullable=True, primitive="int"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters_Coordinates")
@dataclass(frozen=True)
class SetGeolocationOverrideParametersCoordinates(Record):
    coordinates: GeolocationCoordinates | None = field(
        metadata=meta("coordinates", required=True, nullable=True, ref="emulation.GeolocationCoordinates"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters_Error")
@dataclass(frozen=True)
class SetGeolocationOverrideParametersError(Record):
    error: GeolocationPositionError = field(
        metadata=meta("error", required=True, ref="emulation.GeolocationPositionError"),
    )
    contexts: list[str] | UnsetType = field(default=UNSET, metadata=meta("contexts", is_list=True, primitive="str"))
    user_contexts: list[str] | UnsetType = field(
        default=UNSET,
        metadata=meta("userContexts", is_list=True, primitive="str"),
    )


@register("emulation.SetGeolocationOverrideParameters")
class SetGeolocationOverrideParameters(Union):
    """emulation.SetGeolocationOverrideParameters.

    See https://w3c.github.io/webdriver-bidi/#cddl-type-emulationsetgeolocationoverrideparameters
    """

    _PRESENCE = (
        ("emulation.SetGeolocationOverrideParameters_Coordinates", ("coordinates",)),
        ("emulation.SetGeolocationOverrideParameters_Error", ("error",)),
    )
    _OBJECT_ONLY = True


SetGeolocationOverrideParametersValue: TypeAlias = (
    "SetGeolocationOverrideParametersCoordinates | SetGeolocationOverrideParametersError"
)


class Emulation(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    See https://w3c.github.io/webdriver-bidi/#module-emulation
    """

    def set_forced_colors_mode_theme_override(
        self,
        theme: ForcedColorsModeTheme | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setForcedColorsModeThemeOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setForcedColorsModeThemeOverride
        """
        params = SetForcedColorsModeThemeOverrideParameters(
            theme=theme,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setForcedColorsModeThemeOverride", params=params, result=None)

    def set_geolocation_override(
        self,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
        coordinates: GeolocationCoordinates | None | UnsetType = UNSET,
        error: GeolocationPositionError | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setGeolocationOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setGeolocationOverride
        """
        params = SetGeolocationOverrideParameters.build(
            contexts=contexts,
            user_contexts=user_contexts,
            coordinates=coordinates,
            error=error,
        )
        return self._execute("emulation.setGeolocationOverride", params=params, result=None)

    def set_locale_override(
        self,
        locale: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setLocaleOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setLocaleOverride
        """
        params = SetLocaleOverrideParameters(locale=locale, contexts=contexts, user_contexts=user_contexts)
        return self._execute("emulation.setLocaleOverride", params=params, result=None)

    def set_media_features_override(
        self,
        features: MediaFeatures | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setMediaFeaturesOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setMediaFeaturesOverride
        """
        params = SetMediaFeaturesOverrideParameters(
            features=features,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setMediaFeaturesOverride", params=params, result=None)

    def set_network_conditions(
        self,
        network_conditions: NetworkConditionsOffline | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setNetworkConditions (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setNetworkConditions
        """
        params = SetNetworkConditionsParameters(
            network_conditions=network_conditions,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setNetworkConditions", params=params, result=None)

    def set_screen_orientation_override(
        self,
        screen_orientation: ScreenOrientation | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScreenOrientationOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScreenOrientationOverride
        """
        params = SetScreenOrientationOverrideParameters(
            screen_orientation=screen_orientation,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScreenOrientationOverride", params=params, result=None)

    def set_screen_settings_override(
        self,
        screen_area: ScreenArea | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScreenSettingsOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScreenSettingsOverride
        """
        params = SetScreenSettingsOverrideParameters(
            screen_area=screen_area,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScreenSettingsOverride", params=params, result=None)

    def set_scripting_enabled(
        self,
        enabled: bool | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScriptingEnabled (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScriptingEnabled
        """
        params = SetScriptingEnabledParameters(enabled=enabled, contexts=contexts, user_contexts=user_contexts)
        return self._execute("emulation.setScriptingEnabled", params=params, result=None)

    def set_scrollbar_type_override(
        self,
        scrollbar_type: SetScrollbarTypeOverrideParametersScrollbarType | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setScrollbarTypeOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setScrollbarTypeOverride
        """
        params = SetScrollbarTypeOverrideParameters(
            scrollbar_type=scrollbar_type,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setScrollbarTypeOverride", params=params, result=None)

    def set_timezone_override(
        self,
        timezone: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setTimezoneOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setTimezoneOverride
        """
        params = SetTimezoneOverrideParameters(
            timezone=timezone,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setTimezoneOverride", params=params, result=None)

    def set_touch_override(
        self,
        max_touch_points: int | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setTouchOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setTouchOverride
        """
        params = SetTouchOverrideParameters(
            max_touch_points=max_touch_points,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setTouchOverride", params=params, result=None)

    def set_user_agent_override(
        self,
        user_agent: str | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setUserAgentOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setUserAgentOverride
        """
        params = SetUserAgentOverrideParameters(
            user_agent=user_agent,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setUserAgentOverride", params=params, result=None)

    def set_viewport_meta_override(
        self,
        viewport_meta: bool | None,
        contexts: list[str] | UnsetType = UNSET,
        user_contexts: list[str] | UnsetType = UNSET,
    ) -> Any:
        """Execute emulation.setViewportMetaOverride (internal, unsupported).

        See https://w3c.github.io/webdriver-bidi/#command-emulation-setViewportMetaOverride
        """
        params = SetViewportMetaOverrideParameters(
            viewport_meta=viewport_meta,
            contexts=contexts,
            user_contexts=user_contexts,
        )
        return self._execute("emulation.setViewportMetaOverride", params=params, result=None)
