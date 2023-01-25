def add_songs(*args):
    play_dict = {}
    for title, lyrics in args:
        if title not in play_dict.keys():
            play_dict[title] = lyrics
        else:
            play_dict[title].extend(lyrics)

    res = []
    for key, val in play_dict.items():
        res.append(f"- {key}")
        for line in val:
            res.append(line)

    return "\n".join(res)

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))



