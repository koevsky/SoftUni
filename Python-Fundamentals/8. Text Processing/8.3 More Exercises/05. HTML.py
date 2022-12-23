title = input()
print("<h1>")
print(f"    {title}")
print("</h1>")
content = input()
print("<article>")
print(f"    {content}")
print("</article>")
while True:
    comment = input()
    if comment == "end of comments":
        break
    print("<div>")
    print(f"    {comment}")
    print("</div>")
