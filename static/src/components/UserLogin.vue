<!--
<template>
    <div class="container-fluid bg-warning pb-3">
         <div class="container-fluid text-white bg-primary pt-5 pb-5">
             <a class="btn btn-success mb-2 mt-0" style="float:left" href="/" role="button">Home</a>
             <h1>User Login page</h1>
         </div>
 
         <div class="row mt-5 ms-5 me-5 pb-5">
 
             <div class="col-sm-6 mb-3 mb-sm-0 ms-5">
                 <div class="card pb-5 pt-4">
                     <div class="card-body">
                         <h5 class="card-title">Login</h5>
                         <form @submit.prevent="loginUser">
                             <div class="email mt-3">
                                 <label>Email :</label>
                                 <input type="email" v-model="email" />
                             </div>
                             <div class="password mt-3">
                                 <label>Passsword :</label>
                                 <input type="password" v-model="password" />
                             </div>
                             <button type="submit" class="btn btn-primary mt-3">Login</button>
                         </form>
                     </div>
                     <p>Don't have account click here for register</p>
                     <p class="card-text"><router-link to="userregister">User Registration</router-link></p>
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
        <h1 class="text-white mb-0">User Login Page</h1>
        <div></div>
        <!-- Add an empty div to maintain space for Home button -->
      </div>
    </div>

    <!-- Main Content Section -->
    <div class="container-fluid pb-3">
      <div class="container">
        <div class="row justify-content-center mt-5">
          <div class="col-md-6 ms-5">
            <div class="card border-0 shadow">
              <div class="card-body">
                <h2 class="card-title text-primary text-center mb-4">Login</h2>
                <form>
                  <div class="form-group">
                    <label for="email">Email:</label>
                    <input
                      type="email"
                      class="form-control"
                      id="email"
                      v-model="email"
                    />
                  </div>
                  <div class="form-group">
                    <label for="password">Password:</label>
                    <input
                      type="password"
                      class="form-control"
                      id="password"
                      v-model="password"
                    />
                  </div>
                  <button
                    type="button"
                    @click="loginUser"
                    class="btn btn-primary btn-block mt-3"
                  >
                    Login
                  </button>
                </form>
                <p class="mt-3">
                  Don't have an account? Click here to register.
                </p>
                <p class="card-text">
                  <router-link to="userregister">User Registration</router-link>
                </p>
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

.bg-primary {
  background-color: #007bff !important;
}

.bg-warning {
  background-color: #ffc107 !important;
}
</style>
<script>
import axios from "axios";
export default {
  name: "UserLogin",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async loginUser() {
      if (!this.username && !this.password) {
        alert("Please enter both the username and the password !!");
        return;
      }
      await axios
        .post("http://localhost:5000/loginuser", {
          email: this.email,
          password: this.password,
        })
        .then((res) => {
          if (res.data.status === "success") {
            console.log(res.data.sesn);
            this.$router.push({ name: "UserHome" });
            alert("Logged in successfully");
          } else {
            console.log(res);
            alert("Invalid email or password data !!");
          }
        });
    },
  },
};
</script>
