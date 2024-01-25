import axios from 'axios'
import VueAxios from 'vue-axios'

export let axiosInstance = axios.create({
  baseURL: "https://yanghoo.online/api",
  timeout: 3000,
})

export let VueAxiosPlugin = VueAxios