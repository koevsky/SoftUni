jury_count = int(input())
final_assessment = 0
presentation_count = 0
while True:
    data = input()
    if data == "Finish":
        print(f"Student's final assessment is {(final_assessment / presentation_count):.2f}.")
        break
    presentation_mark = 0
    for people in range(jury_count):
        presentation_mark += float(input())
    presentation_mark /= jury_count
    final_assessment += presentation_mark
    presentation_count += 1
    print(f"{data} - {presentation_mark:.2f}.")