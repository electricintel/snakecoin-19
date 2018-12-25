import hashlib

from snakecoin.block import Block
from snakecoin.transaction import Transaction


_sha256_types = {
  Block: _sha256_b,
  Transaction: _sha256_t
}


def sha256(item):
  hash_f = _sha256_types.get(type(item), None)
  if hash_f is not None:
    return hash_f(item)
  raise TypeError('Invalid type for SHA256')


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
