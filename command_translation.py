############### not a working scipt, sketch of current ideas ###############

"""
Translates user input to valid pSQL commands
Step-by-step to approach to easier implement in Java
"""

"""
Query pipeline
User -> GUI -> TranslationAPI -> pSQL -> TranslationAPI -> Output
"""
HARDCODE = True

if not HARDCODE:
  searchByName = False
  searchByState = False
  searchByCategory = False
  selectName = False
  selectState = False
  selectCategory = False

  ## Mimic GUI input for some attributes, set flag for valid inputs (may remove these)
  # take name, set flag
  name = input("Input business name: ")
  if name: searchByName = True
  select = input("is a selection?")
  selectName = False
  if (select): selectName = True


  # take state, set flag
  state = input("Input state: ")
  if state: searchByState = True
  select = input("is a selection?")
  selectName = False
  if (select): selectState = True

  # take category, set flag 
  category = []
  valid_input = True
  while valid_input == True:
    current_category = input("Input category: ")
    if current_category == "-1":
      valid_input = False
      break
    
    category.append(current_category)

  if len(category): searchByCategory = True

  select = input("is a selection?")
  selectName = False
  if (select): selectCategory = True

  # take limit, set flag
  limit = input("Input query-size limit: ")
  if limit: limitResults = True
  else: limitResults = False

  # Clean leading/trailing whitepace
  name = name.strip()
  state = state.strip()
  for e in category: 
    e = e.strip()

  # Verify user input
  def current_values():
    print(f"Business name: {name}")
    print(f"State: {state}")

    for i in range(0, len(category)):
      print(f"Category {i+1}: {category[i]}")

#current_values()  

searchByName = True
searchByState = True
searchByCategory = True
selectName = True
selectState = False
selectCategory = False

if HARDCODE:
  name = "business name"
  state = "TX"
  category = ["cat1", "cat2"]

# Remove repeat elements from list
category = list(set(category))

"""
Java method will look like (encapsulate as a function)

for (Object elem : original_ls) {
  if (!clean_ls.contains(elem))) clean_ls.add(elem);
}
"""

"""
  Compile our dictionary which is key'd by table_name = [col_name_1, ..., col_name_n]
  This is important because we may need to distinguish table and column name in queries
  e.g.
  SELECT business_review.name, business_category.category FROM ...
  instead of
  SELECT name, category FROM ...
"""

"""
```sql
-- 2 attributes, 1 table: Get 10 shopping businesses in TX
--        table      |     col(s)
-- ------------------+------------------      
-- business_category | name, category

--*Start query*--
SELECT business_category.name
FROM business_category
WHERE category LIKE '%Shopping%'
LIMIT 10;
--*end query*--

-- 6 attributes, 2 tables: Get the names, street address and zip of 5 highest rated businesses in WA
--         table      |     col(s)
--  ------------------+------------------  
--  business_location | (pk)business_id, address, zip, state
--  business_review   | (pk)business_id, name, stars_average
  
--*Start query*--
SELECT business_review.name, business_location.address
FROM business_review
INNER JOIN business_location
  ON business_review.business_id = business_location.business_id
WHERE business_location.state LIKE '%WA%'
ORDER BY stars_average DESC
LIMIT 5;
--*end query*--

-- 8 attributes, 3 tables: Get top 10 highest rated Food business in AZ
--*NOTE* AZ has large amount of valid entries, makes a good test candidate
--*NOTE* Always seek to to limit complex queries I/O is always most expensive
--        table      |     col(s)
-- ------------------+------------------  
-- business_category | (pk)business_id, name, category
-- business_location | (pk)business_id, state
-- business_review   | (pk)business_id, stars_average

--*Start query*--
SELECT business_category.name, business_category.category, business_review.stars_average
FROM business_category
JOIN business_location
  ON business_category.business_id = business_location.business_id
JOIN business_review
  ON business_category.business_id = business_review.business_id
WHERE state LIKE '%AZ%'
OR category LIKE '%Food%'
ORDER BY stars_average DESC
LIMIT 10;
--*end query*--
```
"""
table_attribute_dict = {
  'business_category': ['business_id', 'name', 'category'],
  'business_hours':    ['business_id', 'hours_monday', 'hours_tuesday', 'hours_wednesday', 'hours_thursday', 'hours_friday', 'hours_saturday', 'hours_sunday'],
  'business_location': ['business_id', 'address', 'state', 'postal_code', 'latitude', 'longitude'],
  'business_review':   ['business_id', 'name', 'stars_average', 'review_count'],
  'review_content':    ['review_id', 'content', 'datetime'],
  'review_general':    ['review_id', 'stars', 'datetime'],
  'review_key':        ['business_id', 'user_id', 'review_id'],
  'user_general':      ['user_id', 'name', 'review_count', 'stars_average']
}

