<template>
    <div class="app-container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">User: {{ msg[2] }}</a>
                <a class="navbar-brand" href="userissuepage">Issued Page</a>
                <input type="text" v-model="search" placeholder="search here" />
                <a class="btn btn-dark text-white" @click="Search" role="button">Search</a>
                <a class="navbar-brand" @click="logout">Logout</a>
            </div>
        </nav>
        <div class="output">{{ search.status }}</div>
        <br />
        <div class="random" v-for="i in search.val">
            <a class="output" href="/userhome" role="button">{{ i }}</a>
        </div>
        <!-- Content of the page -->
        <div class="container mt-4">
            <div class="row">
                <div class="col-12 col-md-6 col-lg-4 mb-4" v-for="sec in msg[0]" :key="sec.id">
                    <div class="card">
                        <div class="card-header bg-primary text-white">Section-{{ sec.id }}</div>
                        <div class="card-body bg-warning">
                            <div class="row row-cols-1 row-cols-md-2 g-4">
                                <div class="col" v-for="book in msg[1]" :key="book.id">
                                    <div v-if="book.section_id_r == sec.id">
                                        <div class="card">
                                            <div class="card-body">
                                                <h5 class="card-title text-primary">
                                                    {{ book.book_name }}
                                                </h5>
                                                <p class="card-text text-success">Authors: {{ book.authors }}</p>
                                                <button
                                                    type="button"
                                                    class="btn btn-primary"
                                                    @click="issueRequest(book.book_id)"
                                                >
                                                    Issue
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.app-container {
    background-color: #48d8eb; /* Set the desired background color */
    min-height: 100vh; /* Ensure the container stretches to at least the height of the viewport */
    padding-bottom: 20px; /* Add padding at the bottom as needed */
}
</style>
<script>
import axios from "axios";
export default {
    name: "UserHome",
    data: function () {
        return {
            msg: [],
            search: "",
        };
    },
    methods: {
        getResponse() {
            const path = "http://localhost:5000/userhome";
            axios
            .get(path)
            .then((res) => {
                console.log(res.data);
                this.msg = res.data;
            })
            .catch((err) => {
                console.error(err);
            });
        },
        logout() {
            console.warn("Logout called");
            fetch(`http://localhost:5000/logoutuser`)
            .then((r) => r.json())
            .then((d) => {
                console.log("Logout done");
                console.log(JSON.stringify(d)); // Log the JSON data
            });
            //localStorage.clear();
            this.$router.push({name: "UserLogin"});
        },
        issueRequest: function (book_id) {
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/issueRequest/${book_id}`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    if (response.ok) {
                        const result = await response.json();
                        console.log("Success:", result);
                        alert("Issue request sent successfully");
                    } else if (response.status === 400) {
                        const errorText = await response.text();
                        console.error("Error:", errorText);
                        alert("Maximum limit for issue requests exceeded.");
                    } else {
                        throw new Error("Failed to send issue request");
                    }
                } catch (error) {
                    console.error("Error:", error);
                }
            }
            const data = {
                book_id: this.book_id,
            };
            postJSON(data);
        },

        Search: function () {
            const vm = this;
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/search`, {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    console.log(result.status);
                    vm.search = result;
                } catch (error) {
                    console.error("Error:", error);
                }
            }
            const data = {
                search: this.search,
            };
            postJSON(data);
            //this.$router.push({ name: 'Search_output' });
        },
    },
    created() {
        this.getResponse();
    },
};
</script>
