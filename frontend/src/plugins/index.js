/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import * as api from './axios.js'

export function registerPlugins (app) {
  app.use(vuetify)
  app.use(api.VueAxiosPlugin, api.axiosInstance)
}
