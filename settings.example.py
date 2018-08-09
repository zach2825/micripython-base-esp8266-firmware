settings = {}

# micropython default state needs to be high for some reason
settings['default_state'] = 1
settings['debug'] = False
# NEWER MICROPYTHON SUPPORTS THIS FEATURE version 1.9.8 and above. I have to use an older version so I could not
# benefit from this.
settings['hostname'] = '__ESP8266 HOSTNAME__'

settings['wifi'] = {}
settings['mqtt'] = {}

settings['wifi']['ssid'] = '__WIFI BSSID__'
settings['wifi']['pass'] = '__WIFI PASSWORD__'

settings['mqtt']['base_topic'] = b'__BASE TOPIC__'
settings['mqtt']['base_topic_subscribe'] = settings['mqtt']['base_topic'] + b'/input/#'
settings['mqtt']['base_topic_status'] = settings['mqtt']['base_topic'] + b'/status'
settings['mqtt']['host'] = b"__MQTT HOST IP ADDRESS__"
settings['mqtt']['user'] = b'_-MQTT USERNAME__'
settings['mqtt']['pass'] = b'__MQTT PASSWORD__'

# How often to do the status update to mqtt about the ip address and other random things.
seconds = 10
settings['mqtt']['update_interval'] = seconds * 60 * 60  # micro seconds to seconds