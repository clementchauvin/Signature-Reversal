from collections import defaultdict
from femr.datasets import PatientCollection

# 1. Ouvrir le flux
patients = PatientCollection("synthetic_data/extract_lite")

# Structures de stockage
patient_history = defaultdict(dict)
patient_birthdays = {}
patient_count = 0

# 2. Itérer directement sur les objets patient
for patient in patients:
  patient_count += 1
  pid = patient.patient_id

  for event in patient.events:
    if event.code.startswith("Birth/"):
      patient_birthdays[pid] = event.start
      continue

    if "/" not in event.code:
      continue

    vocab, raw_code = event.code.split("/", 1)
    clean_code = raw_code.replace(".", "").upper()
    key = (vocab, clean_code)

    if key in icd_to_phecodes:
      for pcode in icd_to_phecodes[key]:
        if (
            pcode not in patient_history[pid]
            or event.start < patient_history[pid][pcode]
        ):
          patient_history[pid][pcode] = event.start

print(f"Indexation terminée pour {patient_count} patients.")