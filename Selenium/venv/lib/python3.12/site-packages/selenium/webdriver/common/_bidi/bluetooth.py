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


@register("bluetooth.SimulateAdapterParametersState")
class SimulateAdapterParametersState(str, Enum):
    ABSENT = "absent"
    POWERED_OFF = "powered-off"
    POWERED_ON = "powered-on"


@register("bluetooth.SimulateServiceParametersType")
class SimulateServiceParametersType(str, Enum):
    ADD = "add"
    REMOVE = "remove"


@register("bluetooth.SimulateCharacteristicParametersType")
class SimulateCharacteristicParametersType(str, Enum):
    ADD = "add"
    REMOVE = "remove"


@register("bluetooth.SimulateCharacteristicResponseParametersType")
class SimulateCharacteristicResponseParametersType(str, Enum):
    READ = "read"
    WRITE = "write"
    SUBSCRIBE_TO_NOTIFICATIONS = "subscribe-to-notifications"
    UNSUBSCRIBE_FROM_NOTIFICATIONS = "unsubscribe-from-notifications"


@register("bluetooth.SimulateDescriptorParametersType")
class SimulateDescriptorParametersType(str, Enum):
    ADD = "add"
    REMOVE = "remove"


@register("bluetooth.SimulateDescriptorResponseParametersType")
class SimulateDescriptorResponseParametersType(str, Enum):
    READ = "read"
    WRITE = "write"


@register("bluetooth.CharacteristicEventGeneratedParametersType")
class CharacteristicEventGeneratedParametersType(str, Enum):
    READ = "read"
    WRITE_WITH_RESPONSE = "write-with-response"
    WRITE_WITHOUT_RESPONSE = "write-without-response"
    SUBSCRIBE_TO_NOTIFICATIONS = "subscribe-to-notifications"
    UNSUBSCRIBE_FROM_NOTIFICATIONS = "unsubscribe-from-notifications"


@register("bluetooth.DescriptorEventGeneratedParametersType")
class DescriptorEventGeneratedParametersType(str, Enum):
    READ = "read"
    WRITE = "write"


@register("bluetooth.BluetoothManufacturerData")
@dataclass(frozen=True)
class BluetoothManufacturerData(Record):
    """bluetooth.BluetoothManufacturerData.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothbluetoothmanufacturerdata
    """

    key: int = field(metadata=meta("key", required=True, primitive="int"))
    data: str = field(metadata=meta("data", required=True, primitive="str"))


@register("bluetooth.CharacteristicProperties")
@dataclass(frozen=True)
class CharacteristicProperties(Record):
    """bluetooth.CharacteristicProperties.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothcharacteristicproperties
    """

    broadcast: bool | UnsetType = field(default=UNSET, metadata=meta("broadcast", primitive="bool"))
    read: bool | UnsetType = field(default=UNSET, metadata=meta("read", primitive="bool"))
    write_without_response: bool | UnsetType = field(
        default=UNSET,
        metadata=meta("writeWithoutResponse", primitive="bool"),
    )
    write: bool | UnsetType = field(default=UNSET, metadata=meta("write", primitive="bool"))
    notify: bool | UnsetType = field(default=UNSET, metadata=meta("notify", primitive="bool"))
    indicate: bool | UnsetType = field(default=UNSET, metadata=meta("indicate", primitive="bool"))
    authenticated_signed_writes: bool | UnsetType = field(
        default=UNSET,
        metadata=meta("authenticatedSignedWrites", primitive="bool"),
    )
    extended_properties: bool | UnsetType = field(
        default=UNSET,
        metadata=meta("extendedProperties", primitive="bool"),
    )


@register("bluetooth.RequestDeviceInfo")
@dataclass(frozen=True)
class RequestDeviceInfo(Record):
    """bluetooth.RequestDeviceInfo.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothrequestdeviceinfo
    """

    id: str = field(metadata=meta("id", required=True, primitive="str"))
    name: str | None = field(metadata=meta("name", required=True, nullable=True, primitive="str"))


