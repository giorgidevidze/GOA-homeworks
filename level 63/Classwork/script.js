// Task 1
// const person1 = {
//     name: "luka",
//     lastname: "begiashvili",
//     age: 24,
// }

// const person2 = {
//     name: "giorgi",
//     lastname: "devidze",
//     age: 16,
// };

// const person3 = {
//     name: "saba",
//     lastname: "lomidze",
//     age: 40,
// };

// console.log(person1);
// console.log(person2);
// console.log(person3);


// Task 2
function Car(make, model, year) {
    this.make = make;   
    this.model = model; 
    this.year = year;   
}

const car1 = new Car("Toyota", "Corolla", 2020);
const car2 = new Car("Honda", "Civic", 2018);
const car3 = new Car("Ford", "Mustang", 2022);

console.log(car1);
console.log(car2);
console.log(car3);


// Task 3
function Person(name, age, occupation, city) {
    this.name = name;        
    this.age = age;          
    this.occupation = occupation;
    this.city = city;        
}

const person1 = new Person("ნინო", 28, "დეველოპერი", "თბილისი");
const person2 = new Person("გიორგი", 35, "მომხამრებელი", "ბათუმი");
const person3 = new Person("ანა", 40, "დიზაინერი", "ქუთაისი");

console.log(person1);
console.log(person2);
console.log(person3);


// Task 4
function Animal(name, species, age) {
    this.name = name;     
    this.species = species; 
    this.age = age;       
}

const animal1 = new Animal("მია", "კატა", 3);
const animal2 = new Animal("რექსი", "ძაღლი", 5);
const animal3 = new Animal("პეტრუსი", "თაგვი", 1);

console.log(animal1);
console.log(animal2);
console.log(animal3);


// Task 5
// Constructor functions - (კონსტრუქტორის ფუნქციები) JavaScript-ში გამოიყენება ობიექტების შესაქმნელად. ისინი საშუალებას აძლევენ პროგრამისტს შექმნას ერთნაირი ტიპის ობიექტები (მაგალითად, ავტომობილები, ადამიანები, ცხოველები) და თითოეული ობიექტისთვის განისაზღვროს მათი სპეციფიკური თვისებები (ატრიბუტები). კონსტრუქტორის ფუნქციები განსაკუთრებით სასარგებლოა მაშინ, როცა საჭიროა მრავალი ობიექტის შექმნა, რომლებიც ჰქვს საერთო ტიპის და სტრუქტურის.