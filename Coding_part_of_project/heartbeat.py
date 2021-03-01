import conf, json, time
from boltiot import Sms, Bolt
minimum_limit = 67 #the minimum threshold of heart rate
maximum_limit = 110 #the maximum threshold of heart rate
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
   response = mybolt.analogRead('A0')
   data = json.loads(response)
   sensor_value1 = int(data['value'])
   sensor_value1 = sensor_value1
   print ("The current Heartbeat of patient is "+ str(sensor_value1)+" BPM. And the Sensor Value is "+data['value'])
   sensor_value=0
   try:
       sensor_value = int(data['value'])
   except e:
       print("There was an error while parsing the response: ",e)
       continue
   try:
       if sensor_value > maximum_limit or sensor_value < minimum_limit:
           print ("The heartbeat is abnormal.Sending SMS")
           response = sms.send_sms("HeartBeat abnormal. The Current heartbeat is " + str(sensor_value1)+ " BPM")
           print("This is the response for SMS ",response)
   except Exception as e:
       print ("Error",e)
   time.sleep(5)