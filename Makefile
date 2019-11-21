all: create_df create_db

create_df:
	mkdir data
	python 00_create_random_dataframe.py

create_db:
	python 01_create_database_from_csv.py

.PHONY: clean
clean:
	rm -rf data
	rm *.db
