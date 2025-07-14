from collections.abc import MutableMapping

class Store(MutableMapping):

    # sebagai tempat menyimpan data
    def __init__(self):
        self.store = dict()

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]
      
    # untuk memanggil semua data beserta keynya menggunakan for
    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)


if __name__ == "__main__":
    video_store = Store()

    #set item
    video_store["horror"] = "the hollow dark shadow"
    video_store["romance"] = "with plane"
    video_store["comedy"] = "two side"

    # len
    print(len(video_store))
    # output : 3

    # get item
    print(video_store["romance"])
    # output: with plane

    # iter
    for key in video_store:
        print(key, video_store[key])
    # output :
    # horror the hollow dark shadow
    # romance with plane
    # comedy two side


    # delete
    del video_store["comedy"]
    print("after delete :")
    for key in video_store:
        print(key, video_store[key])
    # after delete :
    # horror the hollow dark shadow
    # romance with plane
