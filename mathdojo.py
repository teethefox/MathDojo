class MathDojo(object):
  def __init__(self):
    self.output = 0
  def add(self, *input):
    for a in input:
      if type(a) == list or type(a) == tuple:
        for b in a:
          self.output += b
      else:
        self.output += a
        return self

    """Mimicked style on answer key in order to learn better sytax"""