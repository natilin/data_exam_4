from config.base import session_factory
from sqlalchemy import text


def create_tables():
    with session_factory() as session:
        session.execute(text("""
        create table if not exists country (
            country_id serial primary key,
            country_name varchar(100) unique not null
            );
            
            create table if not exists city (
            city_id serial primary key,
            city_name varchar(100) not null,
            country_id int ,
            foreign key (country_id) references country(country_id)
            );
            
            
            create table if not exists industry (
            industry_id serial primary key,
            industry_name varchar(255) unique not null
            );
            
            
            
            create table if not exists position(
            position_id serial primary key,
            target_longitude NUMERIC(10, 6),
            target_latitude NUMERIC(10, 6),
            target_id varchar(100) unique,
            city_id int,
            foreign key (city_id) references city(city_id)
            );
            
            
            create table if not exists mission(
            mission_id serial primary key,
            position_id int,
            industry_id int,
            target_priority varchar(100),
            target_type varchar(255),
            foreign key (position_id) references position(position_id),
            foreign key (industry_id) references industry(industry_id)
            );
        """))
        session.commit()


def insert_data():
    with session_factory() as session:
        session.execute(text("""
        insert into country (country_name)
            select distinct target_country
            FROM missions
            where target_country is not NULL
            on conflict (country_name) do nothing
            
            
            insert into city (city_name, country_id)
            select distinct
                m.target_city,
                c.country_id
            from missions m
            join country c on m.target_country = c.country_name
            where m.target_city is not null;
            
            
            insert into industry (industry_name)
            select distinct target_industry
            from missions
            where target_industry is not null
            on conflict (industry_name) do nothing;
            
            insert into position (target_longitude, target_latitude, target_id,city_id)
            select distinct
                m.target_longitude,
                m.target_latitude,
                m.target_id,
                c.city_id
            from missions m
            join city c on m.target_city = c.city_name
            ON CONFLICT (target_id) DO NOTHING;
            
            
            
            insert into mission(position_id, industry_id, target_priority, target_type)
                select distinct
                p.position_id,
                i.industry_id,
                m.target_priority,
                m.target_type
                from missions m
                join industry i on m.target_industry = i.industry_name
                join city c on m.target_city = c.city_name
                join position p on m.target_longitude = p.target_longitude
                and m.target_latitude = p.target_latitude
                and m.target_id = p.target_id
                and c.city_id = p.city_id
                 """))
        session.commit()
