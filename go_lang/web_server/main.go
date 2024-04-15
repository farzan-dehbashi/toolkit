package main

import (
	"fmt"
	"log"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/hello" {
		http.Error(w, "404 not found", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "METHOD NOT FOUND", http.StatusNotFound)
		return
	}

	fmt.Fprintf(w, "hello world")
}

func formHandler(w http.ResponseWriter, r *http.Request) {
	if err := r.ParseForm(); err != nil {
		fmt.Fprintf(w, "could not fparse form")
	}
	fmt.Fprint(w, "Post successful")
	name:= r.FormValue("name")
	address:= r.FormValue("address")
	fmt.Fprintf(w, name, address)
}

func main() {
	fileServer := http.FileServer(http.Dir("./html"))
	http.Handle("/", fileServer)
	http.HandleFunc("/form", formHandler)
	http.HandleFunc("/hello", helloHandler)

	fmt.Println("Starting server at port 8080...")
	if err:= http.ListenAndServe(":8089", nil); err != nil {
		log.Fatal(err)
	}
}
