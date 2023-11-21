
        document.addEventListener('DOMContentLoaded', function () {
            const form = document.querySelector('form');

            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent the form from submitting by default

                const name = document.getElementById('name').value;
                const username = document.getElementById('usrname').value;
                const password = document.getElementById('password').value;
                const confirmPassword = document.getElementById('cpassword').value;
                const mobileNumber = document.getElementById('number').value;
                const gender = document.getElementById('inputState').value;
                const checkbox = document.getElementById('gridCheck').checked;

                if (name === '' || username === '' || password === '' || confirmPassword === '' || mobileNumber === '' || !checkbox) {
                    alert('Please fill in all required fields and agree to the terms and conditions.');
                } else if (password !== confirmPassword) {
                    alert('Passwords do not match.');
                } else {    
                    alert('Form submitted successfully!');
                }
            });
        });
