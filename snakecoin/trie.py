# -*- coding: future_fstrings -*-
try:
  from itertools import izip as zip
except ImportError:
  pass

from snakecoin import hashing


def pairwise(iterable):
  a = iter(iterable)
  return zip(a, a)


class Node(object):
  __slots__ = ('left', 'right', 'hash',)

  def __init__(self, hash, left=None, right=None):
    self.left = left
    self.right = right
    self.hash = hash

  def __repr__(self):
    return f'<Node {self.hash}>'

  def __hash__(self):
    return self.hash

  def __eq__(self, other):
    return isinstance(other, Node) and self.hash == other.hash


class MerkleTree(object):
  def __init__(self, root):
    self.root = root

  @classmethod
  def create(cls, units):
    hashes = [Node(hash(unit)) for unit in units]
    if len(hashes) > 0:
      while len(hashes) != 1:
        if (len(hashes) % 2) != 0:
          hashes.append(hashes[-1])
        nodes = []
        for l, r in pairwise(hashes):
          node_hash = hashing.sha256(l, r)
          nodes.append(Node(node_hash, l, r))
        hashes = nodes
      return cls(root=hashes[0])
    return None

  @property
  def root_hash(self):
    return hash(self.root)
