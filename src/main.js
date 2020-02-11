import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import * as firebase from "firebase/app";
import VeeValidate, { Validator } from "vee-validate";
import ja from "vee-validate/dist/locale/ja.js";
import { VLazyImagePlugin } from "v-lazy-image";
import "./assets/scss/fonts.scss";

Vue.config.productionTip = false;

const firebaseConfig = {
  // Your Key
};

Vue.use(VLazyImagePlugin);
Vue.use(VeeValidate, {
  events: "change"
});
Validator.localize("ja", ja);
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
