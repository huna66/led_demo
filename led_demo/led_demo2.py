import RPi.GPIO 
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)


VCC=2
D1=3
D2=18
D3=23
D4=24
LED_A = 25
LED_B = 8
LED_C = 7
LED_D = 12
LED_E = 16
LED_F = 20
LED_G = 21
LED_DP = 26

#RPi.GPIO.cleanup()


RPi.GPIO.setup(VCC, RPi.GPIO.OUT)
RPi.GPIO.setup(D1, RPi.GPIO.OUT)
RPi.GPIO.setup(D2, RPi.GPIO.OUT)
RPi.GPIO.setup(D3, RPi.GPIO.OUT)
RPi.GPIO.setup(D4, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)

RPi.GPIO.output(VCC, True)


def select( ):
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
    RPi.GPIO.output(LED_DP, True)
    return 0



def Digi_num(DIG_No,num):
    RPi.GPIO.output(D1,True)
    RPi.GPIO.output(D2,True)
    RPi.GPIO.output(D3,True)
    RPi.GPIO.output(D4,True)
    

    if num==1:
        select()
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        
    elif num==2:
        select()
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_D, False)
    elif num==3:
        select()
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        
    elif num==4:
        select()
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
    elif num==5:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False) 
    elif num==6:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
    elif num==7:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_B, False)
        
    elif num==8:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_B, False)
    elif num==9:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_D, False)
    else:
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_B, False)


    if DIG_No==1:
        RPi.GPIO.output(D1,False)
    elif DIG_No==2:
        RPi.GPIO.output(D2,False)
    elif DIG_No==3:
        RPi.GPIO.output(D3,False)
    elif DIG_No==4:
        RPi.GPIO.output(D4,False)

select()
#Digi_num(DIG_No,num)

while True:
    try:
    
        Temp_date=time.time()
        Real_date=time.ctime(Temp_date)
        Real_time=Real_date.split()[3]
        Hour_all=Real_time.split(":")[0]
        Min_all=Real_time.split(":")[1]
        Hour_D1=Hour_all[0]
        Hour_D2=Hour_all[1]
        Min_D1=Min_all[0]
        Min_D2=Min_all[1]
        Digi_num(1,int(Hour_D1))
        time.sleep(0.001)
        Digi_num(2,int(Hour_D2))
        RPi.GPIO.output(LED_DP,RPi.GPIO.HIGH)
        time.sleep(0.001)
        Digi_num(3,int(Min_D1))
        time.sleep(0.001)
        Digi_num(4,int(Min_D2))
        time.sleep(0.001)
        
    except KeyboardInterrupt:
        break

RPi.GPIO.cleanup()
