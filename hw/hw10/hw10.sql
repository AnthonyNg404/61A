CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE height <= max AND height > min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents, dogs
  WHERE parent = name
  ORDER BY -height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT parent, child, size
  FROM parents, size_of_dogs
  WHERE child = name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT b.child || " and " || a.child || " are " || a.size || " siblings"
  FROM siblings AS a, siblings  AS b
  WHERE a.size = b.size AND a.parent = b.parent AND a.child <> b.child
  GROUP BY a.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
  INSERT INTO stacks_helper SELECT a.name || ", " || b.name || ", " || c.name || ", " || d.name,
  a.height + b.height + c.height + d.height, d.height
  FROM dogs AS a, dogs AS b, dogs AS c, dogs AS d
  WHERE a.name <> d.name AND a.name <> c.name AND a.name <> b.name AND b.name > c.name AND c.name > d.name
  ORDER BY d.height;

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper
  WHERE stack_height > 170
  GROUP BY stack_height;
