
def judge(U_hand,P_hand):
    if U_hand == 1:
      if P_hand == 1:
          return 'tie'
      elif P_hand == 2:
          
        
          return 'win'
      else :
          
         
          return 'lose'
    elif U_hand == 2:
      if P_hand == 1:
          
         
          return 'lose'
      elif P_hand == 2:
          
          return 'tie'
      else :
        
          
          return 'win'
    else:
      if P_hand == 1:
          
         
          return 'win'
      elif P_hand == 2:
          
          
          return 'lose'
      else :
          
          return 'tie'
