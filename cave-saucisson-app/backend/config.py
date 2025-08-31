import os


def get_env_var(name, default=None, cast=str):
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return cast(value)
    except Exception:
        return default


class Config:
    RELAY_PINS = {
        'humidifier': get_env_var('RELAY_PIN_HUMIDIFIER', 17, int),
        'fan': get_env_var('RELAY_PIN_FAN', 27, int),
        'auxiliary': get_env_var('RELAY_PIN_AUXILIARY', 22, int)
    }
    HUMIDITY_THRESHOLD = get_env_var('HUMIDITY_THRESHOLD', 60, int)  # in percentage
    TEMPERATURE_THRESHOLD = get_env_var('TEMPERATURE_THRESHOLD', 20, int)  # in Celsius
    BME280_I2C_ADDRESS = get_env_var('BME280_I2C_ADDRESS', 0x76, lambda v: int(v, 16))  # Default I2C address for BME280
    UPDATE_INTERVAL = 10  # in seconds for sensor data updates