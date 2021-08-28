# titanic-app

ML API with a postgres and a grafana for Titanic prediction

## Run docker-compose

docker-compose up (you must have docker-compose installed https://docs.docker.com/compose/install/)

## Informations

POSTGRSQL_CONTAINER_NAME: postgres_container

POSTGRES_USER: user

POSTGRES_PASSWORD: userpwd


PGADMIN_EMAIL: pgadmin4@pgadmin.org

PGADMIN_PASSWORD: admin


GRAFANA_USER: admin

GRAFANA_PASSWORD: admin

## Endpoints
 / => home (methods = ["GET"]) 
 
 /predict => prediction (methods = ["GET","POST"])
 
    Body example : { "PassengerId":343,
                    "Pclass":2,
                    "Name":"Collander, Mr. Erik Gustaf",
                    "Sex":"male",
                    "Age":28.0,
                    "SibSp":0,
                    "Parch":0,
                    "Ticket":"248740",
                    "Fare":13.0,
                    "Cabin":null,
                    "Embarked":"S" }
