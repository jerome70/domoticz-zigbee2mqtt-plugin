from adapters.boolean_sensor import BooleanSensor

class SensorWleak(BooleanSensor):
    def __init__(self, devices):
        super().__init__(devices)
        self.sensor_type = self.SENSOR_TYPE_CONTACT
        self.senor_value_key = 'water_leak'

    def get_device_value(self, sensor_value):
        return 0 if sensor_value else 1