import time
def loadercr(text='Loading',timeslot=3,counttime=0):
                    allship=0
                    z=text
                    start = time.time()
                    for trialss in range((timeslot*5)+(int(timeslot//1.5))):
                         
                      
                      if allship==0:
                        z=f"{text}.{' '*(len(text)-1)}"
                      elif allship==1:
                        z=f'{text}..{" "*(len(text)-2)}'
                      elif allship==2:
                          z=f'{text}...{" "*(len(text)-3)}'
                      elif allship==3:
                          z=f'{text}....{" "*(len(text)-4)}'

                      allship+=1

                      if allship==5:
                          allship=0
                      else:
                        print(f'{z}\r',end='')
                        time.sleep(0.23)                  
                    print(f'{" "*(len(text)+4)}\r')
                    end=time.time()
                    if counttime==1:
                        print('Time Taken :',end-start)
    
