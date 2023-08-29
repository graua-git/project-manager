SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Projects;
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
    `trip` int NOT NULL,
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
    `name` char(50), NOT NULL,
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
