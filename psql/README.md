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
```