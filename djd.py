<!DOCTYPE html>
<html>
<head>
    <title>Task Tracker</title>
</head>
<body>
    <h1>My Task List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="New task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
