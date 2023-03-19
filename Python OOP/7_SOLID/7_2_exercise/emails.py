from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return f'\n'.join(['<myML>', self.text, '</myML>'])


class HTMLContent(IContent):

    def format(self):
        return f'\n'.join(['<html>', self.text, '</html>'])


class IProtocol(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def protocol(self):
        pass


class Sender(IProtocol):

    def protocol(self):
        return ''.join(["I'm ", self.text])


class Receiver(IProtocol):

    def protocol(self):
        return ''.join(["I'm ", self.text])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.protocol()

    def set_receiver(self, receiver):
        self.__receiver = receiver.protocol()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


email = Email('IM')

sender = Sender("Ivan")
receiver = Receiver("Pesho")
content = MyContent('Hello, there!')

email.set_sender(sender)
email.set_receiver(receiver)
email.set_content(content)

print(email)



