from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        print("    |    Hero's combat strength:", self.combat_strength)
        print("    |    Hero's health points:", self.health_points)

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()

    def hero_attacks(self, monster):
        ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
        """
        print(ascii_image)
        print("    |    Player's weapon (" + str(self.combat_strength) + ") ---> Monster (" + str(monster.health_points) + ")")
        if self.combat_strength >= monster.health_points:
            # Player was strong enough to kill monster in one blow
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            monster.health_points -= self.combat_strength
            print("    |    You have reduced the monster's health to: " + str(monster.health_points))
        return monster.health_points 