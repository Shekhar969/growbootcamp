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


"""Exception classes for BiDi wire error codes.

Codes the classic WebDriver error handler already types keep that class, so
``except NoSuchElementException`` catches a BiDi failure and a classic one alike, even
where the classic name does not follow from the wire code (``"no such alert"`` is
``NoAlertPresentException``, ``"unable to capture screen"`` is ``ScreenshotException``).
The rest are declared here as ``WebDriverException`` subclasses.

This is internal, unsupported implementation. See
https://www.selenium.dev/documentation/warnings/bidi-implementation/
"""


from __future__ import annotations


from selenium.common.exceptions import (
    InvalidArgumentException,
    InvalidSelectorException,
    InvalidSessionIdException,
    MoveTargetOutOfBoundsException,
    NoAlertPresentException,
    NoSuchElementException,
    NoSuchFrameException,
    ScreenshotException,
    SessionNotCreatedException,
    UnableToSetCookieException,
    WebDriverException,
)


class InvalidWebExtensionException(WebDriverException):
    """Raised for the BiDi "invalid web extension" error."""


class NoSuchNetworkCollectorException(WebDriverException):
    """Raised for the BiDi "no such network collector" error."""


class NoSuchHandleException(WebDriverException):
    """Raised for the BiDi "no such handle" error."""


class NoSuchHistoryEntryException(WebDriverException):
    """Raised for the BiDi "no such history entry" error."""


class NoSuchInterceptException(WebDriverException):
    """Raised for the BiDi "no such intercept" error."""


class NoSuchNetworkDataException(WebDriverException):
    """Raised for the BiDi "no such network data" error."""


class NoSuchNodeException(WebDriverException):
    """Raised for the BiDi "no such node" error."""


class NoSuchRequestException(WebDriverException):
    """Raised for the BiDi "no such request" error."""


class NoSuchScreencastException(WebDriverException):
    """Raised for the BiDi "no such screencast" error."""


class NoSuchScriptException(WebDriverException):
    """Raised for the BiDi "no such script" error."""


class NoSuchStoragePartitionException(WebDriverException):
    """Raised for the BiDi "no such storage partition" error."""


class NoSuchUserContextException(WebDriverException):
    """Raised for the BiDi "no such user context" error."""


class NoSuchWebExtensionException(WebDriverException):
    """Raised for the BiDi "no such web extension" error."""


class UnableToCloseBrowserException(WebDriverException):
    """Raised for the BiDi "unable to close browser" error."""


class UnableToSetFileInputException(WebDriverException):
    """Raised for the BiDi "unable to set file input" error."""


class UnavailableNetworkDataException(WebDriverException):
    """Raised for the BiDi "unavailable network data" error."""


class UnderspecifiedStoragePartitionException(WebDriverException):
    """Raised for the BiDi "underspecified storage partition" error."""


class UnknownCommandException(WebDriverException):
    """Raised for the BiDi "unknown command" error."""


class UnknownErrorException(WebDriverException):
    """Raised for the BiDi "unknown error" error."""


class UnsupportedOperationException(WebDriverException):
    """Raised for the BiDi "unsupported operation" error."""


EXCEPTIONS: dict[str, type[WebDriverException]] = {
    "invalid argument": InvalidArgumentException,
    "invalid selector": InvalidSelectorException,
    "invalid session id": InvalidSessionIdException,
    "invalid web extension": InvalidWebExtensionException,
    "move target out of bounds": MoveTargetOutOfBoundsException,
    "no such alert": NoAlertPresentException,
    "no such network collector": NoSuchNetworkCollectorException,
    "no such element": NoSuchElementException,
    "no such frame": NoSuchFrameException,
    "no such handle": NoSuchHandleException,
    "no such history entry": NoSuchHistoryEntryException,
    "no such intercept": NoSuchInterceptException,
    "no such network data": NoSuchNetworkDataException,
    "no such node": NoSuchNodeException,
    "no such request": NoSuchRequestException,
    "no such screencast": NoSuchScreencastException,
    "no such script": NoSuchScriptException,
    "no such storage partition": NoSuchStoragePartitionException,
    "no such user context": NoSuchUserContextException,
    "no such web extension": NoSuchWebExtensionException,
    "session not created": SessionNotCreatedException,
    "unable to capture screen": ScreenshotException,
    "unable to close browser": UnableToCloseBrowserException,
    "unable to set cookie": UnableToSetCookieException,
    "unable to set file input": UnableToSetFileInputException,
    "unavailable network data": UnavailableNetworkDataException,
    "underspecified storage partition": UnderspecifiedStoragePartitionException,
    "unknown command": UnknownCommandException,
    "unknown error": UnknownErrorException,
    "unsupported operation": UnsupportedOperationException,
}


def exception_for(code: str | None) -> type[WebDriverException]:
    """The exception class for a wire error code, falling back for an unrecognized one.

    An error the remote end reports must surface as that error even when the code is one
    this schema does not declare, so an unknown code is never a serialization failure.
    """
    return EXCEPTIONS.get(code, WebDriverException) if code else WebDriverException
