# Samiyoddin Mohammed: Projects

Welcome. This repository holds my data, software, and web projects. Browse the folders below to see each one.

## Projects

### Full-Stack Todo App (`todo-app/`)
A full-stack task manager built with React and Node.js. It uses an Express REST API to create, update, and delete todos stored in MongoDB Atlas, with Mongoose for the database models.
- React frontend built with Vite.
- Express API with create, read, update, and delete routes.
- MongoDB Atlas database connected through Mongoose schemas.

### Olist E-commerce Analytics Warehouse (`olist-warehouse/`)
A containerized PostgreSQL data warehouse built from the Brazilian Olist e-commerce dataset (99,441 orders).
- Docker Compose runs PostgreSQL 16 and Metabase.
- Python (psycopg) bulk-loads raw CSV files with `COPY`, with idempotent reloads via `TRUNCATE`.
- SQL builds raw, staging, and marts schemas, with type casting and data quality checks.
- `marts.fct_orders` is a fact table at one row per order, feeding a Metabase dashboard of monthly revenue and order trends.

### Python ETL Data Pipeline (`sales-etl-project/`)
An ETL pipeline that generates data, cleans it, and loads it into a database file and CSV output, with SQL queries and Power BI dashboards on top.

### Customer Review Sentiment Analyzer (`sentiment-analysis/customer-sentiment-ai/`)
A machine learning model that classifies customer reviews as positive, negative, or neutral, and summarizes the percentage in each category.

### Personal Project Website (`index.html`, `style.css`)
A responsive, dark-themed site built with vanilla HTML, CSS, and JavaScript. It includes a file character scanner, a word highlighter, a persistent color voting chart, and live weather and movie search powered by free public APIs.

## Skills
- **Data and databases:** PostgreSQL, SQL, Docker, ETL pipelines, data quality testing, star-schema design, Power BI, Metabase, MongoDB
- **Web development:** React, Node.js, Express, HTML, CSS, JavaScript
- **Programming:** Python, JavaScript, Java, Dart
- **Machine learning:** text classification and sentiment analysis
- **Tools:** Git, GitHub, Linux, Windows, Vite

## Contact
- Email: mhd.sami0208@gmail.com
- GitHub: https://github.com/SamiyMohammed

## Live Site
https://samiymohammed.github.io/projectsmine/
