#To know how to use the function read below!!!

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


#The function ends here



#Function :
#tablecr(tablecolumninfo,records,disphead=1,ifcenter=0,showtotalentries=0,ifsrno=0,ifsplit=0,tdisplay='T.ENTRIES',emptytobedisplayedas='─')
  
"""
*Note - To enable something use 1 and to disable it use 0
*Note - The maximum columns length should be at most 167 characters.This will be affected when using Sr.No and ifcenter options.
SECTION-1
  #This deals with single table only
  
  
  #tablecolumninfo is where the table column names along with their size in the form of nested lists go to.
         
         For eg - 
            columnamelist = [['AGE',5],['BG',3],['PASS',4]]
         
      *Note-the column info should only be in list format and none other.
      
  #records is where the records in the form of nested lists or tuples should go to.Records can be either lists or tuples
            
            For eg(related to above) - 
                recordlist = [['5','O+','P'],('12','B+','F'),['12','A+','F']]
                                                              Or
                             (5','O+','P'],('12','B+','F'),['12','A+','F'])
                                              
            *Note-make sure the each record has equal no. of elements as the number of columns
  
  #disphead is whether you want to display the column names or not.It has been set as enabled by default
  
  #ifcenter is whether you want the column names to be in the center of the block or not.This has been disabled by default.
  
  #showtotalentries is whether you want to show the total number of records in the table or not.It has been disabled by default.
  
  #ifsrno is if you want a serial number or record number displayed beside your other columns.It has been disabled by default.
  
  #ifsplit is if you want two tables that are split.It has been disabled by default. *Note - See section-2 to know how it works
  
  #tdisplay is whether you want something else to be displayed instead of T.ENTRIES if you enable showtotalentries
  
  #empty to be displayed is for when you want something else to be displayed for records that are empty i.e ''.
    Default which is shown for such records is '─'
    
  Extra feature-
     Suppose you know there is a column that has values that are fixed like Sex can be M or F or O.
     In such cases if you want your record or entry to be displayed in the middle of the column then use this feature.
     To enable this just add "|{special}|" in front of the column name that you want this in.
       
       Example- 
           columnamelist = [['AGE',5],['Sex|{special}|',3],['PASS',4]]
     

SECTION-2 
  #This deals with split table i.e double tables
  
  #To use this you must have two column name lists and two recordlist
  
  #Separate the columns in the columnamelist by using ['{break}'].
     Example-
        Suppose in column I you have 2 columns Age and Name.
        And in column II you have 2 columns Sex and Pass.
        Then columnlist will be -
           columnlist=[['AGE',4],['NAME',4],['{break}'],['SEX',3],['PASS',4]]
           
  #Separate the record list by using '|{rebreak}|'
     Example(This is related to the above example)-
        Suppose
          recordlistI=[['12','Sakaido'],['15','Mob']]   recordlistII=[['M','P'],['M','F']]
        Then 
          recordlist=[['12','Sakaido'],['15','Mob'],'|{rebreak}|',['M','P'],['M','F']]
          
  *Note-Everything else works the same as in Section 1.Only thing is ifsplit should be enabled i.e 
        equal to 1 if you are using this.
    
  *Note-The special feature works in this too.
           Example-
               columnlist=[['AGE',4],['NAME|{special}|',4],['{break}'],['SEX|{special}|',3],['PASS',4]]

"""

