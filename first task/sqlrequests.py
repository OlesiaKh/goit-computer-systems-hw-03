-- 1. Retrieve all tasks assigned to a specific user
SELECT *
FROM tasks
WHERE user_id = 1;

-- 2. Select tasks with a specific status
SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Update the status of a specific task to "in progress"
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;

-- 4. Retrieve users who do not have any tasks
SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks);

-- 5. Add a new task for a specific user
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Task Title', 'Task Description', (SELECT id FROM status WHERE name = 'new'), 1);

-- 6. Retrieve all tasks that are not yet completed
SELECT *
FROM tasks
WHERE status_id <> (SELECT id FROM status WHERE name = 'completed');

-- 7. Delete a task with a specific id
DELETE
FROM tasks
WHERE id = 1;

-- 8. Find users by a part of their email address
SELECT *
FROM users
WHERE email LIKE '%@example.com';

-- 9. Update a user's name by their id
UPDATE users
SET fullname = 'New Name'
WHERE id = 1;

-- 10. Get the number of tasks for each status
SELECT status.name, COUNT(tasks.id)
FROM status
LEFT JOIN tasks ON status.id = tasks.status_id
GROUP BY status.name;

-- 11. Retrieve tasks assigned to users with a specific domain in their email address
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

-- 12. Retrieve tasks without a description
SELECT *
FROM tasks
WHERE description IS NULL
   OR description = '';

-- 13. Select users and their tasks that have the status "in progress"
SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Retrieve users and the number of tasks assigned to each of them
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;
