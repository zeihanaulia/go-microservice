package main

import (
	"fmt"
	"log"
	"os"

	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

func main() {
	os.Setenv("APP_DB_USERNAME", "root")
	os.Setenv("APP_DB_PASSWORD", "postgres")
	os.Setenv("APP_DB_NAME", "root")

	connectionString := fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable",
		os.Getenv("APP_DB_USERNAME"),
		os.Getenv("APP_DB_PASSWORD"),
		os.Getenv("APP_DB_NAME"),
	)
	fmt.Println(connectionString)
	db, err := sqlx.Open("postgres", connectionString)
	if err != nil {
		log.Fatal(err)
	}

	a := App{}
	a.Initialize(db)
	a.Run(":8080")
}