#These are example outputs.
#Section I-
"""
#For split examples see Section II.
   
#In this-
        columnlist=[['NAME',45],['AGE',5],['SEX',3]]
        recordlist=[['JOSEPH JOESTAR','88','M'],['JONATHON JOESTAR','25','M'],('JOTARO KUJO','19','M'),['ARTURIA PENDRAGON','22','']]

Call(1)- tablecr(columnlist,recordlist) 

O/P(1)-
 _____________________________________________________________
|_NAME__________________________________________|_AGE___|_SEX_|
| JOSEPH JOESTAR                                | 88    | M   |
| JONATHON JOESTAR                              | 25    | M   |
| JOTARO KUJO                                   | 19    | M   |
| ARTURIA PENDRAGON                             | 22    | ─   |
╹─────────────────────────────────────────────────────────────╹

Call(2)- tablecr(columnlist,recordlist,0)

O/P(2)-

| JOSEPH JOESTAR                                | 88    | M   |
| JONATHON JOESTAR                              | 25    | M   |
| JOTARO KUJO                                   | 19    | M   |
| ARTURIA PENDRAGON                             | 22    | ─   |
╹─────────────────────────────────────────────────────────────╹

Call(3)- tablecr(columnlist,recordlist,1,1)

O/P(3)-
 ______________________________________________________________
|______________________NAME______________________|__AGE__|_SEX_|
| JOSEPH JOESTAR                                 | 88    | M   |
| JONATHON JOESTAR                               | 25    | M   |
| JOTARO KUJO                                    | 19    | M   |
| ARTURIA PENDRAGON                              | 22    | ─   |
╹──────────────────────────────────────────────────────────────╹

Call(4)- tablecr(columnlist,recordlist,1,1,1)

O/P(4)-
 ____________ _____________
|__T.ENTRIES_|____4________|
 ______________________________________________________________
|______________________NAME______________________|__AGE__|_SEX_|
| JOSEPH JOESTAR                                 | 88    | M   |
| JONATHON JOESTAR                               | 25    | M   |
| JOTARO KUJO                                    | 19    | M   |
| ARTURIA PENDRAGON                              | 22    | ─   |
╹──────────────────────────────────────────────────────────────╹

Call(5)-  tablecr(columnlist,recordlist,1,1,1,1)

O/P(5)-
 ____________ _____________
|__T.ENTRIES_|____4________|
 __________________________________________________________________________
|___Sr_NO___|______________________NAME______________________|__AGE__|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    | M   |
|    02     | JONATHON JOESTAR                               | 25    | M   |
|    03     | JOTARO KUJO                                    | 19    | M   |
|    04     | ARTURIA PENDRAGON                              | 22    | ─   |
╹──────────────────────────────────────────────────────────────────────────╹

Call(6)- tablecr(columnlist,recordlist,1,1,1,1,0,'NONO')

O/P(6)-
 _______ _____________
|__NONO_|____4________|
 __________________________________________________________________________
|___Sr_NO___|______________________NAME______________________|__AGE__|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    | M   |
|    02     | JONATHON JOESTAR                               | 25    | M   |
|    03     | JOTARO KUJO                                    | 19    | M   |
|    04     | ARTURIA PENDRAGON                              | 22    | ─   |
╹──────────────────────────────────────────────────────────────────────────╹

Call(7)- tablecr(columnlist,recordlist,1,1,1,1,0,'NONO','NIL')

O/P(7)-
 _______ _____________
|__NONO_|____4________|
 __________________________________________________________________________
|___Sr_NO___|______________________NAME______________________|__AGE__|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    | M   |
|    02     | JONATHON JOESTAR                               | 25    | M   |
|    03     | JOTARO KUJO                                    | 19    | M   |
|    04     | ARTURIA PENDRAGON                              | 22    | NIL |
╹──────────────────────────────────────────────────────────────────────────╹

For Special feature:
  columnlist=[['NAME',45],['AGE',5],['SEX|{special}|',3]]
  recordlist=[['JOSEPH JOESTAR','88','M'],['JONATHON JOESTAR','25','M'],('JOTARO KUJO','19','M'),['ARTURIA PENDRAGON','22','F']]

Call(8)- tablecr(columnlist,recordlist,1,1,1,1,0,'NONO')

O/P(8)-
 _______ _____________
|__NONO_|____4________|
 __________________________________________________________________________
|___Sr_NO___|______________________NAME______________________|__AGE__|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    |  M  |
|    02     | JONATHON JOESTAR                               | 25    |  M  |
|    03     | JOTARO KUJO                                    | 19    |  M  |
|    04     | ARTURIA PENDRAGON                              | 22    |  F  |
╹──────────────────────────────────────────────────────────────────────────╹
"""

#Section II
"""
For this :
    columnlist=[['NAME',45],['AGE',5],['{break}'],['SEX|{special}|',3]]
    recordlist=[['JOSEPH JOESTAR','88'],['JONATHON JOESTAR','25'],('JOTARO KUJO','19'),['ARTURIA PENDRAGON','22'],'|{rebreak}|',['M'],['M'],['M'],['F']]

Call(1)- tablecr(columnlist,recordlist,1,1,1,1,1)

O/P(1)-
 __________________________                                                                                                                          __________________________       
|__T.ENTRIES_|____4________|                                                                                                                        |__T.ENTRIES_|____4________|      
 ____________________________________________________________________                                                                                _________________
|___Sr_NO___|______________________NAME______________________|__AGE__|                                                                              |___Sr_NO___|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    |                                                                              |    01     |  M  |
|    02     | JONATHON JOESTAR                               | 25    |                                                                              |    02     |  M  |
|    03     | JOTARO KUJO                                    | 19    |                                                                              |    03     |  M  |
|    04     | ARTURIA PENDRAGON                              | 22    |                                                                              |    04     |  F  |
╹────────────────────────────────────────────────────────────────────╹                                                                              ╹─────────────────╹

Call(2)- tablecr(columnlist,recordlist,1,1,0,1,1)

O/P(2)-
 ____________________________________________________________________                                                                                _________________
|___Sr_NO___|______________________NAME______________________|__AGE__|                                                                              |___Sr_NO___|_SEX_|
|    01     | JOSEPH JOESTAR                                 | 88    |                                                                              |    01     |  M  |
|    02     | JONATHON JOESTAR                               | 25    |                                                                              |    02     |  M  |
|    03     | JOTARO KUJO                                    | 19    |                                                                              |    03     |  M  |
|    04     | ARTURIA PENDRAGON                              | 22    |                                                                              |    04     |  F  |
╹────────────────────────────────────────────────────────────────────╹                                                                              ╹─────────────────╹

Call(3)- tablecr(columnlist,recordlist,1,0,0,1,1)

O/P(3)
 ___________________________________________________________________                                                                                 _________________
|___Sr_NO___|_NAME__________________________________________|_AGE___|                                                                               |___Sr_NO___|_SEX_|
|    01     | JOSEPH JOESTAR                                | 88    |                                                                               |    01     | M   |
|    02     | JONATHON JOESTAR                              | 25    |                                                                               |    02     | M   |
|    03     | JOTARO KUJO                                   | 19    |                                                                               |    03     | M   |
|    04     | ARTURIA PENDRAGON                             | 22    |                                                                               |    04     | F   |
╹───────────────────────────────────────────────────────────────────╹                                                                               ╹─────────────────╹

Call(4)- tablecr(columnlist,recordlist,0,0,0,1,1)

O/P(4)-
|    01     | JOSEPH JOESTAR                                | 88    |                                                                               |    01     | M   |
|    02     | JONATHON JOESTAR                              | 25    |                                                                               |    02     | M   |
|    03     | JOTARO KUJO                                   | 19    |                                                                               |    03     | M   |
|    04     | ARTURIA PENDRAGON                             | 22    |                                                                               |    04     | F   |
╹───────────────────────────────────────────────────────────────────╹                                                                               ╹─────────────────╹
"""
