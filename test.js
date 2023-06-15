// # **Ancestral Stories:**
// # In many African cultures, the art of storytelling is passed
// # down from generation to generation. Imagine you're creating an application that
// # records these oral stories and translates them into different languages. The
// # stories vary by length, moral lessons, and the age group they are intended for.
// # Think about how you would model `Story`, `StoryTeller`, and `Translator`
// # objects, and how inheritance might come into play if there are different types of
// # stories or storytellers.

// # Pseudo code

// # Class 1:Story
// # Input(Story attributes)-length,moral lessons,age group,language
// # Output-Display the length of the story,its moral lessons and age group approriate to hear it
// #Process
// #1. Create a class with Story attributes
// #2. create a method that displays the attributes

// #Class 2:StoryTeller
// # Input(inherit Story attributes)-length,moral lessons,age group,language
// # Output-If it is appropriate for a certain group,depending on the group if the length of the story suits them,the
// #moral lesson  should also suits the age group
// # Process
// #1. Create a class that inherits Story attributes
// #2. Create a 3 method that shows:
// #If the story is appropriate for a certain group
// #if the length of the story suits a certain group
// #if moralanguagel lesson also suits the age group

// #Class 3:Translator
// #Input(inherit Story attributes)-length,moral lessons,age group
// #Class 3:Translator
// #Input(inherit Story attributes)-language
// #Process
// #Create a classe with inherited attributes
// #Create a method that checks the audience language against the story language


class Story{
    constructor(length,moral_lessons,age_group,language){
        this.length=length
        this.moral_lessons=moral_lessons
        this.age_group=age_group
        this.language=language
    }
    displayProperties(){
    return `Story length:${this.length},language:${this.language},Age Group:${this.age_group} and Moral lessons:${this.moral_lessons}`
}
}

    

class StoryTeller extends Story{
    constructor(length, moral_lessons, age_group){
        super(length,moral_lessons,age_group)
        this.length=length
        this.moral_lessons=moral_lessons
        this.age_group=age_group
        
    }
    is_approriate(age){
        if (age >= this.age_group){
            return "Is approriate to hear"
        }   
        else{
            return "Inapproriate to hear"
        }
    }
    gauge_attention_span(max_length){
        if (max_length >=this.length){
            return "The audience can be attentive throughout the story"}
        else{
            return"The audience will get bored"}}
    appropriate_moral_lesson(lesson){
                if (lesson== this.moral_lessons){
                    return "Is approriate to hear"}
                else{
                    return "Inapproriate to hear"}}

}
    
       
class Translator extends Story{
    constructor(language){
        super(language)
        this.language=language
    }
        translate_story(audience_language){
        if (audience_language!= this.language){
            return "Translate story"}
        else{
            return "No need to translate"}}

}
     
        
let story1=new Story(400,"sex education",14,"English")
console.log(story1.displayProperties())

let person1=new StoryTeller(200,"religion",5,"English")
console.log(person1.appropriate_moral_lesson("patience"))
console.log(person1.is_approriate(17))
console.log(person1.gauge_attention_span(300))

let audience1=new Translator(100,"farming",20,"Kiluhya")
console.log(audience1.translate_story("French"))

// input;title,author,available_copies
//output:book details,tracking available copies,display added book
//process:create a class with attributes-title,author,available_copies,
//then 3 methods that to add new books, search for books by
//title or author, keep track of available copies, and display book details.
class LibraryCatalog{
    constructor(self,title,author,available_copies){
        this.title=title
        this.author=author
        this.available_copies=available_copies
        this.book_list=[]
    }
    add_new_book(book){
        if (book==this.title){
            this.book_list.append(book)
            return this.book_list}
        else{
            return "Already exists"}}
    track_available_copies(purchase){
        if (this.available_copies>=purchase) {
            this.available_copies-=purchase
            return "Book bought"}
        else{
            return `Available copies:${this.available_copies}`}}
     display_details(){
        return `title:${this.title},author:${this.author},available_copies:${this.available_copies}`

}}
book1=new LibraryCatalog("Danger","James",25)
console.log(book1.add_new_book("Fire"))
console.log(book1.track_available_copies(100))       
console.log(book1.display_details())        

//  #Create a class called Product with attributes for name, price, and quantity.
//  #Implement a method to calculate the total value of the product (price * quantity).
//  Create multiple objects of the Product class and calculate their total values.   
class Product{
    constructor(name, price,quantity){
        this.name=name
        this.price=price
        this.quantity=quantity
    }
    calculate_total_value(){
        let total=this.price*this.quantity
        return total
    }
}   
let product1=new Product("apples",20,5)
console.log(product1.calculate_total_value())

let product2=new Product("shirts",30,65)
console.log(product2.calculate_total_value())

let product3=new Product("apples",211,35)
console.log(product3.calculate_total_value())
    



