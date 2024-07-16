#include "easun6048.h"
#include "esphome/core/log.h"
#include "esphome/core/hal.h"
namespace esphome {
namespace easun_6048 {

static const char *TAG = "easun_6048";
const int BUFFER_SIZE = 18;
u_int8_t buf[BUFFER_SIZE];
void EASUN6048Component::loop() {

  if (!available())
    return;
  while (available()) {
    uint8_t c;
    read_byte(&c);
    if(c == 125) {
      read_byte(&c);
      if(c != 16){
        return;
      }
      read_array(buf, BUFFER_SIZE);
      decodeBuffer();
    }
  }
}
int bufferCountr=0;
float b0;
float current;
float batV;
float PvV;
float power;
int temp;
void EASUN6048Component::decodeBuffer(){
        batV = float(processByte(6) * 256 + processByte(7))/10;
        PvV = float(processByte(8) * 256 + processByte(9))/10;
        current = float(processByte(10) * 256 + processByte(11))/10;
        temp = processByte(12);
        power = batV*current;
        //sanity filters
        if (batV < 10.0f || batV > 60.0f) return;
        if (current > 70.0f) return;
        if (power > 3000.0f) return;
        if (PvV > 200.0f) return;
        if (this->voltage_sensor_ != nullptr) {
            this->voltage_sensor_->publish_state(batV);
        }
        if (this->pv_sensor_ != nullptr) {
            this->pv_sensor_->publish_state(PvV);
        }
        if (this->current_sensor_ != nullptr) {
            this->current_sensor_->publish_state(current);
        }
        if (this->temp_sensor_ != nullptr) {
            this->temp_sensor_->publish_state(temp);
        }
        if (this->power_sensor_ != nullptr) {
            this->power_sensor_->publish_state(power);
        }
}

char *ptr;
long EASUN6048Component::processByte(int pointer){
        String a = String(buf[pointer], HEX);        
        if(a.length()>2){          
          a = a.substring(a .length()-2);
          return strtoul(a.c_str(), &ptr, 16);          
          }
  else{
    return (long)buf[pointer];
    }
  
  }

  void EASUN6048Component::dump_config(){
    ESP_LOGCONFIG(TAG, "EASUN 6048 sensor");
    LOG_SENSOR("  ", "Voltage", this->voltage_sensor_);
}
    }
}