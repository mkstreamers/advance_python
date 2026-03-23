#18. Design a File Logger System Problem: Create a class Logger that logs operations to a file. Use parameterized constructors to define the log file path. Implement a destructor to automatically close the file when the object is destroyed. Use method overloading to support different types of logs (info, warning, error).
class Logger:
    def __init__(self, filepath):
        self.file = open(filepath, "a")

    def log(self, message):
        self.file.write("[INFO] " + message + "\n")

    def log_warning(self, message):
        self.file.write("[WARNING] " + message + "\n")

    def log_error(self, message):
        self.file.write("[ERROR] " + message + "\n")

    def __del__(self):
        self.file.close()


logger = Logger("log.txt")
logger.log("System started")
logger.log_warning("Low memory")
logger.log_error("Crash detected")