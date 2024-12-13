document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // ყველა input და select ელემენტი
    const fields = ['name', 'email', 'password', 'gender', 'country', 'terms'];
    let valid = true;

    // ამოწმებს თითოეულ input-ს, რომ სწორად იყოს შეყვანილი
    fields.forEach(function(field) {
        const element = document.getElementById(field);
        if (!element.value || (field === 'terms' && !element.checked)) {
            element.classList.add('error');
            valid = false;
        } else {
            element.classList.remove('error');
        }
    });

    if (valid) {
        alert("რეგისტრაცია წარმატებით დასრულდა!");
        // აქ შეგიძლიათ დაამატოთ კოდი მონაცემთა გაგზავნისთვის.
    } else {
        alert("გთხოვთ, შეავსოთ ყველა ველი და დაეთანხმოთ Terms & Conditions.");
    }
});
