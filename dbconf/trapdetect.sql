create table trap (
id serial primary key,
sykoid varchar(50) not null,
syknavn varchar(50) not null,
friskoid varchar(50),
frisknavn varchar(50),
beskrivelse varchar(200),
type int2
);

create table subtrap (
trapid int2 not null references trap on update cascade on delete cascade,
suboid varchar(50) not null,
navn varchar(50) not null,
primary key (trapid,suboid)
);

create table trapkat (
trapid int2 not null references trap on update cascade on delete cascade,
kat varchar(10) not null,
primary key (trapid,kat)
);

create table org (
id serial primary key,
navn varchar(50)
);

create table bruker (
id serial primary key,
bruker varchar(10) not null,
mail varchar(40),
tlf varchar(8),
status varchar(5) not null default 'fri' check (status='fri' or status='aktiv'),
sms char(1) not null default 'N' check (sms='Y' or sms='N'),
dsms_fra varchar(8) not null default '23:30:30',
dsms_til varchar(8) not null default '06:00:00'
);

create table brukeriorg (
brukerid int2 references bruker on update cascade on delete cascade,
orgid int2 references org on update cascade on delete cascade,
primary key (brukerid,orgid)
);

create table trapeier (
orgid int2 references org on update cascade on delete cascade,
trapid int2 references trap on update cascade on delete cascade,
primary key (orgid,trapid)
);

create table varseltype (
id serial primary key,
navn varchar(9) not null
);

create table varsel (
id serial primary key,
brukerid int2 references bruker on update cascade on delete cascade,
trapid int2 references trap on update cascade on delete cascade,
kat varchar(10),
ukat varchar(10),
vtypeid int2 references varseltype on update cascade on delete cascade
);

create table unntak (
id serial primary key,
brukerid int2 references bruker on update cascade on delete cascade,
trapid int2 references trap on update cascade on delete cascade,
boksid int2 not null,
vtypeid int2 references varseltype on update cascade on delete cascade,
status varchar(5) not null check (status='minus' or status='pluss')
);

