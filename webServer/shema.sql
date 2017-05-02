create table user(
  user_id integer primary key autoincrement,
  fname text not null,
  lname text not null,
  emailp1 text not null,
  emailp2 text not null,
  emailAccept boolean not null
);
