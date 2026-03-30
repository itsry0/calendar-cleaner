import requests
import re

ICS_URL = "https://rooster.ucll.be/ical/student/r1083935/hash/11d75fc3965015ad6c97849c675a5931ca984769a3c32ec64bf051993c345fd739c768a1a3ab858e5ad2526df430bc9053d5bd429f783367d474669175863fe1"

def clean_summary(text):
    text = re.sub(r"MNB\d+[a-z]?\s*", "", text)
    text = re.sub(r"GROUP\s*\d+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def clean_ics(content):
    lines = content.splitlines()
    new_lines = []

    for line in lines:
        if line.startswith("SUMMARY:"):
            title = line.replace("SUMMARY:", "")
            cleaned = clean_summary(title)
            new_lines.append("SUMMARY:" + cleaned)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)

def main():
    response = requests.get(ICS_URL)
    cleaned = clean_ics(response.text)

    with open("cleaned.ics", "w", encoding="utf-8") as f:
        f.write(cleaned)

if __name__ == "__main__":
    main()
