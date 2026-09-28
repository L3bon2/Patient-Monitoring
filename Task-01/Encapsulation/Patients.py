class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def latest_reading(self):
        return sorted(self.readings, key=lambda r: r.timestamp)[-1]
