import pandas as pd
from collections import defaultdict

# 1. Charger la table de mapping Unrolled
phecode_df = pd.read_csv("phecodes_cm.csv")

# Nettoyer les codes (supprimer les points et mettre en majuscules)
phecode_df['clean_icd'] = phecode_df['icd'].astype(str).str.replace('.', '', regex=False).str.upper()

# Dictionnaire : (vocabulaire, code) -> set de PheCodes
# Exemple de clé : ("ICD10CM", "E119") -> {"250.2", "250"}
icd_to_phecodes = defaultdict(set)
for _, row in phecode_df.iterrows():
    key = (row['vocabulary_id'], row['clean_icd'])
    icd_to_phecodes[key].add(str(row['phecode']))