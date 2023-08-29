SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Memberships;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Settings;
SET FOREIGN_KEY_CHECKS = 1;

-- Users
CREATE TABLE `Users` (
    `user_id` int AUTO_INCREMENT NOT NULL,
    `email` char(50) UNIQUE NOT NULL,
    `password` char(50) NOT NULL,
    `first_name` char(15) NOT NULL,
    `last_name` char(15) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Projects
CREATE TABLE `Projects` (
    `project_id` int AUTO_INCREMENT NOT NULL,
    `name` char(50) NOT NULL,
    PRIMARY KEY (`project_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Memberships
CREATE TABLE `Memberships` (
    `membership_id` int AUTO_INCREMENT NOT NULL,
    `user` int NOT NULL,
    `project` int NOT NULL,
    `creator` boolean NOT NULL DEFAULT 0,
    PRIMARY KEY (`membership_id`),
    FOREIGN KEY (`user`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`project`)
        REFERENCES Projects(`project_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT unique_user_trip UNIQUE(`user`, `project`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Categories
CREATE TABLE `Categories` (
    `category_id` int AUTO_INCREMENT NOT NULL,
    `project` int NOT NULL,
    `name` char(50) NOT NULL,
    PRIMARY KEY (`category_id`),
    FOREIGN KEY (`project`)
        REFERENCES Projects(`project_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Tasks
CREATE TABLE `Tasks` (
    `task_id` int AUTO_INCREMENT NOT NULL,
    `project` int NOT NULL,
    `category` int NOT NULL,
    `created_by` int NOT NULL,
    `assignee` int,
    `name` char(50) NOT NULL,
    `date_created` char(10) NOT NULL,
    `time_created` char(8) NOT NULL,
    `due_date` char(10),
    `subtask_of` int,
    `completed` boolean DEFAULT 0,
    PRIMARY KEY (`task_id`),
    FOREIGN KEY (`project`)
        REFERENCES Projects(`project_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`category`)
        REFERENCES Categories(`category_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`created_by`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`assignee`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


-- SAMPLE DATA --

-- Users
INSERT INTO `Users` (`email`, `password`, `first_name`, `last_name`)
VALUES ('johndoe@email.com', 'password1234', 'John', 'Doe'),
        ('janedoe@email.com', '@password', 'Jane', 'Doe'),
        ('johnsmith@email.com', 'pAsSwOrD', 'John', 'Smith'),
        ('jesssmith@email.com', 'pass_word', 'Jess', 'Smith');

-- Trips
INSERT INTO `Projects` (`name`)
VALUES ('Doe Project'),
        ('John Project'),
        ('Smith Project');

-- Memberships
INSERT INTO `Memberships` (`user`, `project`, `creator`)
VALUES (1, 1, 1), -- John Doe // Doe Project
        (2, 1, 0), -- Jane Doe // Doe Project
        (1, 2, 1), -- John Doe // John Project
        (3, 2, 0), -- John Smith // John Project
        (3, 3, 0), -- John Smith // Smith Project
        (4, 3, 1); -- Jess Smith // Smith Project

-- Categories
INSERT INTO `Categories` (`project`, `name`)
VALUES (1, 'Chores'),
        (1, 'Work'),
        (2, 'Math'),
        (2, 'History'),
        (3, 'Bathroom'),
        (3, 'Living Room');

-- Tasks
INSERT INTO `Tasks` (`project`, `category`, `created_by`, `assignee`, `name`, `subtask_of`, `date_created`, `time_created`, `due_date`)
VALUES (1, 1, 1, null, 'Laundry', null, '2023/08/29', '15:32:41', null),
        (1, 1, 2, null, 'Dishes', null, '2023/08/29', '15:32:43', null),
        (1, 2, 1, null, 'Payroll', null, '2023/08/30', '15:32:43', null),
        (2, 3, 3, null, 'Homework', null, '2023/08/29', '15:31:43', '2023/08/31'),
        (2, 3, 3, null, '5.5', 4, '2023/08/29', '15:32:43', null),
        (2, 4, 1, null, 'Presentation', null, '2023/08/30', '15:32:43', null),
        (3, 5, 4, null, 'Clean Toilet', null, '2023/08/28', '15:32:43', null),
        (3, 6, 4, null, 'Clean Kitchen', null, '2023/08/29', '15:33:43', null),
        (3, 6, 4, null, 'Do Dishes', 8, '2023/09/01', '15:32:43', null);