@register("bluetooth.ScanRecord")
@dataclass(frozen=True)
class ScanRecord(Record):
    """bluetooth.ScanRecord.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothscanrecord
    """

    name: str | UnsetType = field(default=UNSET, metadata=meta("name", primitive="str"))
    uuids: list[str] | UnsetType = field(default=UNSET, metadata=meta("uuids", is_list=True, primitive="str"))
    appearance: float | UnsetType = field(default=UNSET, metadata=meta("appearance", primitive="float"))
    manufacturer_data: list[BluetoothManufacturerData] | UnsetType = field(
        default=UNSET,
        metadata=meta("manufacturerData", ref="bluetooth.BluetoothManufacturerData", is_list=True),
    )


@register("bluetooth.SimulateAdapterParameters")
@dataclass(frozen=True)
class SimulateAdapterParameters(Record):
    """bluetooth.SimulateAdapterParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulateadapterparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    state: SimulateAdapterParametersState = field(
        metadata=meta("state", required=True, enum="bluetooth.SimulateAdapterParametersState"),
    )
    le_supported: bool | UnsetType = field(default=UNSET, metadata=meta("leSupported", primitive="bool"))


@register("bluetooth.DisableSimulationParameters")
@dataclass(frozen=True)
class DisableSimulationParameters(Record):
    """bluetooth.DisableSimulationParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothdisablesimulationparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))


@register("bluetooth.SimulatePreconnectedPeripheralParameters")
@dataclass(frozen=True)
class SimulatePreconnectedPeripheralParameters(Record):
    """bluetooth.SimulatePreconnectedPeripheralParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulatepreconnectedperipheralparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    name: str = field(metadata=meta("name", required=True, primitive="str"))
    manufacturer_data: list[BluetoothManufacturerData] = field(
        metadata=meta("manufacturerData", required=True, ref="bluetooth.BluetoothManufacturerData", is_list=True),
    )
    known_service_uuids: list[str] = field(
        metadata=meta("knownServiceUuids", required=True, is_list=True, primitive="str"),
    )


@register("bluetooth.SimulateAdvertisementParameters")
@dataclass(frozen=True)
class SimulateAdvertisementParameters(Record):
    """bluetooth.SimulateAdvertisementParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulateadvertisementparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    scan_entry: SimulateAdvertisementScanEntryParameters = field(
        metadata=meta("scanEntry", required=True, ref="bluetooth.SimulateAdvertisementScanEntryParameters"),
    )


@register("bluetooth.SimulateAdvertisementScanEntryParameters")
@dataclass(frozen=True)
class SimulateAdvertisementScanEntryParameters(Record):
    """bluetooth.SimulateAdvertisementScanEntryParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulateadvertisementscanentryparameters
    """

    device_address: str = field(metadata=meta("deviceAddress", required=True, primitive="str"))
    rssi: float = field(metadata=meta("rssi", required=True, primitive="float"))
    scan_record: ScanRecord = field(metadata=meta("scanRecord", required=True, ref="bluetooth.ScanRecord"))


@register("bluetooth.SimulateGattConnectionResponseParameters")
@dataclass(frozen=True)
class SimulateGattConnectionResponseParameters(Record):
    """bluetooth.SimulateGattConnectionResponseParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulategattconnectionresponseparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    code: int = field(metadata=meta("code", required=True, primitive="int"))


@register("bluetooth.SimulateGattDisconnectionParameters")
@dataclass(frozen=True)
class SimulateGattDisconnectionParameters(Record):
    """bluetooth.SimulateGattDisconnectionParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulategattdisconnectionparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))


@register("bluetooth.SimulateServiceParameters")
@dataclass(frozen=True)
class SimulateServiceParameters(Record):
    """bluetooth.SimulateServiceParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulateserviceparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    uuid: str = field(metadata=meta("uuid", required=True, primitive="str"))
    type: SimulateServiceParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.SimulateServiceParametersType"),
    )


@register("bluetooth.SimulateCharacteristicParameters")
@dataclass(frozen=True)
class SimulateCharacteristicParameters(Record):
    """bluetooth.SimulateCharacteristicParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulatecharacteristicparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    type: SimulateCharacteristicParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.SimulateCharacteristicParametersType"),
    )
    characteristic_properties: CharacteristicProperties | UnsetType = field(
        default=UNSET,
        metadata=meta("characteristicProperties", ref="bluetooth.CharacteristicProperties"),
    )


