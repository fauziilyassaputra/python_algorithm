from collections.abc import Iterator, MutableMapping
from dataclasses import dataclass
from typing import TypeVar

# variable tipe generik (tipe T) sehingga tipe data lebih fleksibel
KEY = TypeVar("KEY")
VAL = TypeVar("VAL")

# tidak perlu membuat __init__ manual
@dataclass(slots=True)
class _Item[KEY, VAL]:
    key: KEY
    val: VAL

class _DeletedItem(_Item):
    def __init__(self) -> None:
        super().__init__(None,None)

    def __bool__(self) -> bool:
        return False

_deleted = _DeletedItem()

# mutablemapping dibuat jika ingin membuat class seperti dictionary dan mendukung pengubahan item
# harus menggunakan __getitem, __setitem__, __delitem__ , __iter__ . __len__

class HashMap(MutableMapping[KEY,VAL]):

    def __init__(
            self, initial_block_size:int = 8, capacity_factor:float = 0.75
    ) -> None:
        self._initial_block_size = initial_block_size
        self._buckets:list[_Item | None] = [None] * initial_block_size
        assert 0.0 < capacity_factor < 1.0
        self._capacity_factor =  capacity_factor
        self._len = 0

    def _get_bucket_index(self,key:KEY) -> int:
        return hash(key) % len(self._buckets)

    def _get_next_index(self, index:int) -> int:
        return (index + 1) % len(self._buckets)

    def _try_Set(self, index:int, key:KEY, val:VAL) -> bool:
        stored = self._buckets[index]
        if not stored:
            self._buckets[index] = _Item(key,val)
            self._len += 1
            return True
        elif stored.key == key:
            stored.val = val
            return True
        else:
            return False

    def _is_full(self)-> bool:
        limit = len(self._buckets) * self._capacity_factor
        return len(self) >= int(limit)


    def _resize(self, new_size: int) -> None:
        old_buckets = self._buckets
        self._buckets = [None] * new_size
        self._len = 0
        for item in old_buckets:
            if item:
                self._add_item(item.key, item.val)

    def _size_up(self) -> None:
        self._resize(len(self._buckets) * 2)

    def _size_down(self) -> None:
        self._resize(len(self._buckets) // 2)

    def _iterate_buckets(self, key: KEY) -> Iterator[int]:
        ind = self._get_bucket_index(key)
        for _ in range(len(self._buckets)):
            yield ind
            ind = self._get_next_index(ind)

    def _add_item(self, key:KEY, val: VAL) -> None :
        for index in self._iterate_buckets(key):
            if self._try_Set(index, key, val):
                break


    def __setitem__(self, key:KEY, value:VAL):
        if self._is_full():
            self._size_up()
        self._add_item(key, value)

    def __delitem__(self, key) -> None:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                raise KeyError(key)
            if item is _deleted:
                continue
            if item.key == key:
                self._buckets[ind] = _deleted
                self._len -= 1
                break

    def __getitem__(self, key: KEY) -> VAL:
        for ind in self._iterate_buckets(key):
            item = self._buckets[ind]
            if item is None:
                break
            if item is _deleted:
                continue
            if item.key == key:
                return item.val
        raise KeyError(key)

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[KEY]:
        yield from (item.key for item in self._buckets if item)

    def __repr__(self) -> str:
        val_string =", ".join(
            f"{item.key}: {item.val}" for item in self._buckets if item
        )
        return f"HashMap({val_string})"

if __name__ == "__main__":
    hm = HashMap(3)
    hm._add_item(1,10)
    hm._add_item(2,20)
    print(hm)
    # HashMap(1: 10, 2: 20)

    hm._add_item(2,25) # set item
    hm.__setitem__(3,30)
    print(hm)
    # HashMap(1: 10, 2: 25, 3: 30)
    print(hm.__len__())
    #3

    hm.__delitem__(3)
    print(hm)
    # HashMap(1: 10, 2: 25)
    print(hm.__getitem__(2))
    #25
