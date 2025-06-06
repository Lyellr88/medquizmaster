"""
Medical Quiz Questions Database
Contains questions for Cardiology, Neurology, and Pulmonology specialties
"""

QUESTIONS = [
    # Cardiology Questions
    {
        "question": "What is the most common cause of myocardial infarction?",
        "options": [
            "A. Coronary artery thrombosis",
            "B. Coronary artery spasm",
            "C. Aortic dissection",
            "D. Pericarditis"
        ],
        "answer": "A",
        "specialty": "cardiology",
        "explanation": "Coronary artery thrombosis is the most common cause of myocardial infarction, typically occurring due to plaque rupture and subsequent clot formation."
    },
    {
        "question": "A 65-year-old man presents with chest pain and ST elevation in leads II, III, and aVF. Which artery is most likely occluded?",
        "options": [
            "A. Left anterior descending",
            "B. Right coronary artery",
            "C. Circumflex artery",
            "D. Left main coronary artery"
        ],
        "answer": "B",
        "specialty": "cardiology",
        "explanation": "ST elevation in leads II, III, and aVF indicates an inferior wall myocardial infarction, which is typically caused by right coronary artery occlusion."
    },
    {
        "question": "Which medication is contraindicated in patients with severe aortic stenosis?",
        "options": [
            "A. ACE inhibitors",
            "B. Beta-blockers",
            "C. Nitroglycerin",
            "D. Calcium channel blockers"
        ],
        "answer": "C",
        "specialty": "cardiology",
        "explanation": "Nitroglycerin is contraindicated in severe aortic stenosis as it can cause dangerous hypotension by reducing preload in patients who depend on high filling pressures."
    },

    # Neurology Questions
    {
        "question": "Which neurotransmitter is primarily affected in Alzheimer's disease?",
        "options": [
            "A. Dopamine",
            "B. Serotonin",
            "C. GABA",
            "D. Acetylcholine"
        ],
        "answer": "D",
        "specialty": "neurology",
        "explanation": "Acetylcholine is the primary neurotransmitter affected in Alzheimer's disease, with significant loss of cholinergic neurons in the basal forebrain and reduced acetylcholine activity."
    },
    {
        "question": "A patient presents with sudden onset of severe headache described as 'the worst headache of my life.' What is the most likely diagnosis?",
        "options": [
            "A. Subarachnoid hemorrhage",
            "B. Tension headache",
            "C. Migraine",
            "D. Cluster headache"
        ],
        "answer": "A",
        "specialty": "neurology",
        "explanation": "Sudden onset of severe headache described as 'the worst headache of my life' is classic for subarachnoid hemorrhage, often due to ruptured cerebral aneurysm."
    },
    {
        "question": "Which cranial nerve is most commonly affected in diabetic neuropathy?",
        "options": [
            "A. Facial nerve (VII)",
            "B. Oculomotor nerve (III)",
            "C. Trigeminal nerve (V)",
            "D. Abducens nerve (VI)"
        ],
        "answer": "B",
        "specialty": "neurology",
        "explanation": "The oculomotor nerve (cranial nerve III) is most commonly affected in diabetic neuropathy, causing diplopia and ptosis due to ischemia of the nerve."
    },

    # Pulmonology Questions
    {
        "question": "Which finding on chest X-ray is pathognomonic for pneumothorax?",
        "options": [
            "A. Pleural line with absence of lung markings",
            "B. Consolidation",
            "C. Pleural effusion",
            "D. Pneumonia"
        ],
        "answer": "A",
        "specialty": "pulmonology",
        "explanation": "A pleural line with absence of lung markings beyond it is pathognomonic for pneumothorax, representing the collapsed lung edge separated from the chest wall."
    },
    {
        "question": "What is the gold standard test for diagnosing pulmonary embolism?",
        "options": [
            "A. Chest X-ray",
            "B. CT pulmonary angiogram (CTPA)",
            "C. D-dimer",
            "D. ECG"
        ],
        "answer": "B",
        "specialty": "pulmonology",
        "explanation": "CT pulmonary angiogram (CTPA) is the gold standard test for diagnosing pulmonary embolism, providing detailed visualization of pulmonary arteries and clot detection."
    },
    {
        "question": "Which condition is characterized by irreversible airflow limitation?",
        "options": [
            "A. Asthma",
            "B. Pneumonia",
            "C. Pulmonary edema",
            "D. COPD"
        ],
        "answer": "D",
        "specialty": "pulmonology",
        "explanation": "COPD (Chronic Obstructive Pulmonary Disease) is characterized by irreversible airflow limitation, unlike asthma which typically shows reversible obstruction."
    }
]

# Utility functions for question management
def get_questions_by_specialty(specialty):
    """Get questions filtered by specialty"""
    if specialty == 'mixed':
        return QUESTIONS
    return [q for q in QUESTIONS if q['specialty'] == specialty]

def get_available_specialties():
    """Get list of available specialties"""
    specialties = set()
    for question in QUESTIONS:
        specialties.add(question['specialty'])
    return sorted(list(specialties))
