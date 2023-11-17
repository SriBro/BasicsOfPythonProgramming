class College:

    __id = 0
    __name = None
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    # def set_id(self,id):
    #     __id = id
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

clg = College(1,"TCSC")
print(clg.get_id())
print(clg.get_name())
    