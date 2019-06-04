while 1:
  cal=input('want to start')
  if(cal=='yes'):
      a=int(input('first value '))
      b=int(input('second value '))
      c=(input('what operation '))
      if(c=='+'):
        d=a+b
        print(d)
        continue
      elif(c=='-'):
        d=a-b
        print(d)
        continue
      elif(c=='*'):
        d=a*b
        print(d)
        continue
      elif(c=='/'):
        d=a/b
        print(d)
        continue
      elif(c=='%'):
        d=a%b
        print(d)
        continue
      elif(c=='**'):
        d=a**b
        print(d)
        continue
  elif(cal=='no'):
    break
 
