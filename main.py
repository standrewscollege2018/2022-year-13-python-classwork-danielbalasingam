''' This program demonstrates how classes and object orientation work '''


class Enemy:
   ''' The enemy objects are what the player fights in the game'''

   def __init__(self, name, health):
      ''' The init function is called when a new object is instantiated
          It begins and ends with two underscores '''

      # Set the name
      self._name = name

      # Set the health
      self._health = health

      # Append the new enemy into the enemy_list
      enemy_list.append(self)

      # Scare the world with a villainous laugh!
      print("Mwa ha ha ha")

   def get_name(self):
      ''' This function returns the name of the enemy object '''

      return self._name

   def get_health(self):
      ''' This is a getter function that returns the health of the enemy '''

      return self._health

   def attacked(self, damage):
      ''' This function is called when the enemy is attacked.
          The damage value is deducted from the _health value '''

      self._health -= damage
      if self._health <= 0:
         print("Arrrgggghhhhh. I'm dead")
      else:
         print(f"Ouch! {self._name} is hurt!")


# Create a list to store all enemy objects
enemy_list = []

# Create a new enemy object
Enemy("Gru", 15)
Enemy("Vlad the Impaler", 3)


def display_enemies():
   ''' This function loops through the enemy_list and displays their names and health'''

   for e in enemy_list:
      print(f"{e.get_name()} has {e.get_health()} health")


display_enemies()
