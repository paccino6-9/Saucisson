from flask import Flask, jsonify, request
from relay_control import RelayController
from bme280_sensor import BME280Sensor
import config

app = Flask(__name__)

relay_controller = RelayController()
bme280_sensor = BME280Sensor()

@app.route('/api/relay/<int:relay_id>/<string:action>', methods=['POST'])
def control_relay(relay_id, action):
    if action == 'on':
        relay_controller.turn_on_relay(relay_id)
        return jsonify({'status': 'success', 'message': f'Relay {relay_id} turned on.'}), 200
    elif action == 'off':
        relay_controller.turn_off_relay(relay_id)
        return jsonify({'status': 'success', 'message': f'Relay {relay_id} turned off.'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid action.'}), 400

@app.route('/api/sensor/data', methods=['GET'])
def get_sensor_data():
    temperature = bme280_sensor.read_temperature()
    humidity = bme280_sensor.read_humidity()
    pressure = bme280_sensor.read_pressure()
    return jsonify({
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure
    }), 200

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)