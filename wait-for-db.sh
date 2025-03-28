#!/bin/sh

echo "Waiting db to be ready"

until pg_isready -h db -p 5432 -U postgres
do
  sleep 1
done

echo "Database is ready! Starting the application.."
exec "$@"
