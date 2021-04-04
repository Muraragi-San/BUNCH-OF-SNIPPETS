def tablecr(tablecolumninfo,records,disphead=1,ifcenter=0,showtotalentries=0,ifsrno=0,ifsplit=0,tdisplay='T.ENTRIES',emptytobedisplayedas='─'):
  tcl,re,etd=tablecolumninfo,records,emptytobedisplayedas
  lengt=len(tcl)
  myinfo=[]
  checker=[]
  myinfo2=[]
  checker2=[]
  if ifsrno==0:
     head=""
     calculee=0
  else:
    head='|___Sr_NO___|'
    calculee=1
    
    lengt+=1
  calcul=0
  copy=calculee
  head2=head
  if ifsplit==0:
    for inf in tcl:
      
      inf[0]=inf[0].split('|{special}|')
      lgtcname=len(inf[0][0])
      mentionedlgt=inf[1]
      
      sk=0
      if lgtcname>mentionedlgt:
          mentionedlgt=lgtcname
          diff2=0
          diff1=0
      else:
          diff=mentionedlgt-lgtcname
          
          if ifcenter==0:          
              diff2=diff
              if diff==0:
                  diff2=0
        
          else:        
             if diff%2!=0:
                    
                    diff+=1
                    
             diff1,diff2=(diff//2),(diff//2)
         
      if lgtcname==0 and mentionedlgt==0: 
              pass
      else:        
        if calculee==0:
           if ifcenter==0:
                 head+=f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                 checker.append(len(f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
           else:
               disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               head+=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               checker.append(len(f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
        else:
          if ifcenter==0: 
             head+=f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
             checker.append(len(f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
          else:
               disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               head+=f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
               checker.append(len(f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
        
        if len(inf[0])==2 and ifcenter!=0:
            myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),disvar.index(inf[0][0][1])-2])              
        else:
          if ifcenter==0:
            myinfo.append([mentionedlgt,0])
          else:
             
              myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),0])
        calcul+=1
        calculee+=1
    if len(head) > 167:
     
      print(f"The Column length is exceeding the current limit i.e 167 characters.\nYour length is {len(head)}||It should be at most 167 characters\nTry reducing {len(head)-167} character(s)")
  
    else:     
            if showtotalentries!=0:
                  a=len(re)
                  dig=len(str(a))
                  print("", ("_"*(len(tdisplay)+3)), "_"*13)
                  print(f'{"|__"+tdisplay+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}')
                
            if disphead==1:
              print("", "_"*(len(head)-2))
              print(head)
        
        
            dio11=0
            for reco in re:
                dio11+=1
                if ifsrno!=0:
                   
                   if dio11>=100000:
                        count="ERR"
                   elif dio11<10:
                     count="0"+str(dio11)
                   else:
                     count=str(dio11)
                   
                   strire=''
                   
                   strire+=f'{"|    "+count+" "*(7-len(str(count)))+"|"}'
                   dioo=1
                   
                else:
                    strire=''
                    dioo=0
                dio=0
                for recor in reco:
                    recor=str(recor)
                    if recor=='':
                        recor=etd
                    elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo[dio][0]:
                            recor='Err'
                    elif len(recor)>myinfo[dio][0]:
                        recor=recor[0:(myinfo[dio][0])]
                   
                    if dioo==0:
                        strire+=f"{'| '+(' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"
                          
                    else:
                        strire+=f"{(' '+' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"
                        
                    dio+=1
                    dioo+=1
                    
                   
                print(strire)
            print("╹"+"─"*(len(head)-2)+"╹")       
       
     
     
  else:
      l1=[]
      l2=[]
      oof=re.index('|{rebreak}|')
      r1=re[0:oof]
      r2=re[(oof+1):len(re)]
      a=0
      for jsij in tcl:
         if jsij==['{break}']:
           if a==0:
             l2=l1
             l1=[]
           else:
             pass
         else:
           l1.append(jsij)
      a=0              
      for inf in l2:
          
          inf[0]=inf[0].split('|{special}|')
          lgtcname=len(inf[0][0])
          mentionedlgt=inf[1]
      
          sk=0
          if lgtcname>mentionedlgt:
            mentionedlgt=lgtcname
            diff2=0
            diff1=0
          else:
              diff=mentionedlgt-lgtcname
          
              if ifcenter==0:          
                diff2=diff
                if diff==0:
                   diff2=0
        
              else:        
                 if diff%2!=0:
                    
                    diff+=1
                    
                 diff1,diff2=(diff//2),(diff//2)
         
          if lgtcname==0 and mentionedlgt==0: 
                           pass
          else:        
                if calculee==0:
                    if ifcenter==0:
                        head+=f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                        checker.append(len(f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
                    else:
                       disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       head+=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker.append(len(f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
                else:
                    if ifcenter==0: 
                       head+=f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker.append(len(f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
                    else:
                       disvar=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       head+=f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker.append(len(f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
        
                if len(inf[0])==2 and ifcenter!=0:
                    myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),disvar.index(inf[0][0][1])-2])              
                else:
                   if ifcenter==0:
                      myinfo.append([mentionedlgt,0])
                   else:
                       myinfo.append([mentionedlgt+(checker[calcul]-mentionedlgt),0])
                calcul+=1
                calculee+=1
      calcul=0    
      calculee=copy 
      for inf in l1:
          
          inf[0]=inf[0].split('|{special}|')
          lgtcname=len(inf[0][0])
          mentionedlgt=inf[1]
      
          sk=0
          if lgtcname>mentionedlgt:
            mentionedlgt=lgtcname
            diff2=0
            diff1=0
          else:
              diff=mentionedlgt-lgtcname
          
              if ifcenter==0:          
                diff2=diff
                if diff==0:
                   diff2=0
        
              else:        
                 if diff%2!=0:
                    
                    diff+=1
                    
                 diff1,diff2=(diff//2),(diff//2)
         
          if lgtcname==0 and mentionedlgt==0: 
                           pass
          else:        
                if calculee==0:
                    if ifcenter==0:
                        head2+=f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                        checker2.append(len(f"{'|_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
                    else:
                       disvar2=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       head2+=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker2.append(len(f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-4)
                else:
                    if ifcenter==0: 
                       head2+=f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker2.append(len(f"{'_'+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
                    else:
                       disvar2=f"{'|_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       head2+=f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}"
                       checker2.append(len(f"{'_'+('_'*diff1)+inf[0][0].strip()+('_'*diff2)+'_|'}")-3)
        
                if len(inf[0])==2 and ifcenter!=0:
                    myinfo2.append([mentionedlgt+(checker2[calcul]-mentionedlgt),disvar2.index(inf[0][0][1])-2])              
                else:
                   if ifcenter==0:
                      myinfo2.append([mentionedlgt,0])
                   else:
                       myinfo2.append([mentionedlgt+(checker2[calcul]-mentionedlgt),0])
                calcul+=1
                calculee+=1    
      a=len(r1)
      dig=len(str(a))
      boggline=(head)+(' '*(167-(len(head2)+len(head))))+head2
      closer=' '+('_'*(len(head)-2))+(' '*(167-(len(head2)+len(head))))+'  '+('_'*(len(head2)-2))
      bogline=len(boggline)
      distan=bogline-len(head2)-len(f'{"|__"+tdisplay+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}')
      distan2=' '*(167-(len(head2)+len(head)))
      closer=' '+('_'*(len(head)-2))+(' '*(167-(len(head2)+len(head))))+'  '+('_'*(len(head2)-2))
      if bogline>167:
     
          print(f"The Column length is exceeding the current limit i.e 167 characters.\nYour length is {bogline}||It should be at most 167 characters\nTry reducing {bogline-167} character(s)")
  
      else:
            if showtotalentries!=0:
                 
                  a2=len(r2)
                  dig2=len(str(a2))
                  
                  print(" "+("_"*(len(tdisplay)+3))+"_"*14+' '*distan+"  "+("_"*(len(tdisplay)+3))+"_"*14)
                  print(f'{"|__"+tdisplay+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}'+' '*distan+f'{"|__"+tdisplay+"_|"+"____"+str(a2)+"_"*(9-dig2)+"|"}')
                
            if disphead==1:
              print(closer)
              print(boggline)
        
           
            dio11=0
            if len(r1)>len(r2):
                gr=r1
                sm=r2
            else:
                gr=r2
                sm=r1
            newvar=0
            endingline="╹"+"─"*(len(head)-2)+"╹"+distan2+"╹"+"─"*(len(head2)-2)+"╹"
            for reco in range(len(gr)):
                dio11+=1
                if ifsrno!=0:
                   
                   if dio11>=100000:
                        count="ERR"
                   elif dio11<10:
                     count="0"+str(dio11)
                   else:
                     count=str(dio11)
                   
                   strire=''
                   
                   strire+=f'{"|    "+count+" "*(7-len(str(count)))+"|"}'
                   dioo=1
                   
                else:
                    strire=''
                    dioo=0
                dio=0
                dioo2=dioo
                dio2=dio
                strire2=strire
                if reco<len(sm):
                    for recor in r1[reco]:
                      recor=str(recor)
                      if recor=='':
                        recor=etd
                      elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo[dio][0]:
                            recor='Err'
                        elif len(recor)>myinfo[dio][0]:
                                recor=recor[0:(myinfo[dio][0])]
                      if dioo==0:
                        strire+=f"{'| '+(' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"   
                      else:
                        strire+=f"{(' '+' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}" 
                      dio+=1
                      dioo+=1
                    for recor in r2[reco]:
                      recor=str(recor)
                      if recor=='':
                        recor=etd
                      elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo2[dio2][0]:
                            recor='Err'
                        elif len(recor)>myinfo2[dio2][0]:
                                recor=recor[0:(myinfo2[dio2][0])]
                      if dioo2==0:
                        strire2+=f"{'| '+(' '*myinfo2[dio2][1])+recor.strip()+(' '*(myinfo2[dio2][0]-len(recor)-myinfo2[dio2][1]))+' |'}"  
                      else:
                        strire2+=f"{(' '+' '*myinfo2[dio2][1])+recor.strip()+(' '*(myinfo2[dio2][0]-len(recor)-myinfo2[dio2][1]))+' |'}" 
                      dio2+=1
                      dioo2+=1
                    print(f'{strire+distan2+strire2}')    
                    if reco+1==len(gr):
                          print(endingline)
                        
                else:
                    
                  if len(sm)==len(r1):
                    if newvar==0:
                          strire="╹"+"─"*(len(head)-2)+"╹"
                          endingline=' '*len("╹"+"─"*(len(head)-2)+"╹")+distan2+"╹"+"─"*(len(head2)-2)+"╹"
                    else:
                       strire=f'{" "*len(head)}'
                    for recor in r2[reco]:
                      recor=str(recor)
                      if recor=='':
                        recor=etd
                      elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo2[dio2][0]:
                            recor='Err'
                        elif len(recor)>myinfo2[dio2][0]:
                                recor=recor[0:(myinfo2[dio2][0])]
                      if dioo2==0:
                        strire2+=f"{'| '+(' '*myinfo2[dio2][1])+recor.strip()+(' '*(myinfo2[dio2][0]-len(recor)-myinfo2[dio2][1]))+' |'}"
   
                      else:
                        strire2+=f"{(' '+' '*myinfo2[dio2][1])+recor.strip()+(' '*(myinfo2[dio2][0]-len(recor)-myinfo2[dio2][1]))+' |'}"                        
                      dio2+=1
                      dioo2+=1
                          
                  elif len(sm)==len(r2):
                    if newvar==0:
                          strire2="╹"+"─"*(len(head2)-2)+"╹"
                          endingline="╹"+"─"*(len(head)-2)+"╹"
                    else:
                       strire2=''
                       
                        
                    for recor in r1[reco]:
                      recor=str(recor)
                      if recor=='':
                        recor=etd
                      elif recor.isnumeric() is True:
                        
                        if len(recor)>myinfo[dio][0]:
                            recor='Err'
                        elif len(recor)>myinfo[dio][0]:
                                recor=recor[0:(myinfo[dio][0])]

                      if dioo==0:
                        strire+=f"{'| '+(' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}"  
                      else:
                        strire+=f"{(' '+' '*myinfo[dio][1])+recor.strip()+(' '*(myinfo[dio][0]-len(recor)-myinfo[dio][1]))+' |'}" 
                      dio+=1
                      dioo+=1
                  
                  print(f'{strire+distan2+strire2}')
                  newvar+=1 
                  if reco+1==len(gr):
                        print(endingline)
      print('\n')       
