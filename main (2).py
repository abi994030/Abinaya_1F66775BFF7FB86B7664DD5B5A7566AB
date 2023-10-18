'''Implement a class called player that represents a cricket player the player class should have a method called play()which prints The play is planning cricket.Dervive two classes,Batsman and Bowler,from the player class.Override the play() method in each derived class to print"The batsman is batting" and"The bowler is bowling", respectively.write a program to create objects of both the batsman and bowler classes and call the play()method for each object.'''

class player:
  def play(self):
    print("The player is playing cricket.")
  
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
      
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

batsman = Batsman()
bowler = Bowler()


batsman.play()
bowler.play()