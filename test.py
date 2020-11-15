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
  if (select): selectName = True


  # take state, set flag
  state = input("Input state: ")
  if state: searchByState = True
  select = input("is a selection?")
  if (select): selectState = True

  # take category, set flag 
  category = input("Input category: ")
  if category: searchByCategory = True

  select = input("is a selection?")
  if (select): selectCategory = True

  # take limit, set flag
  limit = input("Input query-size limit: ")
  if limit: limitResults = True
  else: limitResults = False

  in = input("Is ordered by stars?")
  if in: orderedByStars = True
  else: orderedByStars = False

  # Clean leading/trailing whitepace
  name = name.strip()
  state = state.strip()
  category = category.strip()
  

searchByName = True
searchByState = True
searchByCategory = True
selectName = True
selectState = True
selectCategory = False

if HARDCODE:
  name = "business name"
  state = "TX"
  category = "Shopping"

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

if not orderedByStars:
  selectStr = "SELECT "
  selectLs = []
  if selectName: selectLs.append('business_review.name')
  if selectState: selectLs.append('business_review.state')
  if selectCategory: selectLs.append('business_category.category')
  for i in range(len(selectLs)):
    selectStr += f"{selectLs[i]}"
    if i > 1 or i < len(selectLs)-1:
      selectStr += ", "

  fromStr = "FROM "
  if searchByName: fromStr += "business_review"
  elif searchByState: fromStr += "business_location"
  elif searchByCategory: fromStr += "business_category"

  if searchByName and searchByState and not searchByCategory:
    joinStr1 = "JOIN business_location ON business_review.business_id = business_location.business_id"
    whereStr1 = f"WHERE state LIKE '%{state}%'"
    jointStr2 = ""
    whereStr2 = ""
  if searchByName and searchByCategory and not searchByState:
    joinStr1 = "JOIN business_category ON business_review.business_id = business_category.business_id"
    whereStr1 = f"WHERE category LIKE '%{category}%'"
    jointStr2 = ""
    whereStr2 = ""
  if searchByName and searchByState and searchByCategory:
    joinStr1 = "JOIN business_location ON business_review.business_id = business_location.business_id"
    joinStr2 = "JOIN business_category ON business_review.business_id = business_category.category"
    whereStr1 = f"WHERE state LIKE '%{state}%'"
    whereStr2 = f"AND category LIKE '%{category}%'"
else:


print(selectStr)
print(fromStr)
print(joinStr1)
print(joinStr2)
print(whereStr1)
print(whereStr2)

