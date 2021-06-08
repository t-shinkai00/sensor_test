from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
from fluent import sender
from functools import reduce

logger = sender.FluentSender('sensor', host = '127.0.0.1', port = 24224)
sensor = Adafruit_AMG88xx()
sleep(.1)

def mean(list_i):
  total =  reduce(lambda a, b:a+b, list_i)
  len_i = len(list_i)
  return total / len_i

if __name__ == "__main__":
  while(1):
    sensor_val_list = sensor.readPixels()
    mean_tmp = mean(sensor_val_list)
    
    ret_dict = {
      'mean_tmp': mean_tmp,
      'value': sensor_val_list
    }

    logger.emit('grideye', ret_dict)
    sleep(3)