import axios from 'axios'
import VueAxios from 'vue-axios'

export let axiosInstance = axios.create({
  baseURL: "api/",
  timeout: 3000,
})

export let VueAxiosPlugin = VueAxios