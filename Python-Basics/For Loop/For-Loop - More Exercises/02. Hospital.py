period = int(input())

doctors = 7

patients_treated = 0
patients_untreated = 0

for days in range(1, period+1):
    patient_count = int(input())
    if days % 3 == 0 and patients_untreated > patients_treated:
        doctors += 1

    if patient_count >= doctors:
        patients_treated += doctors
        patients_untreated += patient_count - doctors
    else:
        patients_treated += patient_count

print(f"Treated patients: {patients_treated}.")
print(f"Untreated patients: {patients_untreated}.")
