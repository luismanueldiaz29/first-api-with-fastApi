create table author
(
    author_id bigserial
        constraint author_pk
            primary key,
    name      varchar(250) not null,
    age       timestamp    not null,
    gender    varchar(1)
);


create table book
(
    book_id     bigserial
        constraint book_pk
            primary key,
    author_id   bigint       not null
        constraint author_fk
            references author,
    title       varchar(250) not null,
    rating      varchar(100) not null,
    "createdAt" timestamp    not null
);