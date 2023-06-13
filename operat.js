console.log("hello js!");

let number1 = 123;
let text1 = "123";

// comparaison d'égalité
// renvoie true
console.log(number1 == text1);
console.log(text1 == number1);

// comparaison d'identité
// renvoie false
console.log(number1 === text1);
console.log(text1 === number1);

console.log(number1)

//number1 = number1 + 1

//number1 += 1
number1++;
console.log(number1);

//Attention l'incrémentation se fait apres l'affichage 
console.log(number1++);
console.log(number1);

//Attention l'incrémentation se fait avant l'affichage 
console.log(++number1);