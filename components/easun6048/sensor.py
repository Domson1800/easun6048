import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.components import sensor, text_sensor
from esphome.const import (
    CONF_BATTERY_VOLTAGE,
    CONF_ID,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_CURRENT_AC,
    ICON_EMPTY,
    ICON_FLASH,
    ICON_PERCENT,
    ICON_POWER,
    ICON_TIMELAPSE,
    UNIT_AMPERE,
    UNIT_EMPTY,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_WATT_HOURS,
    UNIT_CELSIUS,
    ICON_FAN
)


from . import CONF_EASUN_6048_ID, EASUN6048Component
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_EASUN_6048_ID): cv.use_id(
            EASUN6048Component
        ),
        cv.Optional("voltage_sensor"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional("pv_sensor"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
        ),
        cv.Optional("current_sensor"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional("temp_sensor"): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            icon=ICON_FAN,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_EMPTY,
        ),
        cv.Optional("power_sensor"): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_POWER,
        ),
    }
).extend(uart.UART_DEVICE_SCHEMA)

def to_code(config):
    var = yield cg.get_variable(config[CONF_EASUN_6048_ID])
    if "voltage_sensor" in config:
        sens = yield sensor.new_sensor(config["voltage_sensor"])
        cg.add(var.set_voltage_sensor(sens))
    if "pv_sensor" in config:
        sens = yield sensor.new_sensor(config["pv_sensor"])
        cg.add(var.set_pv_sensor(sens))
    if "current_sensor" in config:
        sens = yield sensor.new_sensor(config["current_sensor"])
        cg.add(var.set_current_sensor(sens))
    if "temp_sensor" in config:
        sens = yield sensor.new_sensor(config["temp_sensor"])
        cg.add(var.set_temp_sensor(sens))
    if "power_sensor" in config:
        sens = yield sensor.new_sensor(config["power_sensor"])
        cg.add(var.set_power_sensor(sens))
