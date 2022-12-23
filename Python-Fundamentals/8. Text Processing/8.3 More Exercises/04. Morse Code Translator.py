morse_dict = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I",
              ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
              ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
              "--..": "Z"}


morse_code = input().split(" | ")
final_result = []
for word in morse_code:
    word = word.split(" ")
    result_word = ""
    for x in word:
        if x:
            result_word += morse_dict[x]
    final_result.append(result_word)
print(" ".join(final_result))