import sensor

import threading 
th1 = threading.Thread(target=sensor.sensor,kwargs={'id':'d1','typ':'heartbeat','loc':'obh_111','ip':'0.0.0.0','port':'9557'})
th2 = threading.Thread(target=sensor.sensor,kwargs={'id':'d2','typ':'heartbeat','loc':'obh_112','ip':'0.0.0.0','port':'9557'})
th3 = threading.Thread(target=sensor.sensor,kwargs={'id':'d10','typ':'heartbeat','loc':'obh_1110','ip':'0.0.0.0','port':'9557'})
th4 = threading.Thread(target=sensor.sensor,kwargs={'id':'d3','typ':'heartbeat','loc':'obh_113','ip':'0.0.0.0','port':'9557'})
th5 = threading.Thread(target=sensor.sensor,kwargs={'id':'d4','typ':'heartbeat','loc':'obh_114','ip':'0.0.0.0','port':'9557'})
th6 = threading.Thread(target=sensor.sensor,kwargs={'id':'d5','typ':'heartbeat','loc':'obh_115','ip':'0.0.0.0','port':'9557'})
th7 = threading.Thread(target=sensor.sensor,kwargs={'id':'d6','typ':'heartbeat','loc':'obh_116','ip':'0.0.0.0','port':'9557'})
th8 = threading.Thread(target=sensor.sensor,kwargs={'id':'d7','typ':'heartbeat','loc':'obh_117','ip':'0.0.0.0','port':'9557'})
th9 = threading.Thread(target=sensor.sensor,kwargs={'id':'d8','typ':'heartbeat','loc':'obh_118','ip':'0.0.0.0','port':'9557'})
th10 = threading.Thread(target=sensor.sensor,kwargs={'id':'d9','typ':'heartbeat','loc':'obh_119','ip':'0.0.0.0','port':'9557'})
# sensor.sensor('d1','numeric_attandance','obh_112','0.0.0.0','9557')
th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()
th9.start()
th10.start()
