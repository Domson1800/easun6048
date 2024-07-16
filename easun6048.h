#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
    namespace easun_6048 {
        class EASUN6048Component : public uart::UARTDevice, public Component {
        public:
            void loop() override;
            void dump_config() override;
            void set_voltage_sensor(sensor::Sensor *voltage_sensor) {
                voltage_sensor_ = voltage_sensor;
            }
            void set_pv_sensor(sensor::Sensor *pv_sensor) {
                pv_sensor_ = pv_sensor;
            }
            void set_current_sensor(sensor::Sensor *current_sensor) {
                current_sensor_ = current_sensor;
            }
            void set_temp_sensor(sensor::Sensor *temp_sensor) {
                temp_sensor_ = temp_sensor;
            }
            void set_power_sensor(sensor::Sensor *power_sensor) {
                power_sensor_ = power_sensor;
            }
        protected:
            void decodeBuffer();
            long processByte(int pointer);
            sensor::Sensor *voltage_sensor_{nullptr};
            sensor::Sensor *pv_sensor_{nullptr};
            sensor::Sensor *current_sensor_{nullptr};
            sensor::Sensor *temp_sensor_{nullptr};
            sensor::Sensor *power_sensor_{nullptr};
    };
}
}