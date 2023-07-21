import csv


class TrainingDataGenerator:

    training_data = []

    def add_row(self, distance, key):
        self.training_data.append([distance, key])

    def write(self, file):
        with open(file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['distance', 'command'])
            for row in self.training_data:
                writer.writerow(row)
