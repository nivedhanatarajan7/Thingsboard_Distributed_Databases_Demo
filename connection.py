from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
from pyignite import Client

client = Client()
client.connect('127.0.0.1', 10800)

#Create cache
my_cache = client.get_cache("testCache")

my_cache.put("heartrate", 60)

#Get value from cache
result = my_cache.get("heartrate")

telemetry = {"heartrate": result}

print(telemetry)

#Connect to Thingsboard and send telemetry data
client = TBDeviceMqttClient("demo.thingsboard.io", username="eqEy6xdQPTPnCOAFSUrL")
client.connect()
client.send_telemetry(telemetry) 
result = client.send_telemetry(telemetry)
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
client.disconnect()