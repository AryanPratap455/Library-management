<template>
  <div class="app-container">
    <!-- Navigation bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="librarianhome">Librarian Dashboard</a>
      </div>
    </nav>

    <!-- Main content area -->
    <main class="main-content">
      <!-- Display images using v-for directive -->
      <div v-for="(imageUrl, index) in imageUrls" :key="index">
        <img v-if="imageUrl" :src="imageUrl" :alt="'Graph ' + (index + 1)">
      </div>
    </main>
  </div>
</template>

<!-- Add styles if needed -->
<style>
  /* Styles for the app container */
  .app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh; /* Ensure the container takes up the full height of the viewport */
  }

  /* Styles for the main content area */
  .main-content {
    flex: 1; /* Allow the main content area to grow and take up remaining vertical space */
    padding: 20px; /* Add padding for spacing */
    display: flex;
    flex-wrap: wrap; /* Allow images to wrap to the next line if necessary */
    justify-content: center; /* Center images horizontally */
    align-items: center; /* Center images vertically */
  }

  /* Style for images */
  img {
    max-width: 100%; /* Ensure images don't exceed their container width */
    height: auto; /* Maintain image aspect ratio */
    margin: 10px; /* Add margin around images for spacing */
  }
</style>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      imageUrls: []
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/stats"; // Backend URL
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.imageUrls = [
            "http://localhost:5000" + res.data.books_per_section_url,
            "http://localhost:5000" + res.data.issues_per_book_url
          ];
        })
        .catch((err) => {
          console.error("Error fetching images:", err);
        });
    }
  },
  created() {
    this.getResponse();
  }
};
</script>
