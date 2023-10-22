//DailyCh 1

// const sentence = "The dinner is bad"

// const wordNot = sentence.search("not")
// const wordBad = sentence.search("bad")

// if (wordNot === -1) {
//     console.log(sentence)
// } else if (wordNot < wordBad) {
// const firstPart = sentence.slice(0, wordNot)
// const secondPart = sentence.slice(wordBad + 3)
// console.log(firstPart + "good" + secondPart)
// } else {
//     console.log(sentence)
// }

//DailyCh 2

const maxNumber = 6
// let stars = " "

// for (let i=0; i < maxNumber; i++) {
//     stars = stars + " * "
//     console.log(stars)
// }

for (let i=0; i < maxNumber; i++) {
    const numberOfStars = i + 1
    let lineOfStars = ""
    for (let b = 0; b < numberOfStars; b++){
        lineOfStars = lineOfStars + " * " 
    }
    console.log(lineOfStars)
}