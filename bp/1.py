# 2022/9/9
# 15:05
class testclass:

    @staticmethod
    def athena_getdb(a):
        print(a)

    @staticmethod
    def mysql_getdb(a):
        print(type(a))

dict__ = testclass.__dict__
getdb = dict__['athena_getdb'](1)
