class RelayController:
    def __init__(self):
        self.relay_pins = {
            'humidifier': 17,  # GPIO pin for humidifier relay
            'fan': 27,         # GPIO pin for fan relay
            'auxiliary': 22    # GPIO pin for auxiliary relay
        }
        self.setup_relays()

    def setup_relays(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        for pin in self.relay_pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def turn_on_relay(self, relay_name):
        if relay_name in self.relay_pins:
            import RPi.GPIO as GPIO
            GPIO.output(self.relay_pins[relay_name], GPIO.HIGH)

    def turn_off_relay(self, relay_name):
        if relay_name in self.relay_pins:
            import RPi.GPIO as GPIO
            GPIO.output(self.relay_pins[relay_name], GPIO.LOW)

    def cleanup(self):
        import RPi.GPIO as GPIO
        GPIO.cleanup()