@register("bluetooth.SimulateCharacteristicResponseParameters")
@dataclass(frozen=True)
class SimulateCharacteristicResponseParameters(Record):
    """bluetooth.SimulateCharacteristicResponseParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulatecharacteristicresponseparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    type: SimulateCharacteristicResponseParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.SimulateCharacteristicResponseParametersType"),
    )
    code: int = field(metadata=meta("code", required=True, primitive="int"))
    data: list[int] | UnsetType = field(default=UNSET, metadata=meta("data", is_list=True, primitive="int"))


@register("bluetooth.SimulateDescriptorParameters")
@dataclass(frozen=True)
class SimulateDescriptorParameters(Record):
    """bluetooth.SimulateDescriptorParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulatedescriptorparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    descriptor_uuid: str = field(metadata=meta("descriptorUuid", required=True, primitive="str"))
    type: SimulateDescriptorParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.SimulateDescriptorParametersType"),
    )


@register("bluetooth.SimulateDescriptorResponseParameters")
@dataclass(frozen=True)
class SimulateDescriptorResponseParameters(Record):
    """bluetooth.SimulateDescriptorResponseParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothsimulatedescriptorresponseparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    descriptor_uuid: str = field(metadata=meta("descriptorUuid", required=True, primitive="str"))
    type: SimulateDescriptorResponseParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.SimulateDescriptorResponseParametersType"),
    )
    code: int = field(metadata=meta("code", required=True, primitive="int"))
    data: list[int] | UnsetType = field(default=UNSET, metadata=meta("data", is_list=True, primitive="int"))


@register("bluetooth.RequestDevicePromptUpdatedParameters")
@dataclass(frozen=True)
class RequestDevicePromptUpdatedParameters(Record):
    """bluetooth.RequestDevicePromptUpdatedParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothrequestdevicepromptupdatedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    prompt: str = field(metadata=meta("prompt", required=True, primitive="str"))
    devices: list[RequestDeviceInfo] = field(
        metadata=meta("devices", required=True, ref="bluetooth.RequestDeviceInfo", is_list=True),
    )


@register("bluetooth.GattConnectionAttemptedParameters")
@dataclass(frozen=True)
class GattConnectionAttemptedParameters(Record):
    """bluetooth.GattConnectionAttemptedParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothgattconnectionattemptedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))


@register("bluetooth.CharacteristicEventGeneratedParameters")
@dataclass(frozen=True)
class CharacteristicEventGeneratedParameters(Record):
    """bluetooth.CharacteristicEventGeneratedParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothcharacteristiceventgeneratedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    type: CharacteristicEventGeneratedParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.CharacteristicEventGeneratedParametersType"),
    )
    data: list[int] | UnsetType = field(default=UNSET, metadata=meta("data", is_list=True, primitive="int"))


@register("bluetooth.DescriptorEventGeneratedParameters")
@dataclass(frozen=True)
class DescriptorEventGeneratedParameters(Record):
    """bluetooth.DescriptorEventGeneratedParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothdescriptoreventgeneratedparameters
    """

    context: str = field(metadata=meta("context", required=True, primitive="str"))
    address: str = field(metadata=meta("address", required=True, primitive="str"))
    service_uuid: str = field(metadata=meta("serviceUuid", required=True, primitive="str"))
    characteristic_uuid: str = field(metadata=meta("characteristicUuid", required=True, primitive="str"))
    descriptor_uuid: str = field(metadata=meta("descriptorUuid", required=True, primitive="str"))
    type: DescriptorEventGeneratedParametersType = field(
        metadata=meta("type", required=True, enum="bluetooth.DescriptorEventGeneratedParametersType"),
    )
    data: list[int] | UnsetType = field(default=UNSET, metadata=meta("data", is_list=True, primitive="int"))


