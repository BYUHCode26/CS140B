document.getElementById('signup-form').addEventListener('submit',function(event) {
    event.preventDefault(); //Purpose: To go to a new page
    alert("Form is submitted!");

    const personName = document.getElementById('personName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    
    if (!personName || !email || !age) {
        alert("You need an email, name and age!")
        return;
    }
    if (age < 18) {
        alert("You are underage mofo!")
        return;
    }

    // if (!age || age < 18) {
    //     alert("You need to be 18 dummah!")
    //     return;
    //}
    const formData = {
        name: personName,
        email: email,
        password: password,
        age: age,
    };
    console.log(formData);

    //Code for interacting after submission
    console.log(formData);
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "submit.json", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onreadystatechange = function () {
        if(xhr.readyState === 4 && xhr.status === 200) {
            alert('Form submitted successfully. ' + ` Success: ${personName}`);  //Determined
            message = document.getElementById('message');
            const response = JSON.parse(xhr.responseText);
            message.textContent = response.message;
            form = document.getElementById('signup-form');
            form.reset();
            //form.textContent = '';
        } else if (xhr.readyState === 4) {
            alert('Error submitting form.');
        }
    };
    xhr.send(JSON.stringify(formData));
});
//Add this somewhere for the form to work
//<div id = "message"></div>