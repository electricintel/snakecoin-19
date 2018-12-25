from __future__ import absolute_import

import hashlib

from snakecoin.block import Block
from snakecoin.transaction import Transaction


def sha256(left, right):
  load = str(left.hash) + str(right.hash)
  load = load.encode('UTF-8')
  return hashlib.sha256(load).hexdigest()


def _sha256_b(block):
  sha = hashlib.sha256()
  string = str()
  for field in block.__slots__:
    value = getattr(block, field, None)
    if value:
      string += str(value)
  sha.update(string.encode('UTF-8'))
  return sha.hexdigest()


def _sha256_t(transaction):
  pass


_sha256_types = {
  Block: _sha256_b,
  Transaction: _sha256_t
}
