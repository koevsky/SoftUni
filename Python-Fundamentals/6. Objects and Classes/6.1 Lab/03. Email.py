class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mails = []
while True:
    line = input()
    if line == "Stop":
        break
    line = line.split(" ")
    sender, receiver, content = line[0], line[1], line[2]
    email = Email(sender, receiver, content)
    mails.append(email)

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    mails[x].send()

for mail in mails:
    print(mail.get_info())