input_table_dict = {
  'name':     ['business_category', 'business_category.name'],
  'state':    ['business_location', 'business_location.state'],
  'category': ['business_category', 'business_category.category']
}

# 1. compose SELECT list
#   -> Set a select bit for each var
# 2. select the FROM (table w/ the most columns we're selecting)
#   -> take max(len(col_ls))
# 3. decide if we join (tables list > 1)
#   -> If len(tables_ls) > 1
#   -> how?
# 4. OR, AND, "categorical" (anytime we query with a string, or comparison)
#   -> Hardcode categorical inputs
# 5. ORDER if we order
#   -> Take some order bit from the user
# 6. LIMIT
#   -> take some limit from user, default 100

# Construct elementary pSQL queries
def make_queries():
  """
  Target:
  --*Start query*--
  SELECT business_category.name, business_category.category, business_review.stars_average
  FROM business_category
  JOIN business_location
    ON business_category.business_id = business_location.business_id
  JOIN business_review
    ON business_category.business_id = business_review.business_id
  WHERE state LIKE '%AZ%'
  OR category LIKE '%Food%'
  ORDER BY stars_average DESC
  LIMIT 10;
  """

  query_columns_ls = []
  query_tables_ls = []
  query_select_ls = []

  query_select_str = "SELECT "
  query_from_str = "FROM "
  query_join_str = ""
  query_bool_str = ""
  query_order_str = ""
  query_limit_str = ""


  # Extract relevant columns and tables from input_table_dict mappings
  if searchByName:
    query_tables_ls.append(input_table_dict['name'][0])
    query_columns_ls.append(input_table_dict['name'][1])
  if searchByState:
    query_tables_ls.append(input_table_dict['state'][0])
    query_columns_ls.append(input_table_dict['state'][1])
  if searchByCategory:
    query_tables_ls.append(input_table_dict['category'][0])
    query_columns_ls.append(input_table_dict['category'][1])

  # remove dups from tables and col lists
  q_table_ls = []
  for e in query_tables_ls:
    if e not in q_table_ls:
      q_table_ls.append(e)

  q_columns_ls = []
  for e in query_columns_ls:
    if e not in q_columns_ls:
      q_columns_ls.append(e)

  query_tables_ls = q_table_ls
  q_columns_ls = q_columns_ls
  
  if selectName: query_select_ls.append(input_table_dict['name'][1])
  if selectState: query_select_ls.append(input_table_dict['state'][1])
  if selectCategory: query_select_ls.append(input_table_dict['category'][1])

  # generate SELECT
  for i in range(len(query_select_ls)):
    query_select_str += f"{query_select_ls[i]}"
    if i < len(query_select_ls)-1:
      query_select_str += ", "
  
  # generate FROM
  query_from_str += f"{query_tables_ls[0]}"

  # generate JOIN iff
  # -> we alway join on PK
  if len(query_tables_ls) > 1:
    for i in range(len(query_tables_ls)-1):
      current_table = query_tables_ls[i+1]
      c_table_attribute = f"{current_table}.{table_attribute_dict[current_table][0]}"

      base_table = query_tables_ls[0]
      b_table_attribute = f"{base_table}.{table_attribute_dict[base_table][0]}"

      q_join_str = f"JOIN {current_table} ON {b_table_attribute} = {c_table_attribute} "
      query_join_str += q_join_str
  
  # generate WHERE iff
  query_bool_str += f"WHERE state LIKE {state}"

  print(f'{query_select_str}')
  print(f'{query_from_str}')
  print(f'{query_join_str}')


make_queries()  





  
  
   