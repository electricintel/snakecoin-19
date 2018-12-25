# -*- coding: future_fstrings -*-

from snakecoin import merkle
from snakecoin import hashing


class Block:
  __slots__ = (
    'nonce', 'timestamp', 'index',
    'prev_hash', 'transactions',
  )

  def __init__(self, nonce=None, timestamp=None, index=None,
               prev_hash=None, transactions=None):
    self.nonce = nonce
    self.index = index
    self.timestamp = timestamp
    self.prev_hash = prev_hash
    self.transactions = transactions

  @property
  def hash(self):
    return hashing.sha256(self)

  @property
  def merkle_root(self):
    return merkle.compute(self.transactions)

  def __repr__(self):
    return f'<{self.__class__.__name__} (i:{self.index})'

  def __hash__(self):
    return self.hash

  def __eq__(self, other):
    return isinstance(other, Block) and self.hash == other.hash

  def __ne__(self, other):
    return not self.__eq__(other)
