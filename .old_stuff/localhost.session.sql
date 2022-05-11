-- INSERT INTO name (first_name, middle_name, last_name)
-- VALUES ("Steven", "L", "O'Driscoll");

-- INSERT INTO group_types (name)
-- VALUES ('self');

-- INSERT INTO types (name)
-- VALUES ('WORK');

-- INSERT INTO address (street, city, state, zip, type, contact_id)
-- VALUES ('2449 E. Jim Bridger Dr.', 'Eagle Mountain', 'Utah', '84005', '1', '1');

-- insert into email (address, type, contact_id)
-- values ('slodriscoll@gmail.com', '1', '1');

-- insert into phone_number (number, type, contact_id)
-- values ('8016023943', '1', '1');

select id
from name
order by id desc limit 0, 1