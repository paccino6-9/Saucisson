class Config:
    RELAY_PINS = {
        'humidifier': 17,
        'fan': 27,
        'auxiliary': 22
    }
    HUMIDITY_THRESHOLD = 60  # in percentage
    TEMPERATURE_THRESHOLD = 20  # in Celsius
    BME280_I2C_ADDRESS = 0x76  # Default I2C address for BME280
    UPDATE_INTERVAL = 10  # in seconds for sensor data updates