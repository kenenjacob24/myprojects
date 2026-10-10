student_data = {
    "id1" : {"name": "Sara", "class" : "V", "subject_integation" : "english, math, science"},
    "id2" : {"name": "Jacob", "class" : "V", "subject_integation" : "english, math, science"},
    "id3" : {"name": "Sara", "class" : "V", "subject_integation" : "english, math, science"},
    "id4" : {"name": "Kenen", "class" : "V", "subject_integation" : "english, math, science"}
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integation"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)