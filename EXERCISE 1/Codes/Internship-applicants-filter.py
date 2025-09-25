
scores = [85, 90, 72, 88, 95, 60]

total = sum(scores)
average = total / len(scores)
minimum = min(scores)
maximum = max(scores)

print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
report = f"Internship Applicants Report:\nTotal Applicants: {len(scores)}\n"
report += f"Total Score: {total}, Average Score: {average:.2f}"
print(report)
threshold = 80
if average > threshold and maximum > 90:   
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
applicants = ["Alice", "Bob", "Clara", "David", "Eva"]
print("Original Applicants:", applicants)
applicants.append("Frank")
if "Bob" in applicants:
    applicants.remove("Bob")
print("Before Sort:", applicants)
applicants.sort()
print("After Sort:", applicants)
import array
arr = array.array('i', [85, 90, 72]) 
print("Array elements:", arr.tolist())

arr_sum = sum(arr)
print("Sum of array:", arr_sum)
print("Compare with list total:", total)

records = [
    {"id": 1, "name": "Alice", "value": 85},
    {"id": 2, "name": "Bob", "value": 90},
    {"id": 3, "name": "Clara", "value": 72},
]
records[2]["value"] = 80
records = [rec for rec in records if rec["name"] != "Bob"]
total_value = sum(rec["value"] for rec in records)

print("Updated Records:", records)
print("Total of values:", total_value)
