settings = {}

# micropython default state needs to be high for some reason
settings['default_state'] = 1
settings['debug'] = False
settings['hostname'] = 'shadow_box'

settings['wifi'] = {}
settings['mqtt'] = {}

settings['wifi']['ssid'] = 'thehouse'
settings['wifi']['pass'] = 'turtlezombiehouse'

settings['mqtt']['base_topic'] = b'controller/02'
settings['mqtt']['base_topic_subscribe'] = b'controller/02/input/#'
settings['mqtt']['base_topic_status'] = b'controller/02'
settings['mqtt']['host'] = b"192.168.1.104"
settings['mqtt']['user'] = b'autohome'
settings['mqtt']['pass'] = b'turtlezombiehouse'

seconds = 10
settings['mqtt']['update_interval'] = seconds * 60 * 60  # micro seconds to seconds
