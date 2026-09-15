
class User:
    def _init_(self, name,email, age, password ):
        self.name = name
        self.email = email
        self.age = age
        self._password = password

    def create_post(self,text):
        return Post(text, self)

    def create_comment(self,text,post):
        pass

    def send_message(self,text, receiver):
        pass
       

class Post:
    def _init_(self, text, author):
        self.text = text
        self.author = author

    def show(self):
        print(f"{self.author.user}: {self.text}")

class Comments:
    def _init_(self,num_comments,time,reactions):
        self.num_comments = num_comments
        self.time = time
        self.reactions = reactions
    def show(self):
        print(f"{self.author.user} commented: {self.text}")

class Message:
    def _init_(self,characters,sended,received):
        self.characters = characters
        self.sended = sended
        self.received = received 

    def show(self):
        print(f"From: {self.sended.user}, To: {self.received.user}")


user = User ("Kelsy")
post = user.create_post ("Kelsy has submited a new post")
post.show()
