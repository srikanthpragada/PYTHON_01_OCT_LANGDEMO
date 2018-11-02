create table jobs
(  job_id  text(5) primary key,
   job_title text(30) not null,
   min_salary integer
);


insert into jobs values('PP','Python Programmer',20000);
insert into jobs values('JP','Java Programmer',15000);
insert into jobs values('OD','Oracle DBA',30000);
