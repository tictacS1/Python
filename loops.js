// Boucle for classique
for (let i=0; i<10; i++) {
    console.log("i = " + i);
}

// Boucle a rebours
for (let i=10; i>0; i++) {
    console.log("i = " + i);
}

let users = ['foo','bar','baz']

for (let user of users) {
    console.log(user);
}

//syntaxe alternative
//users.forEach{
//   (user,i,list) => {
//        console.log('i = 9[i],user=$(user))
//   }
//}

