$dbname = "mydatabase1";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Retrieve the user data from the database
$query = "SELECT * FROM users";
$result = $conn->query($query);

// Display the user data in an HTML table
if ($result->num_rows > 0) {
  echo "<table>";
  echo "<tr><th>ID</th><th>Username</th><th>Email</th><th>Password</th></tr>";
  while ($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row["id"] . "</td><td>" . $row["username"] . "</td><td>" . $row["email"] . "</td><td>" . $row["password"] . "</td></tr>";
  }
  echo "</table>";
} else {
  echo "No users found.";
}

// Close the database connection
$conn->close();
?>