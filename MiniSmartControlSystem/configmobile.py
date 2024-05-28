# {
#   "totalChannels": 1,
#   "totalOccupancy": 0,
#   "channels": {
#     "Channel-Barcelona": {
#       "occupants": [{
#           "uuid": "Amanda-device"
#         }
#           ],
#       "name": "Channel-Barcelona",
#       "occupancy": 0
#     }
#   }
# }

import os
import time

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener


# this will print out the subscription status to console
class Listener(SubscribeListener):
    def status(self, pubnub, status):
        print(f'Status: \n{status.category.name}')


# here we create configuration for our pubnub instance
config = PNConfiguration()
config.subscribe_key = 'sub-c-76ef37b9-dede-433d-b2f5-c51659bec9b9'
config.publish_key = 'pub-c-bf1aee1d-fae2-4524-a378-840ab77025e6'
config.user_id = 'Amanda-device'
config.enable_subscribe = True
config.daemon = True

pubnub = PubNub(config)
pubnub.add_listener(Listener())

subscription = pubnub.channel('Channel-Barcelona').subscription()
subscription.on_message = lambda message: print(f'Message from {message.publisher}: {message.message}')
subscription.subscribe()

time.sleep(1)
publish_result = pubnub.publish().channel("example").message("Hello from MSA").sync()

time.sleep(3)

pubnub.stop()
time.sleep(1)
print('Bye.')