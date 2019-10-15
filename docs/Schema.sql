CREATE TABLE "project" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_date" timestamp,
  "description" text
);

CREATE TABLE "virtual_project" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_date" timestamp,
  "description" text
);

CREATE TABLE "measurement_type" (
  "id" SERIAL PRIMARY KEY,
  "table_name" varchar
);

CREATE TABLE "virutal_project_catalog" (
  "virtual_project_id" int,
  "measurement_type_id" int,
  "measurement_id" int
);

CREATE TABLE "electrolyte_component" (
  "id" SERIAL PRIMARY KEY,
  "component" varchar,
  "concentration" float
);

CREATE TABLE "electrolyte" (
  "id" SERIAL PRIMARY KEY,
  "electrolyte_component_id" int,
  "cell_type_id" int
);

CREATE TABLE "chemistry" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "cell_type" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "vendor" varchar,
  "vendor_batch" varchar,
  "chemistry_id" int,
  "vendor_datasheet" blob
);

CREATE TABLE "cell" (
  "id" SERIAL PRIMARY KEY,
  "cell_type_id" int,
  "created_date" timestamp
);

CREATE TABLE "measurement" (
  "id" SERIAL PRIMARY KEY,
  "cell_id" int,
  "project_id" int,
  "measurement_type_id" int,
  "measurement_id" int
);

CREATE TABLE "cycler_manufacturer" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "created_date" timestamp
);

CREATE TABLE "cycling" (
  "id" SERIAL PRIMARY KEY,
  "cell_id" int,
  "project_id" int,
  "temperature_K" float,
  "data_table_name" varchar,
  "created_date" timestamp,
  "raw_data_filename" varchar,
  "cycler_manufacturer_id" int
);

CREATE TABLE "xps" (
  "id" SERIAL PRIMARY KEY,
  "cell_id" int,
  "project_id" int,
  "temperature_K" float,
  "data_table_name" varchar,
  "created_date" timestamp,
  "raw_data_filename" varchar
);

CREATE TABLE "eis" (
  "id" SERIAL PRIMARY KEY,
  "cell_id" int,
  "project_id" int,
  "temperature_K" float,
  "data_table_name" varchar,
  "created_date" timestamp,
  "raw_data_filename" varchar
);

ALTER TABLE "virutal_project_catalog" ADD FOREIGN KEY ("virtual_project_id") REFERENCES "virtual_project" ("id");

ALTER TABLE "virutal_project_catalog" ADD FOREIGN KEY ("measurement_type_id") REFERENCES "measurement_type" ("id");

ALTER TABLE "electrolyte" ADD FOREIGN KEY ("electrolyte_component_id") REFERENCES "electrolyte_component" ("id");

ALTER TABLE "electrolyte" ADD FOREIGN KEY ("cell_type_id") REFERENCES "cell_type" ("id");

ALTER TABLE "cell_type" ADD FOREIGN KEY ("chemistry_id") REFERENCES "chemistry" ("id");

ALTER TABLE "cell" ADD FOREIGN KEY ("cell_type_id") REFERENCES "cell_type" ("id");

ALTER TABLE "measurement" ADD FOREIGN KEY ("cell_id") REFERENCES "cell" ("id");

ALTER TABLE "measurement" ADD FOREIGN KEY ("project_id") REFERENCES "cell" ("id");

ALTER TABLE "measurement" ADD FOREIGN KEY ("measurement_type_id") REFERENCES "measurement_type" ("id");

ALTER TABLE "cycling" ADD FOREIGN KEY ("cell_id") REFERENCES "cell" ("id");

ALTER TABLE "cycling" ADD FOREIGN KEY ("project_id") REFERENCES "project" ("id");

ALTER TABLE "cycling" ADD FOREIGN KEY ("cycler_manufacturer_id") REFERENCES "cycler_manufacturer" ("id");

ALTER TABLE "xps" ADD FOREIGN KEY ("cell_id") REFERENCES "cell" ("id");

ALTER TABLE "xps" ADD FOREIGN KEY ("project_id") REFERENCES "project" ("id");

ALTER TABLE "eis" ADD FOREIGN KEY ("cell_id") REFERENCES "cell" ("id");

ALTER TABLE "eis" ADD FOREIGN KEY ("project_id") REFERENCES "project" ("id");
