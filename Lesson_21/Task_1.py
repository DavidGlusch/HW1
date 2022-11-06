from datetime import datetime


class ContextManager:
    def __init__(self, filename, filemode='a+'):
        self.filename = filename
        self.filemode = filemode
        self.timestamp = None
        self.text = None

    def __enter__(self):
        file = open(self.filename, self.filemode)
        self.timestamp = datetime.now().timestamp()
        return file

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('logs.txt', 'a+') as log:
            if exc_type is not None and exc_val is not None and exc_tb is not None:
                log.write('\n')
                log.write(str(exc_type))
                log.write('\n')
                log.write(str(exc_val))
                log.write('\n')
                log.write(str(exc_tb))
                log.write('\n')
        end_time = datetime.now().timestamp()

        during_time = end_time - self.timestamp
        self.text = "{:<20} | {:^15} | open \n{:<20} | {:^15} | closed {:>20}s".format(self.timestamp, self.filename,
                                                                             end_time, self.filename, during_time)
        print(self.text)


if __name__ == "__main__":
    file_test = ContextManager('new_file.txt', 'a+')
    with file_test as f:
        f.write('111')
        f.seek(0)
        a = f.read()

