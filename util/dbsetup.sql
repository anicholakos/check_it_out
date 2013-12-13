create table persons (
    id  integer primary key autoincrement,
    f_name  varchar(25),
    l_name  varchar(25),
    email varchar(50),
    phone varchar(14)
       
);

create table items (
    pk  integer primary key autoincrement,
    aps_num varchar(25),
    id_num varchar(25),
    model varchar(25),
    make varchar(25),
    item_type varchar(25),
    specs varchar(25)
);

create table loans (
    person_id  integer,
    person_fname varchar(25),
    person_lname varchar(25),
    item_id integer,
    itemnum varchar(25),
    checked_out date not null,
    foreign key(person_id) references persons(id),
    foreign key(person_fname) references persons(f_name),
    foreign key(person_lname) references persons(l_name),
    foreign key(item_id) references items(pk),
    foreign key(itemnum) references items(id_num)
);

create table users(
    id integer,
    username varchar(25),
    password varchar(25)
);

insert into persons (f_name,l_name,email,phone)  values ('Bob', 'Hans', 'bh@gmail.com', '1111111111');
insert into persons (f_name,l_name,email,phone)  values ('Greg', 'Bennington', 'gb@gmail.com', '2222222222');
insert into persons (f_name,l_name,email,phone)  values ('Charlie', 'Brown', 'cb@gmail.com', '3333333333');
insert into persons (f_name,l_name,email,phone)  values ('Raquel', 'Sanchez', 'rs@gmail.com', '3333344444');

insert into items (aps_num, id_num, model, make, item_type, specs) values ('8675309', '7734', '13375w46', 'Dell', 'Laptop', 'Super cool laptop');
insert into items (aps_num, id_num, model, make, item_type, specs) values ('Null', '123456789', '938djdw', 'Gateway', 'Laptop', 'Brown laptop');
insert into items (aps_num, id_num, model, make, item_type, specs) values ('1003643', '76876', '7687676', 'asd', 'asdghj', 'vbnnbv');

insert into items (aps_num, id_num, model, make, item_type, specs) values ('479102387', '42', '7490123865', 'Stuff', 'Stoof', 'Cool laptop');

insert into items (aps_num, id_num, model, make, item_type, specs) values ('2343848584','23485859', 'Apple', 'dfdf','phone','black');
insert into items (aps_num, id_num, model, make, item_type, specs) values ('APS-CC 4R2P4H1', '10344247525(express service tag)', 'Latitude D630', 'Dell', '.', '.');
