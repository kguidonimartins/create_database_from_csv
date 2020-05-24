.DEFAULT_GOAL := help

all: create_df create_db check_db ## run create_df, create_db, and check_db

create_df: ## create dfs needed for below tasks
	mkdir -p data/input
	mkdir -p data/output
	python 00_create_random_dataframe.py

create_db: create_df ## create dbs based on dfs created in above command
	python 01_create_database_from_csv.py

check_db: create_db ## check created dbs
	python 02_check_tables_in_database.py

.PHONY: clean r-workaround help
clean: ## clean data/ and *.db
	rm -rf data
	rm *.db

r-workaround: create_df create_db ## R lang workaround
	Rscript 02_check_tables_in_database.R

help: ## show this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

