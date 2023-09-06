-- Users
-- Read Users
SELECT user_id, email, first_name, last_name FROM Users;

-- Delete User
DELETE FROM Users WHERE user_id = {id};

-- Projects
-- Read Projects
SELECT * FROM Projects;

-- Read My Projects
SELECT name, owner
FROM Projects
JOIN Memberships ON Memberships.project = Projects.project_id
JOIN Users ON Users.user_id = Memberships.user
JOIN (SELECT project, creator, CONCAT(Users.first_name, ' ', Users.last_name) as owner
FROM Memberships
JOIN Users ON Users.user_id = Memberships.user
WHERE creator = 1) as Creators ON Projects.project_id = Creators.project
WHERE Users.user_id = {user_id};

-- Memberships
-- Read Memberships
SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS project, creator
FROM Memberships
JOIN Users ON Users.user_id = Memberships.user
JOIN Projects on Projects.project_id = Memberships.project;