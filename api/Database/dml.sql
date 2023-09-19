-- Users
-- Read Users
SELECT user_id, email, first_name, last_name FROM Users;

-- Delete User
DELETE FROM Users WHERE user_id = {id};


-- Projects
-- Read Projects
SELECT * FROM Projects;

-- Read One Project
SELECT * FROM Projects WHERE project_id = {project_id} AND EXISTS
(SELECT * FROM Memberships WHERE project = {project_id} AND user = {user_id})

-- Read My Projects
SELECT project_id, name, owner
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


-- Tasks
-- Read Tasks By Project
SELECT * FROM Tasks WHERE project = {project_id} AND EXISTS 
(SELECT * FROM Memberships WHERE project = {project_id} AND user = {user_id})
ORDER BY date_created DESC, time_created;