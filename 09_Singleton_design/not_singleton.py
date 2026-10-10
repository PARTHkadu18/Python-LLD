class Logger:
    log_count=0
    def __init__(self, file_name):
        self.file_name=file_name

    def log(self, text):
        print(f"Logging {text}")
        Logger.log_count+=1

log1=Logger("log1.txt")
log2=Logger("log2.txt")
log3=Logger("log3.txt")

log1.log("First log")
log2.log("Second log")
log3.log("Third log")

print(Logger.log_count)
print(Logger.log_count)
print(Logger.log_count)
