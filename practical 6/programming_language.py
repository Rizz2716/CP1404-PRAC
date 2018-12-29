# class programming_lang:
#
#   def __init__(self, name="",typing="",reflection="",year=0 ):
#       self.name = name
#       self.typing = typing
#       self.reflection = reflection
#       self.year = year
#
#   def is_dynamic(self, typing):
#       if self.typing.lower() == "dynamic":
#           return True
#       else:
#           return False
#
#   def __str__(self):
#       return ("{}, {} typing, reflection = {}, First appeared in {}".format(self.name, str(self.typing), str(self.reflection),self.year))
class programming_lang:

  def __init__(self, name="",typing="",reflection="",year=0 ):
      self.name = name
      self.typing = typing
      self.reflection = reflection
      self.year = year


  def is_dynamic(self, typing, name):
      for i in language_list:
          if self.typing.lower() == "dynamic":
                return True
          else:
                return False


  def __str__(self):
      return (("{}, {} typing, reflection = {}, First appeared in {}".format(self.name, str(self.typing), str(self.reflection),self.year)))
