
//const people = ["Greg", "Mary", "Devon", "James"];

// Write code to remove “Greg” from the people array.
//people.shift();

// Write code to replace “James” to “Jason”.
//people[people.length - 1] = "Jason";

// Write code to add your name to the end of the people array.
//people.push("Oxana");

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
//console.log(people.indexOf("Mary"));

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method
//const newPeople = people.slice(1);
//console.log('newPeople:', newPeople);

// Write code that gives the index of “Foo”. Why does it return -1 ?
//console.log(people.indexOf("Foo"));

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
//const last = people[people.length - 1]
//console.log('last:', last)

//console.log(people);

// Part II - Loops

//for (const friend of people) {
//    console.log("this person is: ", friend)
//    if (friend === "Devon") {break}
//}

// Exercise 2 : Your Favorite Colors

// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

//const colors = ["green", "white", "red", "blue", "black"]
//for (let i = 0; i < colors.length; i ++) {
//    console.log(`My #${i+1} choice is ${colors[i]}`)
//}

// const colors = ["green", "white", "red", "blue", "black"]
// const suffixes = ["st", "nd", "rd", "th", "th"]
// for (let i = 0; i < colors.length; i ++) {
//     console.log(`My ${i+1} ${suffixes[i]} choice is ${colors[i]}`)
// }

// Exercise 3 : Repeat The Question

// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
//const answer = prompt("Please enter a number")
//const number = Number(answer)
//console.log('number:', number + 1)

// let number = null
// while(number !=10) {
// const answer = prompt("Please enter a number")
// number = Number(answer)
// }

//Exercise 4 : Building Management
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },

//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// console.log(building.numberOfFloors)
// console.log("apartments on the first floor: ", building.numberOfAptByFloor.firstFloor)
// console.log("apartments on the third floor: ", building.numberOfAptByFloor.thirdFloor)
// console.log("second tenant:", building.nameOfTenants[1])
// console.log("Dan has this many rooms:", building.numberOfRoomsAndRent.dan[0])

// const sarahRent = building.numberOfRoomsAndRent.sarah[1]
// const davidRent = building.numberOfRoomsAndRent.david[1]
// const danRent = building.numberOfRoomsAndRent.dan[1]


// // if(sarahRent + davidRent > danRent) {
// //     console.log("Dan's rent is lower")
// // }

// if(sarahRent + davidRent > danRent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200
// }
// console.log(building)


// Exercise 5 : Family
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    mother: "Jane",
    father: "Bob",
    daughter: "Mary"
}

for (const item in family) {
    console.log('item:', item)
    console.log('value:', family[item])
}


//Exercise 6 : Rudolf
//Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
// }

// let sentence = ""
// for (const key in details) {
//     sentence = sentence + " " + key + " " + details[key]
// }
// console.log(sentence)


//Exercise 7
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// let acronym = ""
// for (const name of names.sort()) {
//     console.log(name)
//     acronym = acronym + name[0]
// }
// console.log(acronym)