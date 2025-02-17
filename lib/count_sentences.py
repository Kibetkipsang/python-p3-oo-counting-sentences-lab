
import re
import sys
import io

class MyString:
  def __init__(self, value=''):
    self.set_value(value)

  def set_value(self, value):
    if not isinstance(value, str): 
            self._value = ""
            print("The value must be a string.")
    else:
        self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    self.set_value(value)

  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    if not isinstance(self.value, str):
            return 0
    sentences = re.split(r'[.!?]+', self.value.strip())
    return len([s for s in sentences if s]) 


string = MyString()
string.value = 123 
