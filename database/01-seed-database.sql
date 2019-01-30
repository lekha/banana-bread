INSERT INTO cafe.users (id, user_id, name, email, avatar, tokens) VALUES
    (1, 1, 'Mike Wazowski', 'mike@monsters.inc', 'www.monsters-r-us-profiles.com/mike', '12345'),
    (2, 2, 'Emily Dickinson', 'emily@poets.com', 'www.poetsociety.com/emily', '67890'),
    (3, 3, 'Shimrit Seuss', 'shimrit@rhymes.com', 'www.hortonhearsawho.com/seuss', '24680'); 

INSERT INTO cafe.bakers (id, name) VALUES
    (1, 'Mike'),
    (2, 'Emily'),
    (3, 'Shimrit');

INSERT INTO cafe.foods (id, baker_id, image_url) VALUES
    (1, 1, '/media/1.jpg'),
    (2, 2, '/media/2.jpg'),
    (3, 3, '/media/3.jpg');

INSERT INTO cafe.categories (name, superlative) VALUES
    ('presentation', 'prettier'),
    ('taste', 'tastier'),
    ('texture', 'best textured');
