class Logger(object):
    __instance=None
    def __new__(cls, file_name):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
            cls.__instance.file_name=file_name
            cls.__instance.log_count=0
        return cls.__instance

    def log(self, msg):
        print(f"Logging {msg} to file {self.file_name}")
        self.log_count+=1
    
    def get_log_count(self):
        print(self.log_count)

l1=Logger("app.log")
l2=Logger("app.log")
l3=Logger("app.log")
print(l1)
print(l2)
print(l3)
l1.log("Parth")
l2.log("Kadu")
l3.get_log_count()