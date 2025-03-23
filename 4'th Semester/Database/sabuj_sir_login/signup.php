<?php
// Connect to the MySQL database
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mydatabase1";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Process the form data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = $_POST["username"];
  $email = $_POST["email"];
  $password = $_POST["password"];

  // Validate the input
  // ...

  // Check if the username or email is already in use
  $query = "SELECT * FROM users WHERE username='$username' OR email='$email'";
  $result = $conn->query($query);

  if ($result->num_rows > 0) {
    echo "Username or email is already in use.";
  } else {
    // Insert the user data into the database
    $query = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$password')";
    if ($conn->query($query) === TRUE) {
      echo "User created successfully.";
    } else {
      echo "Error creating user: " . $conn->error;
    }
  }

  // Close the database connection
  $conn->close();
}
?>