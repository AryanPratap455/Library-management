<!---
<template>
  <div class="container-fluid bg-warning pb-3">
    <div class="container-fluid text-white bg-primary pt-5 pb-5">
      <a class="btn btn-success mb-2 mt-0" style="float:left" href="/" role="button">Home</a>
      <h1>User Register page</h1>
    </div>

    <div class="row mt-5 ms-5 me-5 pb-5">

      <div class="col-sm-6 mb-3 mb-sm-0">
        <div class="card pb-5 pt-4">
          <div class="card-body">
            <h5 class="card-title">Register here</h5>
            <form>
              <div class="email mt-3">
                <label>Email :</label>
                <input v-model="email" type="email" />
              </div>
              <div class="password mt-3">
                <label>Passsword :</label>
                <input v-model="password" type="password" />
              </div>
              <button type="button" @click="signUp" class="btn btn-primary mt-3">Register</button>
            </form>
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
    <div class="container-fluid bg-primary py-3">
      <div class="container d-flex justify-content-between align-items-center">
        <a class="btn btn-success" href="/" role="button">Home</a>
        <h1 class="text-white mb-0">User Register Page</h1>
        <div></div> <!-- Add an empty div to maintain space for Home button -->
      </div>
    </div>

    <!-- Main Content Section -->
    <div class="container-fluid py-3">
      <div class="container">
        <div class="row justify-content-center mt-5">
          <div class="col-md-6">
            <div class="card border-0 shadow">
              <div class="card-body">
                <h2 class="card-title text-primary text-center mb-4">Register Here</h2>
                <form>
                  <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" class="form-control" id="email" v-model="email" required>
                  </div>
                  <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" class="form-control" id="password" v-model="password" required>
                  </div>
                  <button type="button" @click="signUp" class="btn btn-primary btn-block mt-3">Register</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
}

.btn-success:hover {
  background-color: #218838;
  border-color: #218838;
}
</style>


<script>
import axios from 'axios'
export default {
  name: 'UserRegister',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async signUp() {
      if (!this.email || !this.password) {
        alert("All fields are required !!");
        return;
      }

      if (!this.email.includes("@") || !this.email.endsWith(".com")) {
        alert("Invalid email format !! Email must include '@' and end with '.com'");
        return;
      }

      console.warn('Sign Up', this.email, this.password);
      let res = await axios.post("http://localhost:5000/registeruser", {
        email: this.email,
        password: this.password
      });
      console.warn(res);
      if (res.status == 201) {
        console.warn('Sign up done');
      }
      this.$router.push({ name: 'UserLogin' })
      alert('Signed up done successfully');
    }
  }
}
</script>