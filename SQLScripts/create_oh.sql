create schema `ohdb`;
create table `ohdb`.`OfficeHours`(
    `id` int(8),
	`ta_id` int(8),
    `location` varchar(24),
    `course_name` varchar(24),
    `zoom_link` varchar(24),
    `start_time` time(0),
    `end_time` time(0)
);

INSERT INTO `ohdb`.`OfficeHours` VALUES(
	1, 234, "CSC 451", "Intro to Databases", "examplezoomlink.zom", '11:15:45', '11:45:45'
);