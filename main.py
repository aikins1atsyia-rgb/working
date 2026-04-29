from models import Patient, Hospital
from utils import triage_priority, find_available_hospital

#Data Setup

hospitals = [
    Hospital("Korle-Bu", 2),
    Hospital("37 Military", 3000),
    Hospital("Tema General", 2000),
    Hospital("Cape Coast Teaching", 1500),
    Hospital("Komfo Anokye Teaching", 10000),
    Hospital("Tamale Teaching", 8000),
    Hospital("Ho Teaching", 5000),
    Hospital("Sunyani Regional", 3000),
    Hospital("Effia Nkwanta Regional", 2000),
    Hospital("Cape Coast Regional", 1500),
    Hospital("Koforidua Regional", 1000),
    Hospital("Bolgatanga Regional", 500)
]

def run_system():
    print("--- Emergency Bed Referral System ---")
    while True:
        name = input("\nEnter Patient Name (or 'exit'): ")
        if name.lower() == 'exit': break
        
        age = int(input("Enter Age: "))
        severity = int(input("Enter Severity (1-5): "))
        
        patient = Patient(name, age, severity)
        priority = triage_priority(patient)
        
        print(f"Triage Result: {priority} PRIORITY")

        # Core logic: If/Else/Elif for bed allocation
        target_hospital = find_available_hospital(hospitals)
        
        if target_hospital:
            if target_hospital.allocate_bed():
                print(f"SUCCESS: Bed assigned at {target_hospital.name}.")
            else:
                print("CRITICAL: Bed allocation failed unexpectedly.")
        else:
            # The 'No Bed Syndrome' Trigger
            print("ALERT: NO BEDS AVAILABLE in the network! Initiate emergency protocols.")

if __name__ == "__main__":
    run_system()
