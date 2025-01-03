//  Task 2

let arr = [10, 20, 30, 40, 50, 60, 70, 80, 90];

let slice1 = arr.slice(0, 3);
console.log("Slice 1:", slice1);

let slice2 = arr.slice(3, 6);
console.log("Slice 2:", slice2);

let slice3 = arr.slice(0, arr.length).filter((value, index) => index % 2 === 0);
console.log("Slice 3:", slice3);


//  Task 3

let currentDate = new Date();

let formattedDate = currentDate.getFullYear() + '/' +
                    (currentDate.getMonth() + 1).toString().padStart(2, '0') + '/' +
                    currentDate.getDate().toString().padStart(2, '0') + '/' +
                    currentDate.getHours().toString().padStart(2, '0') + '/' +
                    currentDate.getMinutes().toString().padStart(2, '0') + '/' +
                    currentDate.getSeconds().toString().padStart(2, '0');

console.log(formattedDate);


//  Task 4

function generatePassword(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?';
    
    let password = '';
  
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      
      password += characters[randomIndex];
    }
    
    return password;
  }
  
  let generatedPassword = generatePassword(12);
  console.log("Generated Password: " + generatedPassword);
  