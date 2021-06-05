"""
program: phone_number.py
Author: Zhe Zhang A01257572 Set B
Date: June 5 2021
"""

import re

pattern = r"1[6,7]\d{9}"

content = "Jerry17785496842, Yuki1535477, Mercedeces, 15477, 13354556688"

results = re.findall(pattern, content)

for result in results:
    print(result)
