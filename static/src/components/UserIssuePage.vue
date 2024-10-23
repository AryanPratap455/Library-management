<template>
    <div class="app-container">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="userhome">User Dashboard</a>
            <a class="navbar-brand" @click="logout">Logout</a>
        </div>
    </nav>
    <div class="card m-5" v-for="block in dataa[0]">
        <div class="card-header bg-danger text-white">
            Section-{{ block.section_name }}
        </div>
        <div class="card-body bg-primary text-white">
            <blockquote class="blockquote mb-0">
                <p style="float:left; ">Book name-{{ block.book_name }}</p>
                <p style="float:left; margin-left:30%; margin-right:20%">Issue date : {{ block.time }}</p>
                <button type="button" class="btn btn-success " @click="downloadBook(block.book_id)">Download</button>
                <button type="button" class="btn btn-success" style="margin-left: 10px;" @click="viewPDF(block.book_id)">View</button>
            </blockquote>
        </div>
    </div>
</div>
</template>
<style>
    .app-container {
        background-color: #f0f0f0; /* Set the desired background color */
        min-height: 100vh; /* Ensure the container stretches to at least the height of the viewport */
        padding-bottom: 20px; /* Add padding at the bottom as needed */
    }
</style>
<script>
import axios from 'axios'
export default {
    name: 'UserIssuePage',
    data: function () {
        return {
            dataa: []
        }
    },
    methods: {
        getResponse() {
            const path = `http://localhost:5000/userissuepage`;
            axios.get(path)
                .then((res) => {
                    console.log(res.data);
                    this.dataa = res.data;
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        /*downloadBook: function (book_id) {
            const path = `http://localhost:5000/downloadbook/${book_id}`;
            axios.get(path, { responseType: 'blob' }) // Set responseType to 'blob' to receive binary data
                .then((res) => {
                    const url = window.URL.createObjectURL(new Blob([res.data])); // Create a URL object from the blob data
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', 'book.pdf'); // Set the filename for the downloaded file
                    document.body.appendChild(link);
                    link.click();
                    console.log("Download request sent");
                })
                .catch((err) => {
                    console.error(err);
                });
        },*/

        downloadBook: function (book_id) {
            const path = `http://localhost:5000/downloadbook/${book_id}`;
            axios.get(path, { responseType: 'blob' }) // Set responseType to 'blob' to receive binary data
                .then((res) => {
                    const disposition = res.headers['content-disposition'];
                    const filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                    const matches = filenameRegex.exec(disposition);
                    const filename = matches && matches[1] ? matches[1].replace(/['"]/g, '') : 'book.pdf';

                    const url = window.URL.createObjectURL(new Blob([res.data])); // Create a URL object from the blob data
                    const link = document.createElement('a');
                    link.href = url;
                    link.setAttribute('download', filename); // Set the filename for the downloaded file
                    document.body.appendChild(link);
                    link.click();
                    console.log("Download request sent");
                })
                .catch((err) => {
                    console.error(err);
                });
        },

        viewPDF: function (book_id) {
            const path = `http://localhost:5000/viewpdf/${book_id}`;
            axios.get(path, { responseType: 'arraybuffer' }) // Set responseType to 'arraybuffer' to receive binary data
                .then((res) => {
                    const blob = new Blob([res.data], { type: 'application/pdf' });
                    const url = URL.createObjectURL(blob);
                    window.open(url, '_blank'); // Open the PDF file in a new tab
                    console.log("View request sent");
                })
                .catch((err) => {
                    console.error(err);
                });
            }
        },
        created() {
                this.getResponse();
        }
    }
</script>