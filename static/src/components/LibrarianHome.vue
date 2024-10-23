<template>
    <div class="app-container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Librarian Dashboard</a>
                <a class="navbar-brand" href="/issuerequest">IssueRequest</a>
                <a class="navbar-brand" href="/statslibrarian">Stats</a>
                <a class="navbar-brand" @click="logout">Logout</a>
            </div>
        </nav>

        <!--- Creating Section and Book  -->

        <div class="bg-primary mt-4 mb-4 pt-3 pb-3">
            <!-- Button trigger modal -->
            <button type="button" class="btn btn-warning text-dark" data-bs-toggle="modal" data-bs-target="#exampleModal">
                +Create more section
            </button>

            <!-- Modal for creating section -->

            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Add more section here</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="mb-2">
                                <label>Section name :</label>
                                <input v-model="section_name" type="text">
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" @click="addsection" class="btn btn-primary"
                                data-bs-dismiss="modal">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!--  Model for creating book -->

        <div class="modal fade" id="exampleModal_show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add more book here</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-2">
                            <label>Book name :</label>
                            <input v-model="book_name" type="text">
                        </div>
                        <div class="mb-2">
                            <label>Authors :</label>
                            <input v-model="authors" type="text">
                        </div>
                        <div class="mb-2">
                            <label>File :</label>
                            <input name="file" type="file">
                        </div>
                        <div class="mb-2">
                            <label>section id :</label>
                            <input v-model="section_id" type="integer">
                        </div>
                    </div>

                    <div class=" modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" @click="addbook" class="btn btn-primary"
                            data-bs-dismiss="modal">Submit</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Content of Section and Books-->

        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-5 mb-5 ms-5" v-for="sec in msg[0]">

                    <!-- Modal for updating section -->

                    <div class="modal fade" id="UpdateSection" tabindex="-1" aria-labelledby="exampleModalLabel"
                        aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Change the data below for update
                                        section</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                                        aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <div class="mb-2">
                                        <label>Section Name :</label>
                                        <input v-model="section_name" type="text">
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                    <button type="button" @click="updateSection(sec.id)" class="btn btn-primary"
                                        data-bs-dismiss="modal">Submit</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- content of section and book  -->

                    <div class="card">
                        <div class="card-body bg-warning">
                            <h3 class="card-title text-danger">Section-{{ sec.id }}: {{ sec.section_name }}</h3>
                            <hr>
                            <button type="button" class="btn btn-success mb-1" data-bs-toggle="modal"
                                data-bs-target="#exampleModal_show">Create Book</button>

                            <!-- inside each section for action on book  -->

                            <div class="row">
                                <div class="col-sm-6" v-for="book in msg[1]">

                                    <!-- Modal for updating  book  -->
                                    <div class="modal fade" id="UpdateBook" tabindex="-1"
                                        aria-labelledby="exampleModalLabel" aria-hidden="true">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Change the data
                                                        below for update book</h1>
                                                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                                                        aria-label="Close"></button>
                                                </div>
                                                <div class="modal-body">
                                                    <div class="mb-2">
                                                        <label>Book name :</label>
                                                        <input v-model="book_name" type="text">
                                                    </div>
                                                    <div class="mb-2">
                                                        <label>Authors :</label>
                                                        <input v-model="authors" type="text">
                                                    </div>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary"
                                                        data-bs-dismiss="modal">Close</button>
                                                    <button type="button" @click="updateBook(book.book_id)"
                                                        class="btn btn-primary" data-bs-dismiss="modal">Submit</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                                
                                    <div class="card" v-if="book.section_id_r == sec.id">
                                        <div class="card-body">
                                            <h5 class="card-title">{{ book.book_name }} </h5>
                                            <p class="card-text">{{ book.authors }}</p>
                                            <button type="button" class="btn btn-primary text-white me-2 btn-sm"
                                                data-bs-toggle="modal" data-bs-target="#UpdateBook">
                                                Update
                                            </button>
                                            <button @click="deleteBook(book.book_id)"
                                                class="btn btn-danger btn-sm">Delete</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <hr>
                            <button type="button" @click="updateSection(sec.id)" class="btn btn-primary text-white me-2" data-bs-toggle="modal"
                                data-bs-target="#UpdateSection">
                                Update Section
                            </button>
                            <button @click="deleteSection(sec.id)" class="btn btn-danger">Delete section</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.app-container {
    background-color: #48d8eb;
    min-height: 100vh;
    padding-bottom: 20px;
}
</style>
<script>
import axios from 'axios'
export default {
    name: 'LibrarianHome',

    data: function () {
        return {
            msg: [],
            section_name: "",

            book_name: "",
            authors: "",
            file_data: "",
            section_id: ""

        }
    },

    methods: {
        getResponse() {
            const path = 'http://localhost:5000/librarianhome';
            axios.get(path)
                .then((res) => {
                    console.log(res.data);
                    this.msg = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        },

        addsection: function () {
            const postJSON = async (data)=> {
                try {
                    const response = await fetch("http://localhost:5000/createsection", {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    this.getResponse();
                    console.log("Success:", result);
                } catch (error) {
                    console.error("Error:", error);
                }
            };
            const data = {
                section_name: this.section_name,
            };
            postJSON(data);
        },

        addbook: async function () {
            const formData = new FormData();
            formData.append("book_name", this.book_name);
            formData.append("authors", this.authors);
            formData.append("section_id", this.section_id);

            // Get the file input element
            const fileInput = document.querySelector('input[name="file"]');

            // Check if a file is selected
            if (fileInput.files.length > 0) {
                // Append the file to the FormData object
                formData.append("file", fileInput.files[0]);
                console.log("File selected:", fileInput.files[0]);
            } else {
                console.log("No file selected");
            }

            try {
                const response = await fetch("http://localhost:5000/createbook", {
                    method: "POST",
                    body: formData,
                });

                const results = await response.json();
                console.log("Success:", results);
                this.getResponse();
            } catch (error) {
                console.error("Error:", error);
            }
        },


        updateSection: function (id) {
            console.log(id);
            const postJSON = async (data, id) => {
                try {
                    const response = await fetch(`http://localhost:5000/updatesection/${id}`, {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    this.getResponse();
                    console.log("Success:", result);
                } catch (error) {
                    console.error("Error:", error);
                }
            }

            const data = {
                section_name: this.section_name
            };
            postJSON(data, id);
            console.log(id);

        },

        updateBook: async function (book_id) {
            console.log(book_id);
            const postJSON = async (data, book_id) => {
                try {
                    const response = await fetch(`http://localhost:5000/updatebook/${book_id}`, {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    this.getResponse();
                    console.log("Success:", result);
                } catch (error) {
                    console.error("Error:", error);
                }
            }

            const data = {
                book_name: this.book_name,
                authors:this.authors
            };
            postJSON(data, book_id);
            console.log(book_id);
           
        },

        deleteSection: function (id) {
            console.log(id);
            fetch(`http://localhost:5000/deletesection/${id}`)
            .then(r => r.json())
            .then(d => {
                console.log(" Section deleted");
                this.getResponse();
            })
        },

        deleteBook: function (book_id) {
            console.log(book_id);
            fetch(`http://localhost:5000/deletebook/${book_id}`)
            .then(r => r.json())
            .then(d => {console.log(" Book deleted")
            this.getResponse();
            }) 
        },

        logout() {
            console.warn('Logout called');
            fetch(`http://localhost:5000/logoutlibrarian`)
                .then(r => r.json())
                .then(d => {
                    console.log("Logout done");
                    console.log(JSON.stringify(d)); // Log the JSON data
                });
            //localStorage.clear();
            this.$router.push({ name: 'LibrarianLogin' });
        }
    },

    created() {
        this.getResponse();
    }
}
</script>