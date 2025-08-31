class BME280Sensor:
    def __init__(self, bus_number=1, address=0x76):
        import smbus2
        from bme280 import BME280
        self.bus = smbus2.SMBus(bus_number)
        self.bme280 = BME280(i2c_dev=self.bus, address=address)

    def read_temperature(self):
        return self.bme280.get_temperature()

    def read_humidity(self):
        return self.bme280.get_humidity()

    def read_pressure(self):
        return self.bme280.get_pressure()