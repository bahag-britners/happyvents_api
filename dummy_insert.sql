-- Insert dummy data into the 'users' table
INSERT INTO public.users (email, user_password) VALUES
  ('john.doe@example.com', 'password123'),
  ('alice.smith@example.com', 'pass456'),
  ('bob.jones@example.com', 'securepass'),
  ('emma.watson@example.com', 'p@ssw0rd'),
  ('michael.jordan@example.com', 'bball23');

-- Insert dummy data into the 'events' table
INSERT INTO public.events (title, description, address, image, event_date, likes, price) VALUES
  ('Concert Night', 'Live music from various artists', '123 Main St', '', '2023-12-01', 2, 20.99),
  ('Tech Conference', 'Latest trends in technology', '456 Tech Blvd', '', '2023-12-10', 0, 50.00),
  ('Food Festival', 'Taste the best cuisines in town', '789 Food Ave', '', '2023-12-15', 1, 15.99),
  ('Fitness Workshop', 'Get fit with professional trainers', '101 Fitness St', '', '2023-12-20', 1, 30.50),
  ('Art Exhibition', 'Explore beautiful artworks', '202 Art Gallery', '', '2023-12-25', 1, 10.00);

-- Insert dummy data into the 'user_comments' table
INSERT INTO public.user_comments (eventid, userid, content, "timestamp") VALUES
  (1000, 1000, 'Excited to attend!', '2023-12-01'),
  (1001, 1001, 'Looking forward to the keynote!', '2023-12-05'),
  (1002, 1002, 'So many delicious options!', '2023-12-10'),
  (1003, 1003, 'Great workout session!', '2023-12-15'),
  (1004, 1004, 'Incredible art pieces!', '2023-12-20');

-- Insert dummy data into the 'event_like' table
INSERT INTO public.event_like (eventid, userid) VALUES
  (1000, 1001),
  (1000, 1002),
  (1002, 1002),
  (1003, 1003),
  (1004, 1004);

-- Insert dummy data into the 'comment_like' table
INSERT INTO public.comment_like (eventid, userid, commentid) VALUES
  (1000, 1000, 1005),
  (1001, 1001, 1006),
  (1002, 1002, 1007),
  (1003, 1003, 1008),
  (1004, 1004, 1009);
