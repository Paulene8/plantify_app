create database blogpostdb;

use blogpostdb;

create table blogpost
(
postID int auto_increment primary key,
username varchar(50) not null,
title varchar(255) not null,
post varchar(1000) not null
);

select *
from blogpost;

drop table blogpost