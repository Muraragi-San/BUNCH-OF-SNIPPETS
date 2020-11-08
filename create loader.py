import time
def loadercr(text='Loading',timeslot=3,counttime=0):
                    allship=0
                    start = time.time()
                    k=0
                    while k<timeslot:
                      
                      start2 = time.time()

                      if allship==5:
                          allship=0
                          continue
                      else:

                        print(f"""{text}{'.'*allship}{" "*(len(text)-allship)}\r""",end='')

                      time.sleep(0.23)
                      end2= time.time()
                      k+=end2-start2
                    
                      allship+=1    
                                   
                    print(f'{" "*(len(text)+4)}\r')
                    end=time.time()
                    if counttime==1:
                        print('Time Taken :',end-start)
