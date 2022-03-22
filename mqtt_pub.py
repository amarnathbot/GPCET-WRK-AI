import paho.mqtt.client as mqtt

pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)

print('guess why')

pub_client.subscribe('gpcet/ai')

def notification(sub_client,userdata,msg):
       print(msg.payload)
pub_client.on_message=notification
pub_client.loop_forever()