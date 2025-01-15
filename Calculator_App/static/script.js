function performOperation(operation) {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    if (num1 === '') {
        document.getElementById('result').textContent = 'Please enter the first number.';
        return;
    }

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ operation, num1, num2: num2 || null }), // Send num2 only if it's provided
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('result').textContent = `Error: ${data.error}`;
            } else {
                document.getElementById('result').textContent = `Result: ${data.result}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').textContent = 'An error occurred.';
        });
}
