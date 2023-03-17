# SELECT id, first,last,email
# FROM users;

# SELECT id,first,last,email
# FROM users
# ORDER BY last;

# SELECT id,name,website
# FROM trucks
# WHERE vegetarian_friendly  = true
# ORDER BY name;

# SELECT u.email, t.name
# FROM trucks t
# JOIN users u
# ON t.owner_id = u.id
# ORDER BY t.name;

# SELECT trucks.name, COUNT(reviews.id) AS num_reviews
# FROM trucks
# LEFT JOIN reviews ON trucks.id = reviews.truck_id
# GROUP BY trucks.name
# ORDER BY num_reviews DESC;

# SELECT trucks.name, COUNT(reviews.id) AS num_reviews, AVG(reviews.rating)
# AS average_rating FROM trucks
# LEFT JOIN reviews ON trucks.id = reviews.truck_id
# GROUP BY trucks.name, trucks.id
# ORDER BY trucks.name;

# SELECT trucks.name, COUNT(reviews.id) AS num_reviews, ROUND(AVG(reviews.rating))
# AS average_rating FROM trucks
# LEFT JOIN reviews ON trucks.id = reviews.truck_id
# GROUP BY trucks.name, trucks.id
# ORDER BY trucks.name;

# SELECT t.name, COUNT(tmi.menu_item_id) AS num_items,
# ROUND(AVG(tmi.price)::numeric, 2) AS avg_price
# FROM trucks t
# LEFT JOIN truck_menu_items tmi ON t.id = tmi.truck_id
# GROUP BY t.id, t.name
# ORDER BY t.name DESC;

# -- Write you SELECT statement here
# SELECT t.name, SUM(mi.calories) AS total_calories
# FROM trucks t
# JOIN truck_menu_items tmi ON tmi.truck_id = t.id
# JOIN menu_items mi ON mi.id = tmi.menu_item_id
# GROUP BY t.name;