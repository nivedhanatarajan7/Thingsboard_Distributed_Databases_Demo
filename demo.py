from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
from pyignite import Client

client = Client()
client.connect('127.0.0.1', 10800)

#Create cache
my_cache = client.get_cache("testCache")

#Put value in cache
my_cache.put("heartrate", 63)

#Get value from cache
result = my_cache.get("heartrate")

telemetry = {"heartrate": result}

print(telemetry)

client = TBDeviceMqttClient("demo.thingsboard.io", username="eqEy6xdQPTPnCOAFSUrL")
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
# Disconnect from ThingsBoard
client.disconnect()