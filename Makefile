all: create_df create_db check_db

create_df:
	mkdir -p data/input
	mkdir -p data/output
	python 00_create_random_dataframe.py

create_db:
	python 01_create_database_from_csv.py

check_db:
	python 02_check_tables_in_database.py

.PHONY: clean r-workaround
clean:
	rm -rf data
	rm *.db

r-workaround: create_df create_db
	Rscript 02_check_tables_in_database.R
