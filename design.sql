--Nick Soetaert
--December 4, 2018

drop table Player cascade constraints;

drop table Club_member cascade constraints;

drop table Officer cascade constraints;

drop table Officer_role cascade constraints;

drop table Game cascade constraints;

drop table Time_control cascade constraints;

drop table Move cascade constraints;

drop table Game_venue cascade constraints;

drop table Meeting cascade constraints;

drop table Meeting_attendance cascade constraints;

drop table Tournament cascade constraints;

drop table Tournament_bracket cascade constraints;

create table player(
   STU_ID char(9),
   fname varchar(30) not null,
   lname varchar(30) not null,
   primary key(stu_id)
);

create table club_member(
   STU_ID char(9),
   email varchar(30) not null,
   primary key(stu_id),
   foreign key(stu_id) references player(stu_id)
);

create table officer(
   STU_ID char(9),
   primary key(stu_id),
   foreign key(stu_id) references club_member(stu_id)
);

create table officer_role(
    STU_ID char(9),
    ROLE   varchar(20),
    foreign key (stu_id) references officer
);

create table Game_venue(
    ROOM_NUM integer,
    primary key(ROOM_NUM)
);

create table Meeting(
    ROOM_NUM integer,
    MEETING_DATE date,
    primary key(room_num, meeting_date),
    foreign key(room_num) references Game_venue
);

create table Meeting_attendance(
    ROOM_NUM integer,
    MEETING_DATE date,
    ATTENDEE char(9),
    primary key(room_num, meeting_date, attendee),
    foreign key(room_num, meeting_date) references Meeting
);

create table Tournament(
    ROOM_NUM integer,
    MEETING_DATE date,
    winner char(9),
    primary key(room_num, meeting_date),
    foreign key(room_num) references Game_venue(room_num),
    foreign key(winner) references Player(stu_id)
);

create table Tournament_bracket(
    ROOM_NUM integer,
    MEETING_DATE date,
    CONTESTANT char(9),
    primary key(room_num, meeting_date, contestant),
    foreign key(room_num, meeting_date) references tournament
);

create table Game(
    GAME_ID char(5),
    w_player char(9),
    b_player char(9),
    white_result number(2,1),
    black_result number(2,1),
    day_played date,
    room_num integer,
    primary key(GAME_ID),
    foreign key(w_player) references player(stu_id),
    foreign key(b_player) references player(stu_id),
    foreign key(day_played, room_num) references Meeting(meeting_date, room_num)
);

create table time_control(
    GAME_ID char(5),
    start_time_mins integer,
    move_increment_sec integer,
    primary key(GAME_ID),
    foreign key(GAME_ID) references game
);

create table Move(
    GAME_ID char(5),
    MOVE_NUM integer,
    move_w varchar(8),
    move_b varchar(8),
    primary key(GAME_ID, MOVE_NUM),
    foreign key(GAME_ID) references game
);


