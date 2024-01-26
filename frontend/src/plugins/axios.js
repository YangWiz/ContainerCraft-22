import axios from 'axios'
import VueAxios from 'vue-axios'

export let axiosInstance = axios.create({
  baseURL: "api-service.default.svc.cluster.local/api",
  timeout: 3000,
})

export let VueAxiosPlugin = VueAxios