@register("bluetooth.HandleRequestDevicePromptParameters_AcceptParameters")
@dataclass(frozen=True)
class HandleRequestDevicePromptParametersAcceptParameters(Record):
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    prompt: str = field(metadata=meta("prompt", required=True, primitive="str"))
    device: str = field(metadata=meta("device", required=True, primitive="str"))
    accept: bool = field(default=True, init=False, metadata=meta("accept", required=True, fixed=True))


@register("bluetooth.HandleRequestDevicePromptParameters_CancelParameters")
@dataclass(frozen=True)
class HandleRequestDevicePromptParametersCancelParameters(Record):
    context: str = field(metadata=meta("context", required=True, primitive="str"))
    prompt: str = field(metadata=meta("prompt", required=True, primitive="str"))
    accept: bool = field(default=False, init=False, metadata=meta("accept", required=True, fixed=False))


@register("bluetooth.HandleRequestDevicePromptParameters")
class HandleRequestDevicePromptParameters(Union):
    """bluetooth.HandleRequestDevicePromptParameters.

    See https://webbluetoothcg.github.io/web-bluetooth/#cddl-type-bluetoothhandlerequestdevicepromptparameters
    """

    _DISCRIMINATOR = "accept"
    _VARIANTS = {
        True: "bluetooth.HandleRequestDevicePromptParameters_AcceptParameters",
        False: "bluetooth.HandleRequestDevicePromptParameters_CancelParameters",
    }
    _OBJECT_ONLY = True


HandleRequestDevicePromptParametersValue: TypeAlias = (
    "HandleRequestDevicePromptParametersAcceptParameters | HandleRequestDevicePromptParametersCancelParameters"
)


