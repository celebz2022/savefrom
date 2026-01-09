body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background-color: #f6f6f6;
    margin: 0;
    padding: 0;
    text-align: center;
}

.container {
    background-color: #ffffff;
    width: 90%;
    max-width: 550px;
    margin: 80px auto;
    padding: 40px 30px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

h2 {
    font-size: 24px;
    font-weight: 700;
    color: #111;
    margin-bottom: 30px;
}

input[type=text] {
    width: 80%;
    max-width: 450px;
    padding: 14px 16px;
    margin-bottom: 20px;
    font-size: 16px;
    border: 1px solid #dcdcdc;
    border-radius: 8px;
    box-sizing: border-box;
    transition: all 0.2s ease;
}

input[type=text]:focus {
    outline: none;
    border-color: #ffce00;
    box-shadow: 0 0 5px rgba(255, 206, 0, 0.5);
}

button {
    padding: 14px 30px;
    font-size: 16px;
    font-weight: 700;
    color: #111;
    background-color: #ffce00;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
}

button:hover {
    background-color: #ffb900;
    transform: translateY(-2px);
}

footer {
    margin-top: 25px;
    font-size: 13px;
    color: #888;
}

@media (max-width: 600px) {
    .container {
        padding: 30px 20px;
        margin: 60px 10px;
    }

    input[type=text] {
        width: 100%;
    }
}
