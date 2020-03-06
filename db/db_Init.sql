/* create db*/
CREATE DATABASE data_quality;
CREATE DATABASE ladybug_source;

-- hive1
SELECT 18 as ct
-- hive2
SELECT 2020 as ct

-- exactly1
select 1 as hotel_id ,'rujia' as hotel_name union select 2 as hotel_id ,'qitian' as hotel_name union select 3 as hotel_id ,'su8' as hotel_name
select hotel_id ,hotel_name from source_hotel
/*
CREATE TABLE IF NOT EXISTS  ladybug_source.`source_hotel` (
  `hotel_id` int(10) NOT NULL,
  `hotel_name` varchar(200) NOT NULL
);
insert into ladybug_source.`source_hotel`
(`hotel_id`, `hotel_name`)
values
(1,'rujia'),
(2,'qitian');
*/
select hotel_id ,hotel_name from source_hotel
select 1 as hotel_id ,'rujia' as hotel_name union select 2 as hotel_id ,'qitian' as hotel_name

-- oracle
SELECT 6 AS ct FROM sys.dual

-- hive3 schemal change
/*
CREATE TABLE IF NOT EXISTS  ladybug_source.`source_user` (
  `user_id` int(10) NOT NULL,
  `user_name` varchar(200) NOT NULL,
  `addr` varchar(200) NOT NULL
);
INSERT INTO ladybug_source.source_user
(user_id, user_name, addr)
VALUES
(1, 'zs', 'shanghai'),
(2,'zl','xian');
*/
SELECT case column_name
           when 'user_id' then 'id'
           when 'user_name' then 'foo'
           when 'addr' then 'bar'
           else column_name
       end as 'field'
FROM information_schema.columns
WHERE table_name = 'source_user'
  AND table_schema = 'ladybug_source'
/*
CREATE table  ladybug_dw.demo1 (id int,foo STRING, bar STRING);
INSERT OVERWRITE TABLE ladybug_dw.demo1 
SELECT 1 as id , 'zs' as foo, 'shanghai' as bar
UNION SELECT 2 as id , 'ls' as foo, 'shenzhen' as bar
UNION SELECT 3 as id , 'ww' as foo, 'beijing' as bar
*/
SHOW COLUMNS FROM ladybug_dw.demo1