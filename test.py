# **Ancestral Stories:**
# In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# Pseudo code

# Class 1:Story
# Input(Story attributes)-length,moral lessons,age group,language
# Output-Display the length of the story,its moral lessons and age group approriate to hear it
#Process
#1. Create a class with Story attributes
#2. create a method that displays the attributes

#Class 2:StoryTeller
# Input(inherit Story attributes)-length,moral lessons,age group,language
# Output-If it is appropriate for a certain group,depending on the group if the length of the story suits them,the
#moral lesson  should also suits the age group
# Process
#1. Create a class that inherits Story attributes
#2. Create a 3 method that shows:
#If the story is appropriate for a certain group
#if the length of the story suits a certain group
#if moral language lesson also suits the age group

#Class 3:Translator
#Input(inherit Story attributes)-language
#Process
#Create a classe with inherited attributes
#Create a method that checks the audience language against the story language


class Story:
    def __init__(self,length,moral_lessons,age_group,language):
        self.length=length
        self.moral_lessons=moral_lessons
        self.age_group=age_group
        self.language=language
    def displayProperties(self):
        return f"Story length:{self.length},language:{self.language},Age Group:{self.age_group} and Moral lessons:{self.moral_lessons}"
    

class StoryTeller(Story):
    def __init__(self, length, moral_lessons, age_group,language ):
        super().__init__(length, moral_lessons, age_group,language)
        self.length=length
        self.moral_lessons=moral_lessons
        self.age_group=age_group
    def is_approriate(self,age):
        if age >= self.age_group:
            return "Is approriate to hear"
        else:
            return "Inapproriate to hear"
    def gauge_attention_span(self,max_length):
        if max_length >=self.length:
            return "The audience can be attentive throughout the story"
        else:
            return"The audience will get bored"
    def appropriate_moral_lesson(self,lesson):
        if lesson== self.moral_lessons:
            return "Is approriate to hear"
        else:
            return "Inapproriate to hear"
class Translator(Story):
    def __init__(self,length, moral_lessons, age_group,language):
        super().__init__(length, moral_lessons, age_group,language)
    def translate_story(self,audience_language):
        if audience_language!= self.language:
            return "Translate story"
        else:
            return "No need to translate"
        
story1=Story(400,"sex education",14,"English")
print(story1.displayProperties())

person1=StoryTeller(200,"religion",5,"English")
print(person1.appropriate_moral_lesson("patience"))
print(person1.is_approriate(17))
print(person1.gauge_attention_span(300))

audience1=Translator(100,"farming",20,"Kiluhya")
print(audience1.translate_story("French"))
    

# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.


# #Pseudo code
# // input;title,author,available_copies
# //output:book details,tracking available copies,display added book
# //process:create a class with attributes-title,author,available_copies,
# //then 3 methods that to add new books, search for books by
# //title or author, keep track of available copies, and display book details.

class LibraryCatalog:
    def __init__(self,title,author,available_copies):
        self.title=title
        self.author=author
        self.available_copies=available_copies
        self.book_list=[]
        
    def add_new_book(self,book):
        if book1.title==self.title:
            self.book_list.append(book)
            return self.book_list
        else :
            return "Already exists"
    def track_available_copies(self,purchase):
        if self.available_copies>=purchase :
            self.available_copies-=purchase
            return "Book bought"
        else:
            return f"Available copies:{self.available_copies}"
    def display_details(self):
        return f"title:{self.title},author:{self.author},available_copies:{self.available_copies}"
book1=LibraryCatalog("Danger","James",25)
print(book1.add_new_book("Fire"))
print(book1.track_available_copies(100))       
print(book1.display_details())        

# //  #Create a class called Product with attributes for name, price, and quantity.
# //  #Implement a method to calculate the total value of the product (price * quantity).
# //  Create multiple objects of the Product class and calculate their total values.   
class Product:
    def __init__(self,name, price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculate_total_value(self):
        total=self.price*self.quantity
        return total

product1=Product("apples",20,5)
print(product1.calculate_total_value())

product2=Product("shirts",30,65)
print(product2.calculate_total_value())

product3=Product("apples",211,35)
print(product3.calculate_total_value())


# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

class FlightBooking:
    def __init__(self,available_flights,date,available_seats):
        pass