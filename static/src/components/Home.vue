<!--
<template>
  <div class="container-fluid bg-warning pb-5">
    <div class="container-fluid text-white bg-primary pt-5 pb-5">
      <h1>Welcome to Library Management app</h1>
    </div>

    <div class="row mt-5 ms-5 me-5 pb-5">

      <div class="col-sm-6 mb-3 mb-sm-0">
        <div class="card pb-5 pt-4">
          <div class="card-body">
            <h5 class="card-title">Librarian Block</h5>
            <p class="card-text"><router-link to="librarianregister">Librarian Registration</router-link></p>
            <p class="card-text"><router-link to="librarianlogin">Librarian Login </router-link></p>
          </div>
        </div>
      </div>

      <div class="col-sm-6">
        <div class="card pb-5 pt-4">
          <div class="card-body">
            <h5 class="card-title">User Block</h5>
            <p class="card-text"><router-link to="userregister">User Registration</router-link></p>
            <p class="card-text"><router-link to="userlogin">User Login </router-link></p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>
-->

<template>
  <div>
    <!-- Header Section -->
    <header class="bg-primary py-3">
      <div class="container">
        <h1 class="text-white text-center mb-0">Library Management App</h1>
      </div>
    </header>

    <!-- Main Content Section -->
    <section class="bg-light py-5">
      <div class="container">
        <div class="row justify-content-center">
          <!-- Librarian Block -->
          <div class="col-lg-4 col-md-6 mb-4">
            <div class="card border-0 shadow">
              <div class="card-body text-center">
                <h2 class="card-title text-primary mb-4">Librarian Block</h2>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item border-0">
                    <router-link class="btn btn-primary btn-block" to="librarianregister">Librarian Registration</router-link>
                  </li>
                  <li class="list-group-item border-0">
                    <router-link class="btn btn-primary btn-block" to="librarianlogin">Librarian Login</router-link>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <!-- User Block -->
          <div class="col-lg-4 col-md-6 mb-4">
            <div class="card border-0 shadow">
              <div class="card-body text-center">
                <h2 class="card-title text-primary mb-4">User Block</h2>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item border-0">
                    <router-link class="btn btn-primary btn-block" to="userregister">User Registration</router-link>
                  </li>
                  <li class="list-group-item border-0">
                    <router-link class="btn btn-primary btn-block" to="userlogin">User Login</router-link>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Custom CSS for additional styling */
.card {
  border-radius: 20px;
}

.card-title {
  font-size: 1.75rem;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

/* Adjust the color scheme */
.bg-primary {
  background-color: #343a40 !important;
}

.text-primary {
  color: #007bff !important;
}
</style>




<script>
import axios from 'axios'
export default {
  name: 'Front',
  data() {
    return {
      msg: 'Aryan'
    }
  },
  methods: {
    getResponse() {
      const path = 'http://localhost:5000/shark';
      axios.get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        })
    }
  },
  created() {
    this.getResponse();
  }
}
</script>