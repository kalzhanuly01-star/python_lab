import re

input_filename = 'mailbox.txt'
output_filename = 'output.txt'

# Файлды толықтай оқып алу
with open(input_filename, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    lines = content.splitlines()

results = []

# 1. Sender account names from "From:"
results.append("=== Task 1: Account Names ===")
accounts = re.findall(r'^From:\s*([a-zA-Z0-9._%+-]+)@', content, re.MULTILINE)
results.extend(accounts)

# 2. Revisions from "Details:"
results.append("\n=== Task 2: Revisions ===")
revisions = re.findall(r'Details:\s*https?://[^\s]+rev=(\d+)', content)
results.extend(revisions)

# 3. Count emails
results.append("\n=== Task 3: Email Count ===")
email_count = sum(1 for line in lines if line.startswith('From '))
results.append(str(email_count))

# 4. Domain names from "From:"
results.append("\n=== Task 4: Sender Domain Names ===")
domains = re.findall(r'^From:\s*[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', content, re.MULTILINE)
results.extend(domains)

# 5. DSPAM confidence scores
results.append("\n=== Task 5: DSPAM Confidence Scores ===")
confidences = re.findall(r'X-DSPAM-Confidence:\s*([0-9.]+)', content)
results.extend(confidences)

# 6. Log messages
results.append("\n=== Task 6: Log Messages ===")
logs = re.findall(r'Log:\s*\n(.*?)\n----------------------', content, re.DOTALL)
results.extend([log.strip() for log in logs])

# 7. Sent dates (Month Day, Year)
results.append("\n=== Task 7: Sent Dates ===")
formatted_dates = []
for line in lines:
    if line.startswith('Date:'):
        match = re.search(r'(?:[A-Za-z]+,\s*)?(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', line)
        if match:
            day, month, year = match.groups()
            formatted_dates.append(f"{month} {day}, {year}")
results.extend(formatted_dates)

# 8. ESMTP IDs
results.append("\n=== Task 8: ESMTP IDs ===")
esmtp_ids = re.findall(r'ESMTP\s+id\s+([A-Za-z0-9]+)', content)
results.extend(esmtp_ids)

# 9. IP addresses in "Received:"
results.append("\n=== Task 9: IP Addresses ===")
ips = re.findall(r'Received:.*?\[([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]', content, re.DOTALL)
results.extend(ips)

# 10. Subjects with type "gradebook"
results.append("\n=== Task 10: Gradebook Subjects ===")
gradebook_subjects = [line for line in lines if line.startswith('Subject:') and 'gradebook' in line.lower()]
results.extend(gradebook_subjects)

# 11. Cyrus versions
results.append("\n=== Task 11: Cyrus Versions ===")
cyrus_versions = re.findall(r'Cyrus\s+(v[0-9.]+)', content)
results.extend(cyrus_versions)

# 12. SMTP IDs
results.append("\n=== Task 12: SMTP IDs ===")
smtp_ids = re.findall(r'SMTP\s+ID\s+([A-Za-z0-9]+)', content)
results.extend(smtp_ids)

# 13. Message-IDs
results.append("\n=== Task 13: Message-IDs ===")
message_ids = re.findall(r'Message-ID:\s*<([^@>]+)', content)
results.extend(message_ids)

# 14. Number of lines in the file
results.append("\n=== Task 14: Total Line Count ===")
results.append(str(len(lines)))

# 15. Lines containing "java"
results.append("\n=== Task 15: Lines with 'java' ===")
java_lines = [line for line in lines if 'java' in line.lower()]
results.extend(java_lines)

# 16. Time values
results.append("\n=== Task 16: Time Values ===")
times = re.findall(r'\d{1,2}\s+[A-Za-z]+\s+\d{4}\s+(\d{2}:\d{2}:\d{2})', content)
results.extend(times)

# 17. Longest line
results.append("\n=== Task 17: Longest Line ===")
if lines:
    results.append(max(lines, key=len))

# 18. Shortest line
results.append("\n=== Task 18: Shortest Line ===")
if lines:
    results.append(min(lines, key=len))

# Нәтижелерді output.txt файлына жазу
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write('\n'.join(str(r) for r in results))

print(f"Барлық 18 тапсырма сәтті орындалып, '{output_filename}' файлына сақталды!")