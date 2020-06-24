import re
l='..123456789101213141516171820212223'
m = re.search(r'([0-9])\1+', l.strip())
print(m)
print(m.group(1) if m else -1)
