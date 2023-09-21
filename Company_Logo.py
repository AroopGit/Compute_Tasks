from collections import Counter
company_name = input("Enter the company name in lowercase letters: ")
char_count = Counter(company_name)
sort_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
for char, count in sort_chars[:3]:
    print(char, count)
