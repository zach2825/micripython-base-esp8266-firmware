def mqtt_status(station):
	from machine import Pin
	import json
	from settings import configs

	# micropython default state needs to be high for some reason
	default_state = configs['default_state']

	pins = {
	0: Pin(16, Pin.OUT, value=default_state),
	1: Pin(5, Pin.OUT, value=default_state),
	2: Pin(4, Pin.OUT, value=default_state),
	3: Pin(0, Pin.OUT, value=default_state),
	4: Pin(2, Pin.OUT, value=default_state),
	5: Pin(14, Pin.OUT, value=default_state),
	6: Pin(12, Pin.OUT, value=default_state),
	7: Pin(13, Pin.OUT, value=default_state),
	# 8: machine.Pin(15, machine.Pin.OUT, value=0),
	}

	message = {
	"ifconfig": station.ifconfig(),
	'ssid'    : configs['wifi']['ssid'],
	'pins'    : {
		"PIN 0": pins[0].value(),
		"PIN 1": pins[1].value(),
		"PIN 2": pins[2].value(),
		"PIN 3": pins[3].value(),
		"PIN 4": pins[4].value(),
		"PIN 5": pins[5].value(),
		"PIN 6": pins[6].value(),
		"PIN 7": pins[7].value(),
	}
	}
	return json.dumps(message)


def start_timers(mqtt_server, connect_wifi, station):
	from machine import Timer
	from settings import configs

	tim = Timer(-1)

	# check wifi - make sure I'm still connected
	# tim.init(
	# 	period=configs['mqtt']['update_interval'] - 1000,
	# 	mode=Timer.PERIODIC,
	# 	callback=lambda t: connect_wifi
	# )

	# # Public my status to the mqtt status topic
	# tim.init(
	# 		period=configs['mqtt']['update_interval'],
	# 		mode=Timer.PERIODIC,
	# 		callback=lambda t: mqtt_server.publish(configs['mqtt']['base_topic'], mqtt_status(station))
	# )
	#
	# # There is some random connection but after a few days the chip will lock up because of the mqtt subscription.
	# # so everyday disconnect and re-connect to mqtt and the wifi
	# tim.init(
	# 		period=24 * 60 * 60 * 60 * 60,  # hours * minutes * seconds * etc to make this trigger every 24 hours
	# 		mode=Timer.PERIODIC,
	# 		callback=lambda t: mqtt_server.disconnect()
	# )
