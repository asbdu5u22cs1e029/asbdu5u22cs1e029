class player:
  def play(self):
      print("The player is player cricket.")


class Batsman(player):
   def play(self):
       print("The batsman is batting.")


 class Bowler(player):
   def play(self):
       print("The bowker is bowling.")


batsman = Batsman()
bowler.play()