import os


class Outputer(object):
    def __init__(self):
        self.__data = []

    def collect_data(self, data):
        if data is None:
            return
        self.__data.append(data)

    def outputer_html(self, path, file_name):
        output_file = open(os.path.join(path, file_name), 'w')

        output_file.write("<html>")
        output_file.write("<meta charset='utf-8'>")
        output_file.write("<body>")
        for data in self.__data:
            output_file.write("<div>")
            output_file.write("<div>")
            output_file.write("<span>")
            output_file.write("Craw keywords: ")
            output_file.write("</span>")
            output_file.write("<span>")
            output_file.write(u''.join(data.get('title')).encode('utf-8').strip())
            output_file.write("</span>")
            output_file.write("</div>")
            output_file.write("<div>")
            output_file.write("<span>")
            output_file.write("From URL: ")
            output_file.write("</span>")
            output_file.write("<span>")
            output_file.write(data["url"])
            output_file.write("</span>")
            output_file.write("</div>")
            output_file.write("<span>")
            output_file.write("Craw Content: ")
            output_file.write("</span>")
            output_file.write("<span>")
            output_file.write(u''.join(data["summary"]).encode('utf-8').strip())
            output_file.write("</span>")
            output_file.write("<div>")
            output_file.write("</div>")
            output_file.write("</div>")
        output_file.write("</body>")
        output_file.write("</html>")

        output_file.close()
