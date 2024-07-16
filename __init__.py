import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ['uart']
AUTO_LOAD = ["sensor", "text_sensor"]

empty_uart_sensor_ns = cg.esphome_ns.namespace('easun_6048')
EASUN6048Component = empty_uart_sensor_ns.class_('EASUN6048Component', uart.UARTDevice, cg.Component)

CONF_EASUN_6048_ID = "easun_6048_id"

CONFIG_SCHEMA = uart.UART_DEVICE_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(EASUN6048Component),
    }
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)