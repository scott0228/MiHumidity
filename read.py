from datetime import datetime
from bleak import BleakClient
import asyncio
import struct
import logging

async def read_characteristic_value(address, service_uuid, characteristic_uuid):
    async with BleakClient(address, timeout=60) as client:
        value = await client.read_gatt_char(characteristic_uuid)
        humidity = value[2]
        voltage = struct.unpack('H', value[3:5])[0]/ 1000
        batteryLevel = round((voltage - 2.1),2) * 100
        temperature = struct.unpack('H', value[:2])[0] / 100

        print(f"Tempterature: {temperature}°C")
        print(f"    Humidity: {humidity}%")
        print(f"batteryLevel: {batteryLevel}%")
        print(f"        Time: {datetime.now().strftime('%H:%M:%S')}")

log_level = logging.INFO
logging.basicConfig(
    level=log_level,
    format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
)

address = "A99E3E25-FE1B-1B67-F090-613DF306A501"  # Replace with the actual address of the Bluetooth device
service_uuid = "0000fe95-0000-1000-8000-00805f9b34fb"  # Replace with the UUID of the service
characteristic_uuid = "EBE0CCC1-7A0A-4B0C-8A1A-6FF2997DA3A6"  # Replace with the UUID of the characteristic

asyncio.run(read_characteristic_value(address, service_uuid, characteristic_uuid))

# A4:C1:38:EF:5D:B6: MJWSD05MMC A99E3E25-FE1B-1B67-F090-613DF306A501
# AdvertisementData(local_name='MJWSD05MMC', service_data={'0000fe95-0000-1000-8000-00805f9b34fb': b'\x10Y2(!\xb6]\xef8\xc1\xa4'}, rssi=-80)
# A4:C1:38:1F:01:A6: LYWSD03MMC 6ADC354E-D6AB-880F-C007-48C0B4D14B7A
# AdvertisementData(local_name='LYWSD03MMC', service_data={'0000fe95-0000-1000-8000-00805f9b34fb': b'0X[\x05\x01\xa6\x01\x1f8\xc1\xa4(\x01\x00'}, rssi=-71)
