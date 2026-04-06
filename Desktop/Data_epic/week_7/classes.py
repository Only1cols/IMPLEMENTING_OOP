   jj
          # instance method
       def description(self):
            return f"{self.name} is {self.age} years old"

            # another instance method

        def speak(self, sound):
            return f"{self.name} says {sound}"

        # def __str__(self):
            # return f"{self.name} is {self.age} year old"
        # when you run this using (print(miles)) it gives a much more friendlier output

        # methods like __init__ and __str__ are called dunder methods


miles = Dog("Miles", 4)
buddy = Dog("buddy", 9)


print(miles.speak)
