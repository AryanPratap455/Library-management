import Home from './components/Home.vue'
import LibrarianRegister from './components/LibrarianRegister.vue'
import UserRegister from './components/UserRegister.vue'
import UserLogin from './components/UserLogin.vue'
import LibrarianLogin from './components/LibrarianLogin.vue'
import LibrarianHome from './components/LibrarianHome.vue'
import UserHome from './components/UserHome.vue'
import IssueRequest from './components/IssueRequest.vue'
import UserIssuePage from './components/UserIssuePage.vue'
import StatsLibrarian from './components/StatsLibrarian.vue'
import {createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        name:'Home', 
        component:Home,
        path:'/'
    },
    {
        name:'LibrarianRegister',
        component:LibrarianRegister,
        path:'/librarianregister'
    },
    {
        name:'UserRegister',
        component:UserRegister,
        path:'/userregister'
    },
    {
        name:'UserLogin',
        component:UserLogin,
        path:'/userlogin'
    },
    {
        name:'LibrarianLogin',
        component:LibrarianLogin,
        path:'/librarianlogin'
    },
    {
        name:'LibrarianHome',
        component:LibrarianHome,
        path:'/librarianhome'
    },
    {
        name:'UserHome',
        component:UserHome,
        path:'/userhome'
    },
    {
        name:'IssueRequest',
        component:IssueRequest,
        path:'/issuerequest'
    },
    {
        name:'UserIssuePage',
        component:UserIssuePage,
        path:'/userissuepage'
    },
    {
        name:'StatsLibrarian',
        component:StatsLibrarian,
        path:'/statslibrarian'
    }
];

const router=createRouter({
    history:createWebHistory(),
    routes
});

export default router
