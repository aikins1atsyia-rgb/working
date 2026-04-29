class Patient:
    def __init__(self, name,age, condition_severity):
        self.name = name
        self.age = age
        self.severity = condition_severity # Scale 1 - 5 where 5 is considererd to be critical



class Hospital:
    def __init__(self, name, total_beds):
        self.name = name
        self.total_beds = total_beds
        self.occupied_beds = 0


    def has_space(self):
        return self.occupied_beds < self.total_beds
    
    def allocate_bed(self):
        if self.has_space():
            self.occupied_beds += 1
            return True
        return False