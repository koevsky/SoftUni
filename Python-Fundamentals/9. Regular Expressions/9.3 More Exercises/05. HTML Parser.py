import re
replace_n_ = r"(\\n)"
title_pattern = r""
body_pattern = r""
line = input()
replaced_n = re.sub(replace_n_, "", line)
