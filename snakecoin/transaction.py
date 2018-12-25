import collections

from snakecoin import trie
from snakecoin import hashing


def _to_iterable(data):
  data = data or {}
  if not isinstance(data, collections.Iterable):
    data = set(data)
  return data


class Transaction:
  __slots__ = ('id', 'type', 'inputs', 'outputs')

  def __init__(self, id, type, inputs, outputs):
    self.id = id
    self.type = type
    self.inputs = _to_iterable(inputs)
    self.outputs = _to_iterable(outputs)

  @property
  def hash(self):
    return hashing.sha256(self)
  
