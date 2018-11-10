configs = {}

# micropython default state needs to be high for some reason
configs['default_state'] = 1
configs['debug'] = True
configs['hostname'] = 'garden_sensors'

configs['wifi'] = {}
configs['mqtt'] = {}

configs['wifi']['ssid'] = 'thehouse'
configs['wifi']['pass'] = 'turtlezombiehouse'

configs['mqtt']['base_topic'] = b'garden_sensors/02'
configs['mqtt']['base_topic_subscribe'] = b'garden_sensors/02/input/#'
configs['mqtt']['base_topic_status'] = b'garden_sensors/02'
configs['mqtt']['host'] = b"192.168.1.104"
configs['mqtt']['user'] = b'autohome'
configs['mqtt']['pass'] = b'turtlezombiehouse'

minutes = 15 * 60
# seconds = 10
configs['mqtt']['update_interval'] = minutes * 60 * 60  # micro seconds to seconds