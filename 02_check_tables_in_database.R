if (!require("tidyverse")) install.packages("tidyverse")
if (!require("DBI")) install.packages("DBI")
if (!require("RSQLite")) install.packages("RSQLite")
if (!require("dbplyr")) install.packages("dbplyr")

database <- DBI::dbConnect(RSQLite::SQLite(), "test_small_db.db")

src_dbi(database)

table_list <- dbListTables(database)

table_list

database %>%
  dbReadTable(table_list[1]) %>%
  head()

table_00 <-
  table_list %>%
  .[1] %>%
  tbl(database, .)

table_00 %>%
  head()

table_list %>%
  .[1] %>%
  tbl(database, .) %>%
  select(A, C) %>%
  filter_if(is.numeric, all_vars(. > 500)) %>%
  show_query()
