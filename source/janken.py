from player import h_pon
from computer import c_pon
from janken_judge import judge

h_hand=-1
c_hand=-1
win=0
lose=0
tie=0

def  janken_main():    
     h_hand=-1
     c_hand=-1
     win=0
     lose=0
     tie=0
     for _ in range(3):
         h_hand=h_pon()
         c_hand=c_pon()
         print(h_hand)
         print(c_hand)
         j=judge(h_hand,c_hand)
         if j=='win':
             win = win+1
             print('あなたの勝ちです')
         elif j=='lose':
             lose =lose+1
             print('あなたの負けです')
         elif j=='tie':
             tie=tie+1
             print('ひきわけ')
         
         
     print("【最終結果】")
     if win > lose:
        print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの総合勝利です!")
     elif win < lose:
         print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nコンピューターの総合勝利です!")
     else:
         print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの引き分けです!")
         

if __name__ == '__main__':

      janken_main()
