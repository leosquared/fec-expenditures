import csv


class Processor():

    def __init__(
        self,
        content_path=None,
        header_path=None,
        content_delimiter='|',
        header_delimiter=','
    ):
        self.content_path = content_path
        self.header_path = header_path
        self.content_delimiter = content_delimiter
        self.header_delimiter = header_delimiter

    def generate_processed_file(self, output_path):
        with open(output_path, 'w') as outfile:
            writer = csv.writer(outfile)
            headers = open(
                self.header_path,
            ).read().split(self.header_delimiter)
            writer.writerow(headers)

            with open(self.content_path) as infile:
                reader = csv.reader(
                    infile,
                    delimiter=self.content_delimiter
                )
                for row in reader:
                    writer.writerow(row)

        return True