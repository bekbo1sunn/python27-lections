# Slash commands
* \l - список всех бд
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключение к какой-то бд
* \du - список всех пользователей в postgres
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация о таблицах в текущей бд
* \d+ name_of_table - подробная информация о таблице 
* \q - выход из СУБД(psql)


# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание бд
```

```sql
CREATE TABLE name_of_table(
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создание таблицы
```

```sql
DROP DATABASE name_of_db;
-- удаление бд

DROP TABLE name_of_table;
-- удаление таблицы
```

```sql
 INSERT INTO product
VALUES
('apple', 100, '...'),
('banan', 200, '...');
-- заполнение таблицы
```

# Условия
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию


DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию
```

```sql
SELECT * FROM name_of_table WHERE column = 'hello';
строгое равенство
```

```sql
SELECT * FROM name_of_table WHERE column LIKE '%hello%';
-- записи включающие в себя данную строку с учетом регистра
-- aaahello
-- hello world
-- hello
-- Hello world  - не пройдет (потому что регистр другой) 
```

```sql
SELECT * FROM name_of_table WHERE column ILIKE '%hello%';
-- записи включающие в себя данную строку без учета регистра
-- aaahello
-- hello world
-- hello
-- Hello world 
-- HeLLo
```

```sql
SELECT * FROM name_of_table ORDER BY column;
-- сортировка записей по данному полю в порядке возрастания
```

```sql
SELECT * FROM name_of_table ORDER BY column DESC;
-- сортировка записей по данному полю в порядке убывания
```

```sql
SELECT * FROM name_of_table LIMIT 10;
-- вывод первых 10 записей
```

```sql
SELECT * FROM name_of_table OFFSET 10;
-- пропускаем первые 10 записей
```

```sql
SELECT * FROM name_of_table LIMIT 10 OFFSET 5;
-- пропускаем первые 5 записей
-- вытаскиваем 10 записей
```

# Обновление таблицы
```sql
ALTER TABLE name_of_table ADD COLUMN col_name col_type constraint;
-- добавляем новую колонку в таблицу
```

```sql
ALTER TABLE name_of_table DROP COLUMN col_name;
-- удаляем колонку из таблицы
```

```sql
ALTER TABLE name_of_table RENAME COLUMN col_name TO new_col_name;
-- переименновывание колонки
```

```sql
ALTER TABLE name_of_table ALTER COLUMN col_name SET DATA TYPE new_type;
-- изменение типа данных у поля
```

# Ограничения (constraints)
* `UNIQUE` - не разрешает дубликаты
* `NOT NULL` - требует обязательного заполнения поля
* `PRIMARY KEY` - как UNIQUE и NOT NULL + строит binary tree для быстрого поиска
* `FOREIGN KEY` - ссылается на `PRIMARY KEY` в другой таблице и проверяет 
существует ли такой id


# Связи
## Виды связей
> Один к одному (one to one)
* один человек - один профиль
* один автор - одна автобиография
> Один ко многим (one to many)
* один блоггер - много постов
* одна марка - много моделей
* одна страна - много областей
* один продукт - много комментариев
> Многие ко многим (many to many)
* один разработчик - много проектов. один проект - много разработчиков

## Реализация one2many в postgres 
```sql
CREATE TABLE blogger (
    id serial PRIMARY KEY,
    name varchar(50),
    age int
);

CREATE TABLE post (
    id serial PRIMARY KEY,
    title varchar(100),
    body text,
    blogger_id int,

    CONSTRAINT fk_blogger_post
    FOREIGN KEY (blogger_id) REFERENCES blogger(id)
)
```



## Реализация one2one в postgres 
```sql
CREATE TABLE author (
    id serial PRIMARY KEY,
    name varchar(50),
    last_name varchar(70),
);

CREATE TABLE autobiography (
    id serial PRIMARY KEY,
    piblished data,
    body text,
    author_id int UNIQUE,

    CONSTRAINT fk_autor_bio
    FOREIGN KEY (author_id) REFERENCES author(id)
)
```

## Реализация many2many в postgres 
```sql
CREATE TABLE developer (
    id serial PRIMARY KEY,
    name varchar(50),
    age int,
    experience int
);

CREATE TABLE project (
    id serial PRIMARY KEY,
    title varchar(100),
    tz text,
    deadline date
);

CREATE TABLE dev_pro (
    dev_id int,
    proj_id int,

    CONSTRAINT fk_dev_m2m
    FOREIGN KEY (dev_id) REFERENCES developer(id)

    CONSTRAINT fk_proj_m2m
    FOREIGN KEY (proj_id) REFERENCES project(id)
);
```
# JOINS
> **JOIN** - инструкция которая позволяет одним selectом брать данные из двух
таблиц (у которых есть связанные поля)

> **INNER JOIN (JOIN)** - достаются только те записи у которых есть данные в обоих таблицах

>**FULL JOIN** - достаются все записи и с первой и со второй таблицы

```sql
-- one2one / one2many
SELECT * FROM blogger 
JOIN post ON blogger.id = post.blogger_id;
```

```sql
-- many2many
SELECT * FROM developer
JOIN dev_proj ON developer.id = dev_proj.dev_id
JOIN project ON project.id = dev_proj.proj_id;
```