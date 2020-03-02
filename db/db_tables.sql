CREATE TABLE `user` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test case owner id',
	`name` varchar(200) NOT NULL COMMENT 'case owner name',
	`password` varchar(200) NOT NULL COMMENT 'login password',
	`email` varchar(200) NOT NULL COMMENT 'case owner email',
	`mobile` varchar(20) NOT NULL COMMENT 'mobile number',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when owner is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when owner is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='test case owner';

CREATE TABLE `db_connect` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'database connection id',
	`db_connect_name` varchar(200) NOT NULL COMMENT 'database connection name',
	`db_connect_type` int NOT NULL COMMENT '1.hive, 2.mysql, 3.oracle',
	`host` varchar(200) NOT NULL COMMENT 'database connection url address',
	`port` int NOT NULL COMMENT 'database connection port',
	`username` varchar(200) NOT NULL COMMENT 'database connection username',
	`password` varchar(200) NOT NULL COMMENT 'database connection password',
	`db_name` varchar(200) NOT NULL COMMENT 'database name',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when database connection is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when database connection is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='database connection';

CREATE TABLE `email_template` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'email_template id',
	`email_subject` varchar(1000) NOT NULL COMMENT 'email_template name',
	`msg_template` text NOT NULL COMMENT 'email message template',
	`email_to` varchar(4000) NOT NULL COMMENT 'email to address',
	`email_cc` varchar(4000) NULL COMMENT 'email cc address',
	`email_bcc` varchar(4000) NULL COMMENT 'email bcc address',
	`description` varchar(1000) NULL COMMENT 'email_template description',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when email_template is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when email_template is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='data quality email template';

CREATE TABLE `task_case` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test case id',
	`task_case_name` varchar(1000) NOT NULL COMMENT 'Unique key for the test case. It should be named as what it does',
	`alias` varchar(1000) NULL COMMENT 'alias use to show task_case_name as a sepcial naming format',
	`description` varchar(1000) NULL COMMENT 'Comments of current case',
	`source_sql` text NULL COMMENT 'SQL text from source side',
	`source_connect_id` int NULL COMMENT 'source database connection id',
	`destination_sql` text NULL COMMENT 'SQL text from destination (data warehouse)',
	`destination_connect_id` int NULL COMMENT 'destination database connection id',
	`is_enabled` tinyint NOT NULL COMMENT '0:disable 1:enable',
	`match_type` int NOT NULL COMMENT '1.exactly, 2.range',
	`threshlod_low` int NULL COMMENT 'Lowest value that the case result allows',
	`threshlod_high` int NULL COMMENT 'Highest value that the case result allows',
	`duration_limit` int NOT NULL COMMENT 'The time limitation that the case allows running (unit: seconds). It is used for test case monitor',
	`last_run` datetime NULL COMMENT 'The test case last running time.',
	`owner_id` int NOT NULL COMMENT 'The test case owner id',
	`email_template_id` int NOT NULL COMMENT 'dq email id',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when case is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when case is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='tesk case data table';

CREATE TABLE `task_group` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test case group id',
	`task_group_name` varchar(1000) NOT NULL COMMENT 'Unique key for the test case group. It should be named as what it does',
	`description` varchar(1000) NULL COMMENT 'Comments of current task_group',
	`owner_id` int NOT NULL COMMENT 'The test case group owner id',
	`is_enabled` tinyint NOT NULL COMMENT '0:disable 1:enable',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when task_group is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when task_group is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='tesk case group data table';

CREATE TABLE `task_scenarios` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test case scenarios id',
	`task_scenarios_name` varchar(1000) NOT NULL COMMENT 'Unique key for the test case scenarios. It should be named as what it does',
	`description` varchar(1000) NULL COMMENT 'Comments of current task_scenarios',
	`owner_id` int NOT NULL COMMENT 'The test case scenarios owner id',
	`is_enabled` tinyint NOT NULL COMMENT '0:disable 1:enable',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when scenarios is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when scenarios is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='test case scenarios data table';

CREATE TABLE `case_group` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The case_group id',
	`task_case_id` int NOT NULL COMMENT 'The test case id',
	`task_group_id` int NOT NULL COMMENT 'The test case group id',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when case_group is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when case_group is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='case group data table';

CREATE TABLE `group_scenarios` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The group_scenarios id',
	`task_group_id` int NOT NULL COMMENT 'The test case group id',
	`task_scenarios_id` int NOT NULL COMMENT 'The test scenarios id',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when group_scenarios is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Updated time when group_scenarios is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='group_scenarios data table';

CREATE TABLE `task_case_result` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test case result id',
	`task_case_id` int NOT NULL COMMENT 'The test case id',
	`task_execution_id` int NOT NULL COMMENT 'The execution id',
	`current_status` varchar(50) NOT NULL COMMENT 'processing / success / failed',
	`execution_start` datetime NULL COMMENT 'Start date of the execution',
	`execution_end` datetime NULL COMMENT 'End date of the execution',
	`source_result` text NULL COMMENT 'Source SQL returned result',
	`destination_result` text NULL COMMENT 'Destination SQL returned result',
	`diff` text NULL COMMENT 'The diff details',
	`result_message` text NULL COMMENT 'Return detail while running the case.',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when TestCaseResult is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Update time when TestCaseResult is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='test case group data table';

CREATE TABLE `task_execution` (
	`id` int NOT NULL AUTO_INCREMENT COMMENT 'The test execution id',
	`execution_type` varchar(50) NOT NULL COMMENT 'TaskScenarios / TaskGroup',
	`execution_name` varchar(1000) NULL COMMENT 'ScenariosName / GroupName',
	`current_status` varchar(50) NOT NULL COMMENT 'processing / success / failed',
	`execution_start` datetime NULL COMMENT 'Start date of the execution',
	`execution_end` datetime NULL COMMENT 'End date of the execution',
	`insert_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Inserted time when execution is created',
	`update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Update time when execution is updated',
	PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET=utf8mb4 COMMENT='test case execution data table';