class Bluetooth(Domain):
    """Internal, unsupported.

    See https://www.selenium.dev/documentation/warnings/bidi-implementation/
    """

    EVENTS = {
        "request_device_prompt_updated": "bluetooth.requestDevicePromptUpdated",
        "gatt_connection_attempted": "bluetooth.gattConnectionAttempted",
    }
    EVENT_TYPES = {
        "bluetooth.requestDevicePromptUpdated": "bluetooth.RequestDevicePromptUpdatedParameters",
        "bluetooth.gattConnectionAttempted": "bluetooth.GattConnectionAttemptedParameters",
    }

    def handle_request_device_prompt(
        self,
        context: str,
        prompt: str,
        accept: bool,
        device: str | UnsetType = UNSET,
    ) -> Any:
        """Execute bluetooth.handleRequestDevicePrompt (internal, unsupported)."""
        params = HandleRequestDevicePromptParameters.build(
            context=context,
            prompt=prompt,
            accept=accept,
            device=device,
        )
        return self._execute("bluetooth.handleRequestDevicePrompt", params=params, result=None)

    def simulate_adapter(
        self,
        context: str,
        state: SimulateAdapterParametersState,
        le_supported: bool | UnsetType = UNSET,
    ) -> Any:
        """Execute bluetooth.simulateAdapter (internal, unsupported)."""
        params = SimulateAdapterParameters(context=context, le_supported=le_supported, state=state)
        return self._execute("bluetooth.simulateAdapter", params=params, result=None)

    def disable_simulation(self, context: str) -> Any:
        """Execute bluetooth.disableSimulation (internal, unsupported)."""
        params = DisableSimulationParameters(context=context)
        return self._execute("bluetooth.disableSimulation", params=params, result=None)

    def simulate_preconnected_peripheral(
        self,
        context: str,
        address: str,
        name: str,
        manufacturer_data: list[BluetoothManufacturerData],
        known_service_uuids: list[str],
    ) -> Any:
        """Execute bluetooth.simulatePreconnectedPeripheral (internal, unsupported)."""
        params = SimulatePreconnectedPeripheralParameters(
            context=context,
            address=address,
            name=name,
            manufacturer_data=manufacturer_data,
            known_service_uuids=known_service_uuids,
        )
        return self._execute("bluetooth.simulatePreconnectedPeripheral", params=params, result=None)

    def simulate_advertisement(self, context: str, scan_entry: SimulateAdvertisementScanEntryParameters) -> Any:
        """Execute bluetooth.simulateAdvertisement (internal, unsupported)."""
        params = SimulateAdvertisementParameters(context=context, scan_entry=scan_entry)
        return self._execute("bluetooth.simulateAdvertisement", params=params, result=None)

    def simulate_gatt_connection_response(self, context: str, address: str, code: int) -> Any:
        """Execute bluetooth.simulateGattConnectionResponse (internal, unsupported)."""
        params = SimulateGattConnectionResponseParameters(context=context, address=address, code=code)
        return self._execute("bluetooth.simulateGattConnectionResponse", params=params, result=None)

    def simulate_gatt_disconnection(self, context: str, address: str) -> Any:
        """Execute bluetooth.simulateGattDisconnection (internal, unsupported)."""
        params = SimulateGattDisconnectionParameters(context=context, address=address)
        return self._execute("bluetooth.simulateGattDisconnection", params=params, result=None)

    def simulate_service(self, context: str, address: str, uuid: str, type: SimulateServiceParametersType) -> Any:
        """Execute bluetooth.simulateService (internal, unsupported)."""
        params = SimulateServiceParameters(context=context, address=address, uuid=uuid, type=type)
        return self._execute("bluetooth.simulateService", params=params, result=None)

    def simulate_characteristic(
        self,
        context: str,
        address: str,
        service_uuid: str,
        characteristic_uuid: str,
        type: SimulateCharacteristicParametersType,
        characteristic_properties: CharacteristicProperties | UnsetType = UNSET,
    ) -> Any:
        """Execute bluetooth.simulateCharacteristic (internal, unsupported)."""
        params = SimulateCharacteristicParameters(
            context=context,
            address=address,
            service_uuid=service_uuid,
            characteristic_uuid=characteristic_uuid,
            characteristic_properties=characteristic_properties,
            type=type,
        )
        return self._execute("bluetooth.simulateCharacteristic", params=params, result=None)

    def simulate_characteristic_response(
        self,
        context: str,
        address: str,
        service_uuid: str,
        characteristic_uuid: str,
        type: SimulateCharacteristicResponseParametersType,
        code: int,
        data: list[int] | UnsetType = UNSET,
    ) -> Any:
        """Execute bluetooth.simulateCharacteristicResponse (internal, unsupported)."""
        params = SimulateCharacteristicResponseParameters(
            context=context,
            address=address,
            service_uuid=service_uuid,
            characteristic_uuid=characteristic_uuid,
            type=type,
            code=code,
            data=data,
        )
        return self._execute("bluetooth.simulateCharacteristicResponse", params=params, result=None)

    def simulate_descriptor(
        self,
        context: str,
        address: str,
        service_uuid: str,
        characteristic_uuid: str,
        descriptor_uuid: str,
        type: SimulateDescriptorParametersType,
    ) -> Any:
        """Execute bluetooth.simulateDescriptor (internal, unsupported)."""
        params = SimulateDescriptorParameters(
            context=context,
            address=address,
            service_uuid=service_uuid,
            characteristic_uuid=characteristic_uuid,
            descriptor_uuid=descriptor_uuid,
            type=type,
        )
        return self._execute("bluetooth.simulateDescriptor", params=params, result=None)

    def simulate_descriptor_response(
        self,
        context: str,
        address: str,
        service_uuid: str,
        characteristic_uuid: str,
        descriptor_uuid: str,
        type: SimulateDescriptorResponseParametersType,
        code: int,
        data: list[int] | UnsetType = UNSET,
    ) -> Any:
        """Execute bluetooth.simulateDescriptorResponse (internal, unsupported)."""
        params = SimulateDescriptorResponseParameters(
            context=context,
            address=address,
            service_uuid=service_uuid,
            characteristic_uuid=characteristic_uuid,
            descriptor_uuid=descriptor_uuid,
            type=type,
            code=code,
            data=data,
        )
        return self._execute("bluetooth.simulateDescriptorResponse", params=params, result=None)
