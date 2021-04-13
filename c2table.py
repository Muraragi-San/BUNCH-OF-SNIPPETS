import os 
dir_path = os.path.dirname(os.path.realpath(__file__))+'\\Table.txt'

class c2table:
    columnlist=[['Default-1',15]]
    
    recordlist=[['default record']]
    
    dispheader=True
    
    splittable=False
    
    disptentries=False
    
    dispsrno=False
    
    emptyrecordS='─'
    
    colincenter=False
    
    tentryS='T.ENTRIES'
    
    tabletxt=False
    
    tabletxtloc=dir_path
    
    def checker(inf,L=[],r=[]):
            
            a=len(inf.columnlist)
            rec=inf.recordlist
            if inf.splittable:
                a=len(L)
                rec=r
            
            for i in rec:
                if len(i)!=a:                    #checks if the number of columns are equal to the number of records
                    print("Records don't match number of columns.")
                    return True
            return False
        
    def checkcolumn(inf,L=[]):
               chklist=[]
               a=inf.columnlist
               if inf.splittable:
                   a=L
               for i in a:
                   if len(i[0].split('|{special}|')[0])>i[1]:
                       chklist.append([i[0],len(i[0].split('|{special}|')[0])])  #checks if the column name is less than size mentioned and fixes it
                   else:
                       chklist.append(i)
               if inf.splittable:
                   return chklist
               inf.columnlist=chklist
    
    def header(inf,colgt,colgt2=0,r1=[],r2=[],mainlgt=0):
        head=""                                 #creates the header
        if inf.disptentries:
            if inf.splittable:
               a = len(r1)
               a2=len(r2)
               dig=len(str(a))
               dig2=len(str(a2))
               Sign=inf.tentryS
               leg=mainlgt-colgt2-len(f' {"_"*(len(Sign[:20])+3)} {"_"*13}')              
               head+=f' {"_"*(len(Sign[:20])+3)} {"_"*13} '+" "*(leg)+f' {"_"*(len(Sign[:20])+3)} {"_"*13}\n'
               head+=f'{"|__"+Sign[:20]+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}'+" "*(leg)+f'{"|__"+Sign[:20]+"_|"+"____"+str(a2)+"_"*(9-dig2)+"|"}\n'
               
            else:  
             a = len(inf.recordlist)
             dig=len(str(a))
             head+=f' {"_"*(len(inf.tentryS[:20])+3)} {"_"*13}\n'
             head+=f'{"|__"+inf.tentryS[:20]+"_|"+"____"+str(a)+"_"*(9-dig)+"|"}\n'
             
            

        
        if inf.splittable:
            head+=f' {"_"*(colgt-2)}{" "*(167-(colgt+colgt2))}  {"_"*(colgt2-2)} '
        else:
            head+=f' {"_"*colgt} '
        return head
    
    def colstr(inf,L=[]):
        #creates the column string
        colinf=[]
        header=""
        collist=inf.columnlist
        if inf.splittable:
            collist=L
        if inf.dispsrno:
            header+="|___Sr_NO___"
        if inf.colincenter:
          for i in collist: 
            a=i[0].split('|{special}|')
                
            diff=i[1]-len(a[0])
            if diff%2!=0:
                diff+=1
            diff//=2
            kconst=f"{'_'+('_'*diff)+a[0]+('_'*diff)}_"
            header+="|"+kconst
            if len(a)==2:
                colinf.append([[kconst,i[1]],True])
            else:
                colinf.append([[kconst,i[1]],False])
        else:
          for i in collist:
            a=i[0].split('|{special}|')
            if len(a)==1:
                 diff=i[1]-len(a[0])
                 kconst=f"{'_'+a[0]+('_'*diff)}_"
                 header+="|"+kconst
                 colinf.append([[kconst,i[1]],False])
            elif len(a)==2:
                
                diff=i[1]-len(a[0])
                if diff%2!=0:
                   diff+=1
                diff//=2
                kconst=f"{'_'+('_'*diff)+a[0]+('_'*diff)}_"
                header+="|"+kconst
                colinf.append([[kconst,i[1]],True])
                
        header+="|"
        return header,colinf
    def splitrowcr(inf,row1,row2,colulgt):
        a=0
        row=""
        for i in row1:
            row+=f'{i}{" "*colulgt}{row2[a]}\n'
            a+=1
        return row
            
    def rowstr(inf,colu,totalgt,L=[],L2=[],colu2=[],totalgt2=0):
         row=''
         records=inf.recordlist
         end=0
         co=0
         trig=False
         rlist=[]
         if inf.splittable:
            records=L
            trig=True
            
         for i in records:
             if inf.dispsrno:          #creates the row string
              co+=1
              if co>=100000:
                        count="ERR"
              elif co<10:
                     count="0"+str(co)
              else:
                     count=str(co)
              row+=f'{"|    "+count+" "*(7-len(str(count)))+"|"}'
             else:
                row+="|"
             a=0
             
             for rec in i:
                 
                if colu[a][1]:
                    rec=str(rec)
                    if rec=='':
                        rec=inf.emptyrecordS
                    elif len(rec)>colu[a][0][1]:
                      rec=rec[:colu[a][0][1]]
                    role=(len(colu[a][0][0])-len(rec))//2
                    role2=len(colu[a][0][0])-role-len(rec)-1
                    row+=f"""{' '*role}{rec}{' '*role2} |"""
                    
                else:
                  role=colu[a][0][1]
                
                  if rec=='':
                      rec=inf.emptyrecordS
                  elif len(rec)>role:
                      rec=rec[:role]
                  rec=str(rec)
                
                  row+=f""" {rec}{' '*(len(colu[a][0][0])-len(rec)-2)} |"""
                  
                a+=1
             end+=1
             if end==len(records):
                if trig:
                 rlist.append(row)
                 rlist.append(f"╹{'─'*totalgt}╹")
                else:
                   row+=f"\n╹{'─'*totalgt}╹" 
             else:
              if trig:
                rlist.append(row) 
                row=""
              else:
               row+="\n"
         if trig:
             return rlist
         else:
           return row    

    def disptable(info):              #displays table
        try: 
            if info.splittable:
                cl1=[]
                cl2=[]
                k=0
                for i in info.columnlist:
                    if i==['{break}']:
                        k=1
                        continue
                    if k==0:
                        cl1.append(i)
                    elif k==1:
                        cl2.append(i)
                if cl2==[]:
                    print("No breaking point in the columnlist.Please check if the format is correct!!")
                    return
                k=0
                re1=[]
                re2=[]
                for i in info.recordlist:
                    if i==['{rebreak}']:
                        k=1
                        continue
                    if k==0:
                        re1.append(i)
                    elif k==1:
                        re2.append(i)
                if re2==[]:
                    print("No breaking point in the recordlist.Please check if the format is correct!!")
                    return
                if info.checker(cl1,re1):
                    return
                if info.checker(cl2,re2):
                    return
                
                cl1=info.checkcolumn(cl1)
                cl2=info.checkcolumn(cl2)
                column,colinfo=info.colstr(cl1)
                column2,colinfo2=info.colstr(cl2)
                maincolumn=column+" "*(167-len(column)-len(column2))+column2
                if len(maincolumn)>167:
                    print(f"The Column length is exceeding the current limit i.e 167 characters.\nYour length is {len(maincolumn)}||It should be at most 167 characters\nTry reducing {len(maincolumn)-167} character(s)")
                else:
                  if info.dispheader:
                    head=info.header(len(column),len(column2),re1,re2,len(maincolumn))
                    print(head)    
                    print(maincolumn)
                  row1=info.rowstr(colinfo,len(column)-2,re1)
                  row2=info.rowstr(colinfo2,len(column2)-2,re2)
                  row=info.splitrowcr(row1,row2,(167-(len(column)+(len(column2)))))
                  print(row)
                  if info.tabletxt:
                    with open(info.tabletxtloc,'+a') as f:
                      f.write(head+'\n')
                      f.write(maincolumn+'\n')
                      f.write(row+'\n')
            else:
                if info.checker():
                    return
                info.checkcolumn()
                column,colinfo=info.colstr()
                if len(column)>167:
                    print(f"The Column length is exceeding the current limit i.e 167 characters.\nYour length is {len(column)}||It should be at most 167 characters\nTry reducing {len(column)-167} character(s)")
                else:
                  row=info.rowstr(colinfo,len(column)-2)
                  if info.dispheader:
                    head=info.header(len(column)-2)
                    print(head)
                    print(column)
                  print(row)
                if info.tabletxt:
                  with open(info.tabletxtloc,'+a') as f:
                    f.write(head+'\n')
                    f.write(column+'\n')
                    f.write(row+'\n')
                
        except Exception as e:
             print(f"Error :{e}")
