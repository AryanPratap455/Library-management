<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Librarian Dashboard</a>
            <a class="btn btn-dark text-light" href="/librarianhome" role="button">Home</a>
            <a class="navbar-brand" href="#">Logout</a>
        </div>
    </nav>

    <div class="bg-warning mt-2 mb-2 pt-3 pb-3 ms-5 me-5">
        <div class="text-danger">
            <h3>Book issue request is below</h3>
        </div>
    </div>
    <div class="card m-5" v-for="block in dataa[0]">
        <div class="card-header bg-success text-white">
            Section-{{ block.section_name }}
        </div>
        <div class="card-body bg-primary text-white">
            <blockquote class="blockquote mb-0">
                <p style="float:left; ">Book name : {{block.book_name}}</p>
                <button type="button" class="btn btn-success" @click="confirm1(block.book_id)">Confirm</button>
                <button type="button" class="btn btn-danger" @click="confirm2(block.book_id)">Reject</button>
                <p style="float:right; ">Username : {{block.user_email}}</p>
            </blockquote>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'IssueRequest',
    data: function () {
        return {
            dataa: []
        }
    },
    methods: {
        getResponse() {
            const path = `http://localhost:5000/requestdata`;
            axios.get(path)
                .then((res) => {
                    console.log(res.data);
                    this.dataa = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        confirm1: function (book_id) {
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/confirmrequest/${book_id}`, {
                        method: "POST",
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
                book_id: this.book_id,
                status: "approved"
            };
            postJSON(data);
        },
        confirm2: function (book_id) {
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/confirmrequest/${book_id}`, {
                        method: "POST",
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
                book_id: this.book_id,
                status: "reject"
            };
            postJSON(data);
        }
    },
    created() {
        this.getResponse();
    }
}
</script>