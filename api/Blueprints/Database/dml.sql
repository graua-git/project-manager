-- Users
-- Read Users
SELECT user_id, email, first_name, last_name FROM Users;

-- Projects
-- Read Projects
SELECT * FROM Projects;

-- Memberships
-- Read Memberships
SELECT membership_id, CONCAT(first_name, ' ', last_name) AS participant_name, email, name AS project, creator
FROM Memberships
JOIN Users ON Users.user_id = Memberships.user
JOIN Projects on Projects.project_id = Memberships.project;