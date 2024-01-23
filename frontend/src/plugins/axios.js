import axios from 'axios'
import VueAxios from 'vue-axios'

export let axiosInstance = axios.create({
  baseURL: 'http://localhost:2333',
  timeout: 3000,
})

export let VueAxiosPlugin = VueAxios